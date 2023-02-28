"""
Python for Revit - Building Custom Tools

Lecture 8 - Accessing Revit API

"""

#import the Revit DB and UI namespaces
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

#get current Autodesk Revit project that can interface and interact with settings and operations in the UI
uidoc = __revit__.ActiveUIDocument
#get current Revit database document from the active UI document
doc = __revit__.ActiveUIDocument.Document

#print the uidoc and doc variables to see the objects
print(uidoc)
print(doc)