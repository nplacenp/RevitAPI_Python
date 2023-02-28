
# Load the Python Standard and DesignScript Libraries
import sys
import clr

sys.path.append(r"G:\##Revit Experiments\___Courses\Python Nodes\modules")

import module1 as ML
# The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN


sph1 = ML.sphere()
number = ML.outputNumber()
# Assign your output to the OUT variable.
OUT = sys.builtin_module_names