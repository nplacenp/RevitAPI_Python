import sys
sys.path.append(r"F:\Python")
from Functions import *

import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
# The inputs to this node will be stored as a list in the IN variables.

Geo1 = flatten(IN[0])
Curves = CurvesfromGeometryLines(Geo1,IN[1])

OUT = Surface.ByLoft(Curves)