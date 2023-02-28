#RevitPythonShell Standard Imports:

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

#pyrevit libraries
from rpw.ui.forms import (FlexForm, Label, ComboBox, TextBox, Separator, Button, CheckBox)

#create flexform components

components = [Label('Number of Levels'), TextBox('number', Text = '1'), Label('Specing Between Levels'), TextBox('spacing', Text = '3150'), Button('Create Levels')]

form = FlexForm('Create Levels', components)

form.show()

#getting values from the form
spacing = int(form.values.get('spacing'))
number_levels = int(form.values.get('number'))

uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document

active_view = uidoc.ActiveView

#selectingStuffinactiveview

selection  =FilteredElementCollector(doc, active_view).OfCategory(whatevercategory).WhereElementIsNotElementType().ToElementIds()#just an example


element.LookupParameter('Whatever').AsString()

element.get_Parameter(BuiltInParameter.ROOM_NAME).AsString() #example

t = Transaction(doc)

t.Start("whatever you want to call it")

#do stuff

t.Commit()

#closes RevitPythonShell output window
__window__.close()