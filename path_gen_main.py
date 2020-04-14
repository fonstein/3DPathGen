import sys

import FreeCAD
import FreeCADGui

# Has to be added to the path for FreeCAD to find the scripts
sys.path.append("C:/Users/ingridon/OneDrive/Documents/PhD/3D Path Generation code/3DPathGen")

__title__ = "PathGeneration"
__author__ = "Ingrid Fjordheim Onstein"
__version__ = "0.1"
__doc__ = """Tool for generating paths for deburring based on edges in STEP CAD models"""

def main():
    FreeCAD.Console.PrintMessage("\n\n============== START ==============")
    selected = FreeCADGui.Selection.getSelectionEx()
    edge = selected[0].SubObjects

    FreeCAD.Console.PrintMessage("\n Selected object: " + str(edge))

    FreeCAD.Console.PrintMessage("\n\n============= FINISHED ============")

if __name__ == "__main__":
    main()
