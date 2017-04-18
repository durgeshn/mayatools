import os
from ConfigParser import SafeConfigParser

mayaFilePath = r"D:\temp\BDG105_004_lay.ma"
configFilePath = os.path.dirname(__file__) + '/setting.config'


class getSceneDetails(object):
    def __init__(self, mayaFilePath, configFilePath):
        self.mayaFilePath = mayaFilePath
        self.configFilePath = configFilePath

    @property
    def getParser(self):
        parser = SafeConfigParser()
        parser.read(self.configFilePath)
        return parser

    def getReferences(self, nameFilter=['cam', 'Cam', 'CAM']):
        allReferences = []
        camReferences = []
        with open(self.mayaFilePath, 'r') as fi:
            for line in fi.readlines():
                if line.startswith('file -rdi'):
                    allReferences.append(line.split(' ')[-1].replace('"', '').replace(';', '').strip())
        for each in allReferences:
            for filt in nameFilter:
                if each.find(filt) != -1:
                    camReferences.append(each)
        return camReferences

    def get_cams(self):
        all_cams = []
        mainFileCams = self._getCams(self.mayaFilePath)
        for each in mainFileCams:
            all_cams.append(each)
        allReferences = self.getReferences()
        for each in allReferences:
            for eachFile in self._getCams(each):
                all_cams.append(eachFile)
        return list(set(all_cams))

    def _getCams(self, mayaFilePath):
        all_cams = list()
        if mayaFilePath.startswith('$'):
            env = mayaFilePath.split('/')[0]
            newPath = self.getParser.get('env_path', env[1:])
            mayaFilePath = mayaFilePath.replace(env, newPath)
        with open(mayaFilePath, 'r') as fi:
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

    def getResolution(self):
        print self.getParser.options('resolution')


a = getSceneDetails(mayaFilePath, configFilePath)
# print a.getFrameRange()
# print a.get_cams()
# print a.getResolution()
print a.get_cams()
