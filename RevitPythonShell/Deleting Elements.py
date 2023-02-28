"""
Python for Revit - Building Custom Tools

Lecture 18 - Deleting Elements

"""

#import the Revit DB and UI namespaces
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

#create filtered element collector to get all the instances of sheets
col_sheets = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets).WhereElementIsNotElementType().ToElements()

#create and start a transaction
t = Transaction(doc)
t.Start('Delete sheets')

#iterate through the sheets in the model
for sheet in col_sheets:
    #if the sheet number does not equal 'XX' (the model splash screen)...
	if sheet.SheetNumber != 'XX':
        #...delete all the views on that sheet...
		for view in sheet.GetAllPlacedViews():
			doc.Delete(view)
        #...then delete the sheet    
		doc.Delete(sheet.Id)

#commit the transaction to the model		
t.Commit()