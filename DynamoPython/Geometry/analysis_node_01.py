
# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
Geometry = IN[0]
Range = IN[1]
Geo1=[]
# Place your code below this line
for a in Geometry:
	if isinstance(a,list):
		for b in a:
			Geo1.append(b)
	else:
		Geo1.append(a)
GPts = []
for a in Geo1:
	G1Pts = []
	for b in Range:
		pt1=a.PointAtParameter(b)		
		G1Pts.append(pt1.Add(Vector.ByCoordinates(0,0,b*4)))
	GPts.append(G1Pts)
GtPts = map(list,zip(*GPts))
Curves=[]
for a in GtPts:
	curve=NurbsCurve.ByPoints(a)
	Curves.append(curve)
# Assign your output to the OUT variable.
OUT = Curves