
# Load the Python Standard and DesignScript Libraries
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN

def outputNumber():
	return 42

def sphere(x=0,y=0,radius = 10):
	pt = Point.ByCoordinates(x,y,0)
	return Sphere.ByCenterPointRadius(pt, radius)
	
values = IN[0]

def ManySpheres(vals):
	if not isinstance(vals, list):
		vals = [vals]
		
	doubles = [i*2 for i in vals]
	radii = [i*0.5 for i in vals]
	
	spheres1 = [sphere(radius = rad, x=val) for rad,val in zip(radii,doubles)]
	spheres2 = [sphere(radius = rad, y=val) for rad,val in zip(radii,doubles)]	
	return spheres1,spheres2
	
OUT = ManySpheres(values)