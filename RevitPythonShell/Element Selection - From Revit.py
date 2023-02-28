"""
Python for Revit - Building Custom Tools

Lecture 14 - Element Selection - From Revit

"""

#import the Revit DB and UI namespaces
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

#get current Autodesk Revit project that can interface and interact with settings and operations in the UI
uidoc = __revit__.ActiveUIDocument
#get current Revit database document from the active UI document
doc = __revit__.ActiveUIDocument.Document

#get the current selection element
selection = uidoc.Selection

#print the selection to ensure the object exists
print(selection)

#create placeholder empty list
elements = []

#add the elements in the selection using the GetElement() method to the new elements list
for id in selection.GetElementIds():
    elements.append(doc.GetElement(id))
    
#iterate through the new list and print each object
for element in elements:
    print(elements)
    
#iterate through the new list and print the category of each object
for element in elements:
    print(element.Category.Name)
 
#if the element is a wall, print the value of the IsStackedWall property
for element in elements:
    if element.Category.Name == 'Walls':
    	print(element.IsStackedWall)