import freecad
import FreeCAD as App
from FreeCAD import Part as Prt
import sys
def test_freecad():
    # Create a new document
    doc = App.newDocument()

    # Add a box to the document
    box = doc.addObject("Part::Box", "MyBox")
    box.Length = 10  # Set the length of the box to 10 units
    box.Width = 10   # Set the width of the box to 10 units
    box.Height = 10  # Set the height of the box to 10 units

    # Recompute the document to apply changes
    doc.recompute()

    # Check some properties of the box
    print("Box Length:", box.Length)
    print("Box Width:", box.Width)
    print("Box Height:", box.Height)

    # Close the document without saving
    App.closeDocument(doc.Name)
    for i in sys.path:
        print(i)

# Run the test
test_freecad()