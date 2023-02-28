"""
Python for Revit - Building Custom Tools

Lecture 15 - Transactions

"""

#import the Revit DB and UI namespaces
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

#get current Autodesk Revit project that can interface and interact with settings and operations in the UI
uidoc = __revit__.ActiveUIDocument
#get current Revit database document from the active UI document
doc = __revit__.ActiveUIDocument.Document

#create a filtered element collector containing room elements
col_rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType()

#create a transaction in the current document
t = Transaction(doc)
#start the transaction, giving the transaction a name / text description
t.Start('Apply Level code to room parameter')

#iterate through the rooms in the filtered element collector and set the value for the parameter MT_RoomLevel to be the Level number
for room in col_rooms:
	room.LookupParameter('MT_RoomLevel').Set(room.Level.Name[6:])

#commit the transaction to the Revit document
t.Commit()