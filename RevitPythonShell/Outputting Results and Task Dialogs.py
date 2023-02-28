"""
Python for Revit - Building Custom Tools

Lecture 12 - Outputting Results and Task Dialogs

"""

#import the Revit DB and UI namespaces
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

#get current Autodesk Revit project that can interface and interact with settings and operations in the UI
uidoc = __revit__.ActiveUIDocument
#get current Revit database document from the active UI document
doc = __revit__.ActiveUIDocument.Document

#create a filtered element collector object from the current document (required) where the category is Rooms and element is not element type
col_rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType()

#create a 'placeholder' starter variable for the total area which will be used later
total_area = 0

#add the area for each room to the total area using the Area property (room.Area)
for room in col_rooms:
	total_area = total_area + room.Area
	
#print the total area to check
print(total_area)

#construct a TaskDialog element
message = TaskDialog

#generate the text to be displayed in the TaskDialog using string formatting and line breaks
text = 'The total area of rooms in the building is \n\n{} square feet'.format(round(total_area, 1))

#show the TaskDialog with a title and the defined text
message.Show('Total Area Calculation', text)