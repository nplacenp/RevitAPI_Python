
# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitAPI')
#from Autodesk.Revit.DB import *
import Autodesk.Revit.DB as DB

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN
doc = DocumentManager.Instance.CurrentDBDocument
roomFilter = DB.ElementCategoryFilter(DB.BuiltInCategory.OST_Rooms)
rooms = DB.FilteredElementCollector(doc).WherePasses(roomFilter).WhereElementIsNotElementType().ToElements()

floors = DB.FilteredElementCollector(doc).OfClass(DB.Floor).ToElements()
sType = DB.Structure.StructuralType.NonStructural

walls = []

TransactionManager.Instance.EnsureInTransaction(doc)

TransactionManager.Instance.TransactionTaskDone()

# Assign your output to the OUT variable.
OUT = walls