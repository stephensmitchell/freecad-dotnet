import FreeCAD as App
import Part, math
import sys

def save_step(model, filename):
    model.exportStep(filename)
    print(f"Model saved as STEP file: {filename}")


def save_fcstd(model, filename):
    doc = App.newDocument()
    obj = doc.addObject("Part::Feature", "MyModel")
    obj.Shape = model
    doc.saveAs(filename)
    #doc.close()
    print(f"Model saved as FCStd file: {filename}")


def save_iges(model, filename):
    model.exportIges(filename)
    print(f"Model saved as IGES file: {filename}")

def save_obj(model, filename):
    model.exportObj(filename)
    print(f"Model saved as OBJ file: {filename}")

def save_dxf(model, filename):
    import importDXF
    importDXF.export(model, filename)
    print(f"Model saved as DXF file: {filename}")

import FreeCAD as App

def save_obj2(model, filename):
    doc = App.newDocument()
    obj = doc.addObject("Part::Feature", "MyModel")
    obj.Shape = model
    # The export method requires a list of tuples, each with the object label and filename
    doc.export([tuple([obj.Label, filename])], format='OBJ')
    print(f"Model saved as OBJ file: {filename}")
    doc.close()


def makeBottleTut(myWidth = 50.0, myHeight = 70.0, myThickness = 30.0):
    aPnt1=App.Vector(-myWidth / 2., 0, 0)
    aPnt2=App.Vector(-myWidth / 2., -myThickness / 4., 0)
    aPnt3=App.Vector(0, -myThickness / 2., 0)
    aPnt4=App.Vector(myWidth / 2., -myThickness / 4., 0)
    aPnt5=App.Vector(myWidth / 2., 0, 0)

    aArcOfCircle = Part.Arc(aPnt2, aPnt3, aPnt4)
    aSegment1=Part.LineSegment(aPnt1, aPnt2)
    aSegment2=Part.LineSegment(aPnt4, aPnt5)

    aEdge1=aSegment1.toShape()
    aEdge2=aArcOfCircle.toShape()
    aEdge3=aSegment2.toShape()
    aWire=Part.Wire([aEdge1, aEdge2, aEdge3])

    aTrsf=App.Matrix()
    aTrsf.rotateZ(math.pi)  # rotate around the z-axis

    aMirroredWire=aWire.copy()
    aMirroredWire.transformShape(aTrsf)
    myWireProfile=Part.Wire([aWire, aMirroredWire])

    myFaceProfile=Part.Face(myWireProfile)
    aPrismVec=App.Vector(0, 0, myHeight)
    myBody=myFaceProfile.extrude(aPrismVec)

    myBody=myBody.makeFillet(myThickness / 12.0, myBody.Edges)

    neckLocation=App.Vector(0, 0, myHeight)
    neckNormal=App.Vector(0, 0, 1)

    myNeckRadius = myThickness / 4.
    myNeckHeight = myHeight / 20.
    myNeck = Part.makeCylinder(myNeckRadius, myNeckHeight, neckLocation, neckNormal)
    myBody = myBody.fuse(myNeck)

    return myBody

if __name__ == "__main__":
    el = makeBottleTut()
    output_file = "output_file_path2.stl"  # Define the output file path
    el.exportStl(output_file)
    save_step(el, "bottle_model.step")
    save_fcstd(el, "bottle_model.fcstd")
    save_iges(el, "bottle_model.iges")
    #save_obj2(el, "bottle_model.obj")
    #save_dxf(el, "bottle_model.dxf")
    print(f"Model exported to {output_file}")



