
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

output = []
symbol = UnwrapElement(IN[0])
pointList = IN[1]
# Place your code below this line
TransactionManager.Instance.EnsureInTransaction(doc)
if not symbol.IsActive:
	symbol.Activate()
for i in pointList:
	#point = DB.XYZ(i,i,0).ToPoint()
	xyz = i.ToXyz()
	familyInstance = doc.Create.NewFamilyInstance(xyz, symbol, DB.Structure.StructuralType.NonStructural)
	#wrap element to Dynamo type:
	wrappedElement = familyInstance.ToDSType(False)
	output.append(wrappedElement)
TransactionManager.Instance.TransactionTaskDone()

# Assign your output to the OUT variable.
OUT = output