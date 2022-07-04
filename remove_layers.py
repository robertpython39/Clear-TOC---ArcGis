from arcpy import env
import arcpy

mxd = arcpy.mapping.MapDocument("CURRENT")
for df in arcpy.mapping.ListDataFrames(mxd):
    for lyr in arcpy.mapping.ListLayers(mxd, "", df):
        arcpy.mapping.RemoveLayer(df, lyr)

