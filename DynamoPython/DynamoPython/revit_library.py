
# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.AddReference('RevitNodes')
import Revit
# The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN

# Place your code below this line
level = IN[0]
wallType = IN[1]
length = IN[2]
pt1 = Point.ByCoordinates(0,0,0)
pt2 = Point.ByCoordinates(length,0,0)

line = Line.ByStartPointEndPoint(pt1,pt2)


# Assign your output to the OUT variable.
OUT = Revit.Elements.Wall.ByCurveAndHeight(line,2000,level,wallType)