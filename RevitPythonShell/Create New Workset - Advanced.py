"""
Python for Revit - Building Custom Tools

Lecture 22 - Create New Workset - Advanced

"""

#import the Revit DB and UI namespaces
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
#import the FlexForm and associated classes from RevitPythonWrapper
from rpw.ui.forms import (FlexForm, Label, ComboBox, TextBox, TextBox,
                           Separator, Button, CheckBox)

#get current Autodesk Revit project that can interface and interact with settings and operations in the UI
uidoc = __revit__.ActiveUIDocument
#get current Revit database document from the active UI document
doc = __revit__.ActiveUIDocument.Document

#create a filtered element collector containing all the user created workset objects in the model
col_worksets = FilteredWorksetCollector(doc).OfKind(WorksetKind.UserWorkset)

#create a list of workset names using list comprehension
workset_names = [workset.Name for workset in col_worksets]

#create the components or inputs that will be used in the FlexForm
components = [Label('Enter New Workset Name'), TextBox('workset_name', Text = 'New Workset'),
				CheckBox('visible_all', 'Visible In All Views', default = True), Button('Create Workset')]

#show the FlexForm to allow the user to select the inputs
form = FlexForm('Create New Workset', components)

#if the document is workshared / workshare enabled
if doc.IsWorkshared:
    #show the FlexForm
	form.show()
	
    #extract the values from the form results
	workset_name = form.values.get('workset_name')
	visibility = form.values.get('visible_all')
	
    #if the workset name that has been defined already exists in the model
	if workset_name in workset_names:
        #show a TaskDialog with an appropriate warning
		message = TaskDialog
		message.Show('Error', 'This model already has a workset with this name')
    #if the workset name that has been defined does not exist in the model
	else:
        #if the form has been completed
		if len(form.values) != 0:
            #create a transaction in the current document
			t = Transaction(doc)
            #start the transaction, giving the transaction a name / text description
			t.Start('Create new workset')
			
            #create a new workset with the name defined by the results of the form
			new_workset = Workset.Create(doc, workset_name)
            #create a workset default visibility settings object in the current document
			visibility = WorksetDefaultVisibilitySettings.GetWorksetDefaultVisibilitySettings(doc)
			#set the default workset visibility of this new workset to the result of the form
            visibility.SetWorksetVisibility(new_workset.Id, visibility)
			
            #commit the transaction to the Revit document
			t.Commit()

#if the document is not workshared, show a TaskDialog stating this			
else:
	message = TaskDialog
	message.Show('Error', 'Please enable worksharing')

#close the RevitPythonShell output window
__window__.Close()