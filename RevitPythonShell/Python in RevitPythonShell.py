"""
Python for Revit - Building Custom Tools

Lecture 7 - Python in RevitPythonShell

"""

#create a list containing string objects
room_names = ['Office 1', 'Store', 'Office 2', 'Corridor', 'Print Room']

#print the list
print(room_names)

#iterate through all the objects in the list and print each object (room)
for room in room_names:
	print(room)
	
#iterate through the list and only print the objects that contain the string 'Office'    
for room in room_names:
	if 'Office' in room:
		print(room)