
# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

pointList = IN[0]

output = []
for ptLst1 in pointList:
	output1 = []
	for ptLst2 in ptLst1:
		output2 =[]
		for pt in ptLst2:
			try:
				myPoint = Point.ByCoordinates(pt.X,pt.Y,pt.Z + 10)
				output2.append(myPoint)
			except Exception, ex: 
				output2.append(ex)
		output1.append(output2)
	output.append(output1)
# Assign your output to the OUT variable.
OUT = output