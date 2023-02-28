
# Load the Python Standard and DesignScript Libraries
import sys
sys.path.append(r"E:\PDPS\Udemy\83_Python Interphase")
from Forms import *
import clr

# The inputs to this node will be stored as a list in the IN variables.
ELEMENTS = IN[0]
LEVELS = IN[1]
ULEV = list(set(LEVELS))
ULEV.sort()

Selection = SingleComboBoxForm(ULEV,["Level Selector","POSIBLE LEVELS"])
RESULT = []
for a,b in zip(LEVELS,ELEMENTS):
	if a==Selection:
		RESULT.append(b) 	    
	   
# Place your code below this line

# Assign your output to the OUT variable.
OUT = RESULT 