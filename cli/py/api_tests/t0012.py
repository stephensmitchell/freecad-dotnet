import FreeCAD
import Part

def main():
    # Create a new document
    doc = FreeCAD.newDocument()

    # Create a part container
    myPart = doc.addObject("App::Part", "MyPart")

    # Create a simple box inside the part container
    box = doc.addObject("Part::Box", "MyBox")
    box.Length = '100 mm'
    box.Width = '50 mm'
    box.Height = '25 mm'
    
    # Move the box into the part
    myPart.addObject(box)
    
    # Set visibility
    #box.ViewObject.Visibility = True  # Ensure the box is visible
    #myPart.ViewObject.Visibility = True  # Ensure the part is visible

    doc.recompute()

    # Export the box to a STEP file
    step_path = "your_box5.step"
    #box.exportStep(step_path)  # Export the whole part containing the box
    print(f"STEP file saved at: {step_path}")

    # Save the FreeCAD document
    fcstd_path = "your_file5.FCStd"
    doc.saveAs(fcstd_path)
    print(f"FreeCAD document saved at: {fcstd_path}")

    # Close the document
    FreeCAD.closeDocument(doc.Name)

if __name__ == "__main__":
    main()
