
# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitAPI')
#from Autodesk.Revit.DB import *
import Autodesk.Revit.DB as DB

clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN
doc = DocumentManager.Instance.CurrentDBDocument
view = UnwrapElement(IN[0])
filterStairPathTypes = DB.ElementCategoryFilter(DB.BuiltInCategory.OST_StairsPaths)
filterStairs = DB.ElementCategoryFilter(DB.BuiltInCategory.OST_Stairs)
stairtPathType = DB.FilteredElementCollector(doc).WherePasses(filterStairPathTypes).WhereElementIsElementType().FirstElementId()
stairs = DB.FilteredElementCollector(doc).WherePasses(filterStairs).WhereElementIsNotElementType().ToElementIds()

output = []
TransactionManager.Instance.EnsureInTransaction(doc)
for stairId in stairs:
	try:
		newstairpath = DB.Architecture.StairsPath.Create(doc, DB.LinkElementId(stairId), stairtPathType, view.Id)
		output.append(newstairpath)
	except Exception, textV:
		output.append(textV)
TransactionManager.Instance.TransactionTaskDone()
# Assign your output to the OUT variable.
OUT = output