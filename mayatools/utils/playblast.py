import pymel.core as pm
import maya.mel as mel


def mp_playblast(fileName, width, height, startTime=None, endTime=None):
    """
    playblast using custom setting.
    :param fileName: string (file path)
    :param width: int
    :param height: int
    :param startTime: float
    :param endTime: float
    :return: playblast
    """
    cam = pm.ls('*:cameraHD', typ='transform')[0]
    # noinspection PyTypeChecker
    # convertPrspCamToShotCam(cam, 'persp')
    aPlayBackSlider = mel.eval('$tmpVar=$gPlayBackSlider')
    soundFile = pm.windows.timeControl(aPlayBackSlider, q=True, s=True)
    if startTime and endTime:
        pm.playbackOptions(min=startTime)
        pm.playbackOptions(ast=startTime)
        pm.playbackOptions(max=endTime)
        pm.playbackOptions(aet=endTime)
    if soundFile:
        playblast = pm.playblast(f=fileName, format='qt', s=soundFile[0], sqt=0, fo=True, cc=True, p=100,
                                 compression="H.264",
                                 quality=100, height=height, width=width)
    else:
        playblast = pm.playblast(f=fileName, format='qt', sqt=0, fo=True, cc=True, p=100,
                                 compression="H.264",
                                 quality=100, height=height, width=width)
    return playblast


def convertPrspCamToShotCam(cam, prspCam):
    """
    convert perspective cam as shot cam.
    cam transform node as constraint
    cam shape attributes connect.
    :param cam: string
    :param prspCam: string
    :return: prspCam
    """
    cam = pm.PyNode(cam)
    prspCam = pm.PyNode(prspCam)
    camShape = cam.getShape()
    prspShape = prspCam.getShape()

    camShapeAttrs = pm.listAttr(camShape)

    pm.parentConstraint(cam, prspCam)
    for each in camShapeAttrs:
        try:
            pm.connectAttr(camShape + '.' + each, prspShape + '.' + each, f=True)
        except:
            pass
    return prspCam


def getSoundFilePath():
    audio = pm.ls(type='audio')[0]
    path = audio.filename.get()
    if path:
        print path
        return path
    else:
        return False
