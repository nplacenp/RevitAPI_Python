"""
Python for Revit - Building Custom Tools

Lecture 20 - Total Area of Wall Type

"""

#import the Revit DB and UI namespaces
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
#import SelectFromList from pyrevit package
from pyrevit.forms import SelectFromList

#get current Autodesk Revit project that can interface and interact with settings and operations in the UI
uidoc = __revit__.ActiveUIDocument
#get current Revit database document from the active UI document
doc = __revit__.ActiveUIDocument.Document

#create a filtered element collector containing all wall instance objects
col_wall_instances = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType()

#create a filtered element collector containing all wall type objects
col_wall_types = FilteredElementCollector(doc).OfClass(WallType)

#create list of type names from the type objects using list comprehension, using BuiltInParameter
type_names = [type.get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString() for type in col_wall_types]

#sort the type names alphabetically for improved user readability
type_names.sort()

#use the SelectFromList to allow the user to select a type name
selected_type = SelectFromList.show(type_names, button_name = 'Select Wall Type')

#create placeholder variable for the total area of the chosen wall type
total_area = 0

#for each wall in the instance object filtered element collector
for wall in col_wall_instances:
    #if the wall type name of the instance matches the user defined type name
	if selected_type == wall.WallType.get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString():
        #add the area of that wall to the total_area variable
		total_area = total_area + wall.get_Parameter(BuiltInParameter.HOST_AREA_COMPUTED).AsDouble()

#convert from internal Revit units to a defined unit type		
meters = UnitUtils.ConvertFromInternalUnits(total_area, UnitTypeId.SquareMeters)

#print a string containing the total_area value for the user defined wall type
print('The total area of wall type {x} is {y} square meters'.format(x = selected_type, y = round(meters, 1)))