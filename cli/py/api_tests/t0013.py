import FreeCADGui as Gui
from pivy import coin

Gui.setupWithoutGUI()
doc = App.newDocument()
obj = doc.addObject("Part::Box","Box")
doc.recompute()
view = Gui.subgraphFromObject(obj)

doc.saveAs("your_file6.FCStd")