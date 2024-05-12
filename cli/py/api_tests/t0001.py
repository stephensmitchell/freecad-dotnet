import clr
clr.AddReference("System")
from System import *
from System.Collections import ArrayList
# Create an instance of ArrayList
list = ArrayList()
list.Add("Apple")
list.Add("Banana")
list.Add("Orange")
# Access elements of the list
for item in list:
    print(item)
