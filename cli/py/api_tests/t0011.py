import FreeCAD
import Part

def main():
    # Create a new document
    doc = FreeCAD.newDocument()

    # Create a simple box
    box = doc.addObject("Part::Box", "MyBox")
    box.Length = '100 mm'
    box.Width = '50 mm'
    box.Height = '25 mm'
    #box.ViewObject.Visibility = True  # Ensure the object is visible
    doc.recompute()

    # Export the box to a STEP file
    step_path = "your_box3.step"
    box.Shape.exportStep(step_path)
    print(f"STEP file saved at: {step_path}")

    # Save the FreeCAD document
    fcstd_path = "your_file3.FCStd"
    doc.saveAs(fcstd_path)
    print(f"FreeCAD document saved at: {fcstd_path}")

    # Close the document
    FreeCAD.closeDocument(doc.Name)

if __name__ == "__main__":
    main()
