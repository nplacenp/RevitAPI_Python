"""
Python for Revit - Building Custom Tools

Lecture 25 - Isolate all Groups with Excluded Elements

"""

#import the Revit DB and UI namespaces and the List class from .NET System.Collections.Generic
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from System.Collections.Generic import List

#get current Autodesk Revit project that can interface and interact with settings and operations in the UI
uidoc = __revit__.ActiveUIDocument
#get current Revit database document from the active UI document
doc = __revit__.ActiveUIDocument.Document
#get the current active view
active_view = uidoc.ActiveView

#create a filtered element collector containing all the model groups visible in the active view
col_groups = FilteredElementCollector(doc, active_view.Id).OfCategory(BuiltInCategory.OST_IOSModelGroups).WhereElementIsNotElementType()

#create a placeholder list in which to add groups with excluded elements
excluded_groups = []

#iterate through each group in the collector and add to the placeholder list, any groups with excluded elements
for group in col_groups:
	if 'excluded)' in group.Name:
		excluded_groups.append(group)

#create a placeholder list in which to add all the elements that are within each group with excluded elements		
elements = []

#iterate through each group with excluded elements
for group in excluded_groups:
	#iterate through all the Ids of all the elements inside the groups
    for element in group.GetMemberIds():
		#add these elements to the placeholder groups
        elements.append(element)

#create an IList / ICollection to input into the IsolateElementsTemporary method
isolate_collection = List[ElementId](elements)

#create a transaction in the current document
t = Transaction(doc)
#start the transaction, giving the transaction a name / text description
t.Start('Isolate Groups with Excluded Elements')

#in the active view, isolate the elements in the groups with excluded members
#Note you cannnot isolate the groups themselves, you must isolate the elements within the groups
active_view.IsolateElementsTemporary(isolate_collection)

#commit the transaction to the Revit document
t.Commit()

#close the RevitPythonShell output window
__window__.Close()