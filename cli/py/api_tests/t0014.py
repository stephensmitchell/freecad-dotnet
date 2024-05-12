import FreeCAD
import Part
import Sketcher

# Initialize a new document
doc = FreeCAD.newDocument()

# Create a new sketch
sketch = doc.addObject('Sketcher::SketchObject', 'RectangleSketch')

# Add a rectangle to the sketch
sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(0,0,0), FreeCAD.Vector(10,0,0)), False)
sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(10,0,0), FreeCAD.Vector(10,10,0)), False)
sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(10,10,0), FreeCAD.Vector(0,10,0)), False)
sketch.addGeometry(Part.LineSegment(FreeCAD.Vector(0,10,0), FreeCAD.Vector(0,0,0)), False)

# Create a pad (extrusion) from the sketch
pad = doc.addObject("PartDesign::Pad", "Pad")
pad.Profile = sketch
pad.Length = 10.0  # Length of the extrusion

# Recompute the document to apply changes
doc.recompute()

# Save the document
file_path = "freecad_project0.fcstd"  # Update with your desired file path
doc.saveAs(file_path)

# Optionally close the document if you're done
FreeCAD.closeDocument(doc.Name)

print("Saved FreeCAD project to", file_path)
