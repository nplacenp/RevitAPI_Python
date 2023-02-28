
# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
x_Coordinate = IN[0]
y_Coordinate = IN[1]
z_Coordinate = IN[2]
# Place your code below this line
xOutput = []
for val1 in x_Coordinate:
	yOutput = []
	for val2 in y_Coordinate:
		zOutput = []
		for val3 in z_Coordinate:
			myPoint = Point.ByCoordinates(val1,val2,val3)
			zOutput.append(myPoint)
		yOutput.append(zOutput)
	xOutput.append(yOutput)

# Assign your output to the OUT variable.
OUT = xOutput