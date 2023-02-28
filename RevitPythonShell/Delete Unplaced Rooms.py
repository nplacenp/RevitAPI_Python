"""
Python for Revit - Building Custom Tools

Lecture 24 - Delete Unplaced Rooms

"""

#import the Revit DB and UI namespaces
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

#get current Autodesk Revit project that can interface and interact with settings and operations in the UI
uidoc = __revit__.ActiveUIDocument
#get current Revit database document from the active UI document
doc = __revit__.ActiveUIDocument.Document

#create a filtered element collector containing all room objects in the document
col_rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType()

#create placeholder empty list in order to add any unplaced rooms
unplaced_rooms = []

#iterate through each room object
for room in col_rooms:
    #if the room has not been placed / does not have a location
	if room.Location == None:
        #add the room to the placeholder list
		unplaced_rooms.append(room)

#create a TaskDialog object for the result		
result = TaskDialog

#create TaskDialog common buttons for Yes and No
buttons = TaskDialogCommonButtons.Yes | TaskDialogCommonButtons.No

#if there are any unplaced rooms in the model
if len(unplaced_rooms) > 0:
    #create a TaskDialog object
    confirm = TaskDialog
    #show the confirm TaskDialog object asking the user if they want to delete n number of unplaced rooms and if the result is Yes
    if confirm.Show('Confirm', 'There are {} unplaced room(s) in the model.\n\nDo you want to delete them?'.format(len(unplaced_rooms)), buttons) == TaskDialogResult.Yes:
        #create a transaction in the current document
        t = Transaction(doc)
        #start the transaction, giving the transaction a name / text description
        t.Start('Delete unplaced rooms')
        #iterate through the unplaced_rooms list and delete each room
        for room in unplaced_rooms:
			doc.Delete(room.Id)
        #commit the transaction to the Revit document
        t.Commit()
        #show the result TaskDialog confirming the number of rooms deleted from the model
        result.Show('Result', '{} unplaced room(s) have been deleted from the model'.format(len(unplaced_rooms)))

#if there are no unplaced rooms in the model, show the result TaskDialog stating there are no unplaced rooms
else:
	result.Show('Result', 'There are zero unplaced rooms in the model')

#close the RevitPythonShell output window	
__window__.Close()