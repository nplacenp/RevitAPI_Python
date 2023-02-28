"""
Python for Revit - Building Custom Tools

Lecture 19 - Get Type Names and Family Names

"""

#import the Revit DB and UI namespaces
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

#get the currently selected element Ids
selection = uidoc.Selection.GetElementIds()

#iterate through each id in the selection...
for id in selection:
    #get the Revit object from that element Id
	element = doc.GetElement(id)
    #get the type Id from that instance object
	type_id = element.GetTypeId()
    #print the Category of the object
	print('Category - ' + element.Category.Name)
    #print the type name
	print('Type - ' + doc.GetElement(type_id).get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString())
    #print the family name
	print('Family - ' + doc.GetElement(type_id).get_Parameter(BuiltInParameter.SYMBOL_FAMILY_NAME_PARAM).AsString())
    #print separator string
	print('----')	

#create a filtered element collector of all the floor types in the model
col_wall_types = FilteredElementCollector(doc).OfClass(FloorType)

#create a list of types name using list comprehension
type_names = [x.get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString() for x in col_wall_types]
#create a list of family name using list comprehension
family_names = [x.get_Parameter(BuiltInParameter.SYMBOL_FAMILY_NAME_PARAM).AsString() for x in col_wall_types]

#print each type name
for type in type_names:
	print(type)
	
print('---')

#print each family name
for family in family_names:
	print(family)
	
