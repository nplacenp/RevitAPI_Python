#Dynamo Python Standard Imports:

import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

import Autodesk.Revit.DB as DB

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference('System')
from System.Collections.Generic import List
#List creating
whatever = List[DB.whatevertype]()
#always have to do whatever.Add(whatevertoadd)

__________________________________________________________________________________

doc = DocumentManager.Instance.CurrenDBDocument

#unwrapping
something = UnwrapElement(IN[0])

#converting back to dynamo (directShape)
wrappedElement = familyInstance.ToDSType(False)

quickFilter = DB.ElementCategoryFilter(DB.BuiltInCategory.OST_Stairs) #as an example

DB.FilteredElementCollector(doc).WherePasses(quickfiltername).WhereElementIsNotElementType().ToElementIds()

__________________________________________________________________________________

TransactionManager.Instance.EnsureInTransaction(doc)

for whatever in whatever:
    newWhatevers = DB.Architecture.Something.Create(doc, etc)

TransactionManager.Instance.TransactionTaskDone()

Out = output or whatever