"""
Python for Revit - Building Custom Tools

Lecture 11 - Accessing Parameters - Part 2

"""

#import the Revit DB and UI namespaces
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

#get current Autodesk Revit project that can interface and interact with settings and operations in the UI
uidoc = __revit__.ActiveUIDocument
#get current Revit database document from the active UI document
doc = __revit__.ActiveUIDocument.Document

#create a filtered element collector object from the current document (required) where the category is Rooms and element is not element type
col_rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType()

#print the value of each parameter called 'Name' for each Room in the model
for x in col_rooms:
	print(x.Number)
	for param in x.GetParameters('Name'):
		print(param.AsString())

#use BuiltInParameter enumerations to extract the built in parameter values
for x in col_rooms:
	if x.get_Parameter(BuiltInParameter.ROOM_DEPARTMENT).AsString() == 'Circulation':
		print(x.get_Parameter(BuiltInParameter.ROOM_NAME).AsString())



