"""
Python for Revit - Building Custom Tools

Lecture 27 - Configuring RevitPythonShell

"""

#amend the name of imported classes to create cleaner / succint code
from Autodesk.Revit.DB import FilteredElementCollector as fec, BuiltInCategory as bic

#get current Autodesk Revit project that can interface and interact with settings and operations in the UI
uidoc = __revit__.ActiveUIDocument
#get current Revit database document from the active UI document
doc = __revit__.ActiveUIDocument.Document

#create a filtered element collector containing the room objects in the model
col_rooms = fec(doc).OfCategory(bic.OST_Rooms).WhereElementIsNotElementType()

#print the Department parameter value for each room
for room in col_rooms:
	print(room.get_Parameter(BuiltInParameter.ROOM_DEPARTMENT).AsString())