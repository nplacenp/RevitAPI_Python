"""
Python for Revit - Building Custom Tools

Lecture 22 - Create New Workset - Basic

"""

#import the Revit DB and UI namespaces
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

#get current Autodesk Revit project that can interface and interact with settings and operations in the UI
uidoc = __revit__.ActiveUIDocument
#get current Revit database document from the active UI document
doc = __revit__.ActiveUIDocument.Document

#if the current Revit document is workshared / workshare enabled
if doc.IsWorkshared:
    #create a transaction in the current document
	t = Transaction(doc)
    #start the transaction, giving the transaction a name / text description
	t.Start('Create new workset')
    
	#create a new workset with a defined name
	new_workset = Workset.Create(doc, 'RevitLink_Structure')
    #create a workset default visibility settings object in the current document
	visibility = WorksetDefaultVisibilitySettings.GetWorksetDefaultVisibility(doc)
    #set the default workset visibility of this new workset to True (visible)
	visibility.SetWorksetVisibility(new_workset.Id, True)
	
    #commit the transaction to the Revit document
	t.Commit()