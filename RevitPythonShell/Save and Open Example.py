"""
Python for Revit - Building Custom Tools

Lecture 16 - Save and Open Example

"""

#import the Revit DB and UI namespaces
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

#get current Autodesk Revit project that can interface and interact with settings and operations in the UI
uidoc = __revit__.ActiveUIDocument
#get current Revit database document from the active UI document
doc = __revit__.ActiveUIDocument.Document

#create a filtered element collector containing rooms
col_rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType()

#iterate through the filtered element collector and print the department parameter value for each room
for room in col_rooms:
	print(room.get_Parameter(BuiltInParameter.ROOM_DEPARTMENT).AsString())