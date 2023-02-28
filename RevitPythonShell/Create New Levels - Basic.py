"""
Python for Revit - Building Custom Tools

Lecture 23 - Create New Levels - Basic

"""

#import the Revit DB and UI namespaces
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import *

#get current Autodesk Revit project that can interface and interact with settings and operations in the UI
uidoc = __revit__.ActiveUIDocument
#get current Revit database document from the active UI document
doc = __revit__.ActiveUIDocument.Document

#create a transaction in the current document
t = Transaction(doc)
#start the transaction, giving the transaction a name / text description
t.Start('Create Level')

#create a new level in the current document with a defined elevation in feet
new_level = Level.Create(doc, 27)
#set the name of the new Level once it has been created
new_level.Name = 'Level 03'

#commit the transaction to the Revit document
t.Commit()