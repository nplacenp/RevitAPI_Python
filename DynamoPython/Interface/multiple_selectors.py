
# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference("RevitAPIUI")
from  Autodesk.Revit.UI import *

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
uidoc=DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
view = uidoc.ActiveView
sel1 = uidoc.Selection
obj1 = Selection.ObjectType.Element
msg1 = "Select a Column to Start Performing, and press Esc to end Function"
TaskDialog.Show("The Selector", msg1)
flag = True
out1=[]
TransactionManager.Instance.EnsureInTransaction(doc)
while flag:
	try:
		el1= doc.GetElement(sel1.PickObject(obj1,msg1).ElementId)
		out1.append(el1)
	except:
		flag=False 
TransactionManager.Instance.TransactionTaskDone()

# Assign your output to the OUT variable.
OUT = out1