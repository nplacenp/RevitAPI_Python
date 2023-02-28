"""
Python for Revit - Building Custom Tools

Lecture 10 - Accessing Parameters - Part 1

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

#iterate through the filtered element collector print Name of the rooms who have a Department of Bedroom
#example using the Lookup() method.
for x in col_rooms:
	if x.LookupParameter('Department').AsString() == 'Bedroom':
		print(x.LookupParameter('Name').AsString())



