import pymel.core as pm


def exportLipSetup():
    lipCtrlGrps = ['upperLip3Attach_L', 'upperLip3Attach_R', 'lowerLip3Attach_L', 'lowerLip3Attach_R',
                   'upperLip5Attach_R',
                   'lowerLip5Attach_R', 'upperLip5Attach_L', 'lowerLip5Attach_L', 'Lip6Attach_L', 'Lip6Attach_R',
                   'lowerLip0Attach_M', 'upperLip0Attach_M']
    deleteObjArray = ['rig_group', 'FaceGroup', 'Head_M', 'Main', 'faceLid', 'Jaw_M', 'FaceUpperRegion_M',
                      'FaceLowerRegion_M']
    # create groups.
    lipControllersGrp = pm.createNode('transform', n='Lip_Controllers')
    clusterSetup = pm.createNode('transform', n='NewClusterSetup')
    pm.parent('LipRegion', 'LipsRegion', 'FKOffsetLips_M', 'LipSetup', 'Brs', 'faceHeadJoint', lipCtrlGrps, w=True)
    pm.parent(lipCtrlGrps, lipControllersGrp)

    curvesFromMeshEdgeArray = []
    for each in lipCtrlGrps:
        allHist = pm.listHistory(each, pdo=True)
        for hist in allHist:
            if hist.nodeType() == 'pointOnCurveInfo':
                clusterCurve = hist.inputCurve.connections()[0]
                pm.parent(clusterCurve, clusterSetup)
                crvFrmMshEdg = hist.inputCurve.connections()[0].create.connections()[0]
                pm.connectAttr('LipRegionShape.worldMesh[0]', crvFrmMshEdg + '.inputMesh', f=True)
                curvesFromMeshEdgeArray.append(crvFrmMshEdg)

    # create dummy head and main.
    pm.delete('Brs_orientConstraint1', 'FaceAllSet', 'FaceControlSet', 'MainAndHeadScaleMultiplyDivide', deleteObjArray)
    # Brs scale set to 1.
    pm.setAttr('Brs.sx', 1)
    pm.setAttr('Brs.sy', 1)
    pm.setAttr('Brs.sz', 1)
    # create Hirarchy.
    faceGroup = pm.createNode('transform', n='FaceGroup')
    faceMotionSystem = pm.createNode('transform', n='FaceMotionSystem')
    faceMotionFollowHead = pm.createNode('transform', n='FaceMotionFollowHead')
    controlsSetup = pm.createNode('transform', n='ControlsSetup')
    faceDeformationSystem = pm.createNode('transform', n='faceDeformationSystem')
    regionDeformation = pm.createNode('transform', n='RegionDeformations')
    pm.parent(faceMotionSystem, faceDeformationSystem, faceGroup)
    pm.parent(faceMotionFollowHead, controlsSetup, clusterSetup, 'LipSetup', faceMotionSystem)
    pm.parent(regionDeformation, 'faceHeadJoint', faceDeformationSystem)
    pm.parent('Brs', lipControllersGrp, controlsSetup)
    pm.parent('FKOffsetLips_M', faceMotionFollowHead)
    pm.parent('LipRegion', 'LipsRegion', regionDeformation)
    clusterSetup.rename('ClusterSetup')


def importLipSetup():
    pass
