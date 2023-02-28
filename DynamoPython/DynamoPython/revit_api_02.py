
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

output = []
symbol = UnwrapElement(IN[0])
# Place your code below this line
TransactionManager.Instance.EnsureInTransaction(doc)

for i in range(0, 50, 10):

	familyInstance = doc.Create.NewFamilyInstance(DB.XYZ(i,0,0), symbol, DB.Structure.StructuralType.NonStructural)
	output.append(familyInstance)
TransactionManager.Instance.TransactionTaskDone()

# Assign your output to the OUT variable.
OUT = output