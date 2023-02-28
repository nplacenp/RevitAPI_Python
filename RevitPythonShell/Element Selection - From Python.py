"""
Python for Revit - Building Custom Tools

Lecture 14 - Element Section - From RevitPythonShell

"""

#import the Revit DB and UI namespaces
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

#get current Autodesk Revit project that can interface and interact with settings and operations in the UI
uidoc = __revit__.ActiveUIDocument
#get current Revit database document from the active UI document
doc = __revit__.ActiveUIDocument.Document

#get the current active view from Revit
active_view = uidoc.ActiveView

#create a filtered element collector from the current view of the Room Tag category, excluding types
col_selection = FilteredElementCollector(doc, active_view.Id).OfCategory(BuiltInCategory.OST_RoomTags).WhereElementIsNotElementType().ToElementIds()

#iterate through the filtered element collector and print the objects to ensure correct selection
for x in col_selection:
	print(x)

#create a seletion element from the uidoc and select the elements within the filtered element collector
#these will then be the selected elements inside Revit once RevitPythonShell is closed	
selection = uidoc.Selection.SetElementIds(col_selection)