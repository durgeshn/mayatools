import os
from ConfigParser import SafeConfigParser

mayaFilePath = r"D:\temp\BDG105_004_layNew.ma"
configFilePath = os.path.dirname(__file__) + '/setting.config'


class getSceneDetails(object):
    def __init__(self, mayaFilePath, configFilePath):
        self.mayaFilePath = mayaFilePath
        self.configFilePath = configFilePath

    def get_cams(self):
        all_cams = list()
        with open(self.mayaFilePath, 'r') as fi:
            for line in fi.readlines():
                if line.startswith('createNode camera'):
                    all_cams.append(line.split(' ')[-1].strip().replace(';', '').replace('"', ''))
        return all_cams

    def getFrameRange(self):
        startFrame = float()
        endFrame = float()
        with open(self.mayaFilePath, 'r') as fi:
            for line in fi.readlines():
                if line.find('playbackOptions') != -1:
                    startFrame = line.split('-min ')[-1].split(' -max ')[0]
                    endFrame = line.split('-min ')[-1].split(' -max ')[1].split(' -ast')[0]
        return startFrame, endFrame

    @property
    def getParser(self):
        parser = SafeConfigParser()
        parser.read(self.configFilePath)
        return parser

    def getResolution(self):
        print self.getParser.options('resolution')


a = getSceneDetails(mayaFilePath, configFilePath)
print a.getFrameRange()
print a.get_cams()
print a.getResolution()
