import pymel.core as pm

lipCtrlGrps = ['upperLip3Attach_L', 'upperLip3Attach_R', 'lowerLip3Attach_L', 'lowerLip3Attach_R', 'upperLip5Attach_R',
               'lowerLip5Attach_R', 'upperLip5Attach_L', 'lowerLip5Attach_L', 'Lip6Attach_L', 'Lip6Attach_R',
               'lowerLip0Attach_M', 'upperLip0Attach_M']
deleteObjArray = ['rig_group', 'FaceGroup', 'Head_M', 'Main']
# create groups.
lipJointOffsetGrp = pm.createNode('transform', n='JointOffsetLips_M')
lipControllersGrp = pm.createNode('transform', n='Lip_Controllers')

pm.delete(pm.parentConstraint('faceHeadJoint', lipJointOffsetGrp))
pm.parent('Lips_M', lipJointOffsetGrp)
pm.parent('LipRegion', 'FKOffsetLips_M', 'LipSetup', lipCtrlGrps, w=True)
pm.parent(lipCtrlGrps, lipControllersGrp)

curvesFromMeshEdgeArray = []
for each in lipCtrlGrps:
    allHist = pm.listHistory(each, pdo=True)
    for hist in allHist:
        if hist.nodeType() == 'pointOnCurveInfo':
            crvFrmMshEdg = hist.inputCurve.connections()[0].create.connections()[0]
            curvesFromMeshEdgeArray.append(crvFrmMshEdg)
