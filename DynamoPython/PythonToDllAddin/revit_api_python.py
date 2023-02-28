
# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference("RevitAPIUI")
from Autodesk.Revit.UI import * 
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

def LinePointAtParameters(LN,PARAMS):
	POINTS = []
	for a in PARAMS:
		POINT = LN.GetEndPoint(0).Add(LN.Direction.Normalize().Multiply(a*LN.Length))
		POINTS.append(POINT)
	return POINTS

def verticalline(pt):
	vel = Line.CreateBound(pt,pt.Add(XYZ(0,0,1)))
	return vel


doc = DocumentManager.Instance.CurrentDBDocument
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
view = uidoc.ActiveView

sel1 = uidoc.Selection
obt1 = Selection.ObjectType.Element
msg1 = "Select Line on Model"
TaskDialog.Show("Select Line on Model",msg1)

TransactionManager.Instance.EnsureInTransaction(doc)
el1 = doc.GetElement(sel1.PickObject(obt1,msg1).ElementId)
TransactionManager.Instance.TransactionTaskDone()

LINE = el1.GeometryCurve
PAR = [0,0.5,1]
POINTS = LinePointAtParameters(LINE,PAR)
ANGLE = LINE.Direction.AngleTo(XYZ(1,0,0))

FamCollector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_GenericModel).OfClass(FamilySymbol)
famtypeitr= FamCollector.GetElementIdIterator()
famtypeitr.Reset()
TYPE = []
for item in famtypeitr:
	famobj=doc.GetElement(item)
	if famobj.get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString()=="01_Block":
		TYPE.append(famobj)
FAMILIES=[]
TransactionManager.Instance.EnsureInTransaction(doc)
for a in range(len(POINTS)):
	fam1 = doc.Create.NewFamilyInstance(POINTS[a],TYPE[0],Structure.StructuralType.NonStructural)
	ElementTransformUtils.RotateElement(doc,fam1.Id,verticalline(POINTS[a]),ANGLE)
	FAMILIES.append(fam1)

TransactionManager.Instance.TransactionTaskDone()

# Assign your output to the OUT variable.
OUT = FAMILIES