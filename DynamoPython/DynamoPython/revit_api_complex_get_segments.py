
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

boundaryOptions = DB.SpatialElementBoundaryOptions()
output = []
searchWord = IN[3]
desiredRooms = []

TransactionManager.Instance.EnsureInTransaction(doc)
for room in rooms:
	roomName = DB.Element.Name.GetValue(room)
	if searchWord.lower() in roomName.lower():
        desiredRooms.append(room)
        outerBoundaries = room.GetBoundarySegments(boundaryOptions)[0]
        for bSegment in outerBoundaries:
            curve = bSegment.GetCurve().Convert()
            output.append(curve)

TransactionManager.Instance.TransactionTaskDone()

# Assign your output to the OUT variable.
OUT = output