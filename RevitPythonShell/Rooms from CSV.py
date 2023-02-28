
"""
Python for Revit - Building Custom Tools

Lecture 14 - Element Section - From RevitPythonShell

"""

#import the Revit DB and UI namespaces, csv package and pyrevit package
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from pyrevit.forms import pick_file, SelectFromList
import csv

#get current Autodesk Revit project that can interface and interact with settings and operations in the UI
uidoc = __revit__.ActiveUIDocument
#get current Revit database document from the active UI document
doc = __revit__.ActiveUIDocument.Document

#create a definition that will read the provided csv file and return the values as a list
def read_csv(room_list):
	rooms = []
	with open(room_list, 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			rooms.append(row)
		return(rooms)

#select the csv file that contains the room data		
file = pick_file(file_ext = 'csv', multi_file = False)

#if a file has been selected
if file:
	#extract the room data using the defintion above
    room_list = read_csv(file)
	
    #create a filtered element collector containing the phases in the mode (rooms must be created on a specific phase)
	col_phases = FilteredElementCollector(doc).OfClass(Phase)
	
    #create a dictionary
	dic_phase = {}
	
    #set the key to be the phase name and the value to be the phase object
	for phase in col_phases:
		dic_phase[phase.Name] = phase
	
    #show the form asking the user to select the phase they want to create the rooms in
	form = SelectFromList.show(dic_phase.keys(), button_name = 'Select Phase', height = 300, title = 'Select Phase for Rooms')
	
    #get the phase object (value) from the the result of the form (key)
	phase = dic_phase.get(form)
	
    #if a phase was selected
	if phase:
		#create a transaction in the current document
        t = Transaction(doc)
        #start the transaction, giving the transaction a name / text description
		t.Start('Import rooms from CSV')
		
        #iterate through each room, creating a room on the user defined phase and setting parameter values from the indexes within each room list
		for row in room_list[1:]:
			room = doc.Create.NewRoom(phase)
			room.get_Parameter(BuiltInParameter.ROOM_NAME).Set(row[0])
			room.get_Parameter(BuiltInParameter.ROOM_DEPARTMENT).Set(row[1])
		
        #commit the transaction to the Revit document
		t.Commit()

#close the RevitPythonShell output window        
__window__.Close()