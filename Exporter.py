import maya.cmds as cmds
import maya.OpenMaya as OpenMaya

sList = OpenMaya.MSelectionList()
sList.add("pPlane4")

mObj = OpenMaya.MObject()
mDagPath = OpenMaya.MDagPath()