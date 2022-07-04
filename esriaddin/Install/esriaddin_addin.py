import arcpy
import pythonaddins

class RemoveLayersTOC(object):
    """Implementation for esriaddin_addin.btn_1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        mxd = arcpy.mapping.MapDocument("CURRENT")
        for df in arcpy.mapping.ListDataFrames(mxd):
            for lyr in arcpy.mapping.ListLayers(mxd, "", df):
                arcpy.mapping.RemoveLayer(df, lyr)