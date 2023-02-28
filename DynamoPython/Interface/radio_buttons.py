
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

NAMES = ["First Selection", "Second Selection", "Third Selection"]
MULLISTS = [ULEV,ULEV,ULEV]
"""Selection = multipleComboBoxForm(NAMES,MULLISTS,"SELECTOR")

#Selection = SingleComboBoxForm(ULEV,["Level Selector","POSIBLE LEVELS"])
RESULT = []
for c in Selection:
	INDRESULT=[]
	for a,b in zip(LEVELS,ELEMENTS):
		if a==c:
			INDRESULT.append(b)
	RESULT.append(INDRESULT)			
"""	   
# Place your code below this line
Selection2 = SingleRadioButtonsForm(ULEV,"Radio Buttons")
RESULTS2=[] 
for a,b in zip(LEVELS,ELEMENTS): 
		if a==Selection2: 
			RESULTS2.append(b)
	 
# Assign your output to the OUT variable.
OUT = Selection2,RESULTS2 