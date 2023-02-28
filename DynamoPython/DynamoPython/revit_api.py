
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
# The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN
doc = DocumentManager.Instance.CurrentDBDocument

# Place your code below this line
stairtPathTypes = DB.FilteredElementCollector(doc).OfCategory(DB.BuiltInCategory.OST_StairsPaths).ToElements()
# Assign your output to the OUT variable.
OUT = stairtPathTypes