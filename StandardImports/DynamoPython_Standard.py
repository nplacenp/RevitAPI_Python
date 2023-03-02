#Dynamo Python Standard Imports:
import sys
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')


clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

from  Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

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

#whatever = List[DB.whatevertype]()
#always have to do whatever.Add(whatevertoadd)

__________________________________________________________________________________

doc = DocumentManager.Instance.CurrentDBDocument
active_view = doc.ActiveView

#unwrapping
something = UnwrapElement(IN[0])

#converting back to dynamo (directShape)
wrappedElement = familyInstance.ToDSType(False)

quickFilter = ElementCategoryFilter(BuiltInCategory.OST_Stairs) #as an example

new_col = FilteredElementCollector(doc).WherePasses(quickFilter).WhereElementIsNotElementType().ToElementIds()

__________________________________________________________________________________

TransactionManager.Instance.EnsureInTransaction(doc)

for whatever in whatever:
    newWhatevers = Architecture.Something.Create(doc, etc)

TransactionManager.Instance.TransactionTaskDone()

Out = output or whatever