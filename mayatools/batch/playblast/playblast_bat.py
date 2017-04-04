import os
import tempfile
from subprocess import Popen, PIPE
import pprint


def test():
    mayaFileLocation = "D:/temp/BDG105_004_layNew.ma"
    mayaPath = "C:/Program Files/Autodesk/Maya2015/bin/mayabatch.exe"
    scriptPath = "C:/Users/amol/PycharmProjects/mayatools/batch/playblast/startupCmd.mel"

    print "Working On :- %s" % mayaFileLocation
    process = Popen([mayaPath, "-batch", "-file", mayaFileLocation, "-script", scriptPath], stdout=PIPE)
    stdout, stderr = process.communicate()
    print stdout
    print stderr


def batPlayblast(cam, mayaFilePath, startFrame, endFrame, xRes=1280, yRes=720, imageName=None,
                 renderDirPath=None, mayaVersion='Maya2015'):
    """
    create playblast using hardware render.
    :param cam: string
    :param mayaFilePath: string (maya file path)
    :param xRes: int (x resolution)
    :param yRes: int (y resolution)
    :param startFrame: float
    :param endFrame: float
    :param imageName: string
    :param renderDirPath: string (path)
    :param mayaVersion: string
    :return: playblast
    """
    renderExe = "C:/Program Files/Autodesk/%s/bin/Render.exe" % mayaVersion
    if not imageName:
        imageName = 'test'
    if not renderDirPath:
        renderDirPath = tempfile.mktemp(prefix='test_')
    preCmd = "python(\"execfile(\'C:/Users/amol/PycharmProjects/mayatools/utils/playblast.py\')\");python(\"getSoundFilePath();\")"
    # preCmd = "python(\"execfile(\'C:/Users/amol/PycharmProjects/mayatools/utils/playblast.py\')\");"
    # preCmd = 'python("execfile(' + 'C:/Users/amol/PycharmProjects/mayatools/utils/playblast.py' + ');getSoundFilePath()");'
    # preCmd = 'print "abcddddddddddddddddddddddddddddddddddddddddd";'
    os.environ['PROD_SERVER'] = "P:/badgers_and_foxes"
    render_cmd = '"{0}" -s {7} -e {8} -preRender "{9}" -r "hw2" -of "png" -cam "{1}" -im "{6}" -fnc 3 -x {2} -y {3} -rd "{4}" "{5}"'.format(
        renderExe,
        cam, xRes,
        yRes,
        renderDirPath,
        mayaFilePath,
        imageName,
        startFrame,
        endFrame,
        preCmd
    )
    print render_cmd
    print preCmd
    process = Popen(render_cmd, stdout=PIPE)
    stdout, stderr = process.communicate()
    pprint.pprint(stdout)
    pprint.pprint(stderr)
    return renderDirPath


batPlayblast('SH004_CAM:cameraHD', 'D:/temp/BDG105_004_layNew.ma', 101, 105)
