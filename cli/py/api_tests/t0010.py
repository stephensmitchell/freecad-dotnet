import FreeCAD as App
import Part

def main():
    # Create a new document
    doc = FreeCAD.newDocument()
    
    # Create a simple box
    box = doc.addObject("Part::Box", "MyBox")
    box.Length = '100 mm'
    box.Width = '50 mm'
    box.Height = '25 mm'
    doc.recompute()

    # Export the box to a STEP file
    step_path = "your_box4.step"
    box.Shape.exportStep(step_path)
    print(f"STEP file saved at: {step_path}")

    # Save the FreeCAD document
    fcstd_path = "your_file4.FCStd"
    doc.recompute()
    doc.saveAs(fcstd_path)
    doc.recompute()
    print(f"FreeCAD document saved at: {fcstd_path}")
    App.ActiveDocument.recompute()
    # Close the document
    #doc.close()

if __name__ == "__main__":
    main()
