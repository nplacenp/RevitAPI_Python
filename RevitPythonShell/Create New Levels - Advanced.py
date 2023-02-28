"""
Python for Revit - Building Custom Tools

Lecture 23 - Create New Levels - Advanced

"""

#import the Revit DB and UI namespaces
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import *
#import the FlexForm and associated components from RevitPythonWrapper
from rpw.ui.forms import (FlexForm, Label, ComboBox, TextBox, TextBox, 
						Separator, Button, CheckBox)

#get current Autodesk Revit project that can interface and interact with settings and operations in the UI
uidoc = __revit__.ActiveUIDocument
#get current Revit database document from the active UI document
doc = __revit__.ActiveUIDocument.Document

#create the components for the FlexForm
components = [Label('Number of Levels'), TextBox('number', Text = '1'), Label('Spacing Between Levels'), 
				TextBox('spacing', Text = '3150'), Button('Create Levels')]

#create the form				
form = FlexForm('Create Levels', components)

#show the form to allow for user input
form.show()

#get the values from the form
spacing = int(form.values.get('spacing'))
number_levels = int(form.values.get('number'))
#set a prefix for the Level names
prefix = 'Level '

#convert the spacing form value to Revit internal units from millimetres
spacing_internal = UnitUtils.ConvertToInternalUnits(spacing, UnitTypeId.Millimeters)

#create a filtered element collector containing the Level instance objects already in the model
col_levels = FilteredElementCollector(doc).OfClass(Level).WhereElementIsNotElementType()

#create a list of the Level names using list comprehension
level_names = [level.Name for level in col_levels]

#create placeholder variable to get elevation of the highest Level
highest_elevation = 0

#iterate through the Levels to find the Level with the highest elevation and set the highest_elevation to that value
for level in col_levels:
	if level.Elevation > highest_elevation:
		highest_elevation = level.Elevation
        
#create a variable for the elevation of the first new Level to be created		
start_elevation = highest_elevation + spacing_internal
		
#create a definition to create the Level name based on the number of digits of the Level name
def level_name(x, y):
	if y < 10:
		return x + '0' + str(y)
	else:
		return x + str(y)

#create a transaction in the current document
t = Transaction(doc)
#start the transaction, giving the transaction a name / text description
t.Start('Create levels')

#iterate through a range of values as defined from the form results
for i in range(number_levels + len(level_names)):
	#using the level_name definition, establish the name of the Level
    new_name = level_name(prefix, i)
    #if the new_name does not exist in the current Revit levels
    if new_name not in level_names:
		#try to create a new level at the starting_elevation and print the result
        try:
			new_level = Level.Create(doc, start_elevation)
			new_level.Name = new_name
			#print(new_name + ' has been created')
        except:
			#print(new_name + ' has not been created')
			pass
		
        #once each new Level is created, add the spacing to the start_elevation to establish the elevation of the next Level to be created
        start_elevation = start_elevation + spacing_internal

#commit the transaction to the Revit document
t.Commit()

#close the RevitPythonShell output window
__window__.Close()