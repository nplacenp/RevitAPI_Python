
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
	
values = [10,15,20]

def ManySpheres(vals):
	doubles = [i*2 for i in vals]
	radii = [i*0.5 for i in vals]
	spheres = map(sphere,vals,doubles,radii)
	return spheres
	
OUT = ManySpheres(values)