
import os
import pickle

"""
Class dedicated to save exercices
"""
class Exercice(object):
    def __init__(self,name,memberList,description,videoPath):
        self.name = name
        self.memberList = memberList
        self.description = description
        self.videoPath = videoPath

    def getName(self):
        return self.name

    def getMemberList(self):
        return self.memberList
    
    def getDescription(self):
        return self.description
    
    def getVideoPath(self):
        return self.videoPath

    def setName(self,name):
        self.name = name
    
    def setMemberList(self,memberList):
        self.memberList = memberList
    
    def setDescription(self,description):
        self.description = description

    def setVideoPath(self,path):
        self.videoPath = path

"""
Class dedicated to save Patients
"""
class Patient(object):
    def __init__(self,name,ipp):
        self.ipp = ipp
        self.name = name
    def getName(self):
        return self.name
    def getIpp(self):
        return self.ipp
    def setName(self,name):
        self.name = name
    def setIPP(self,ipp):
        self.ipp = ipp

"""
Class dedicated to save Programms of patients
"""
class Program(object):
    def __init__(self,listExercice,patient):
        self.listExercice = listExercice
        self.patient = patient
    def getListExercice(self):
        return self.listExercice
    def getPatient(self):
        return self.patient

    def setListExercice(self,list):
        self.listExercice = list

    def setPatient(self,patient):
        self.patient = patient

"""
Class dedicated to save all patients, all programs and all exercice
"""
class AppData(object):
    def __init__(self,bibliotheque,listPatient,listProgram):
        self.bibliotheque = bibliotheque
        self.listPatient = listPatient
        self.listProgram = listProgram
        self.listParts = readAllParts()
    def getBibliotheque(self):
        return self.bibliotheque
    def getListPatient(self):
        return self.listPatient
    def getListProgram(self):
        return self.listProgram

    def setBibliotheque(self,bibliotheque):
        self.bibliotheque = bibliotheque
    
    def setListPatient(self,list):
        self.listPatient = list

    def setListProgram(self,list):
        self.listProgram = list

"""
Parser of categories.txt file
"""
def readAllParts():
    parts = []
    
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'categories.txt')
    fp = open(my_file)
    line = fp.readline()
    while line != '':  # The EOF char is an empty string
        line = line.rstrip() #skip \n
        if(line[0] != '-'):
            parts.append(line)
        line = fp.readline()
    fp.close()
    return parts

"""
Serialize class data in data.dat file
"""
def seralize(obj):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data')
    my_file = os.path.join(my_file, 'data.dat')
    fp = open(my_file,'wb')
    pickle.dump(obj, fp)
    fp.close()


"""
Deserialize class data in data.dat file
"""
def deserialize():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data')
    my_file = os.path.join(my_file, 'data.dat')
    fp = open(my_file,'rb')
    obj = pickle.load(fp)
    fp.close()
    return obj


if __name__ == "__main__":
    print("main launched")
    """
    parts = readAllParts()
    for part in parts :
        print(part)
    """
    obj = Patient("jaques" , "454514545")
    seralize(obj)
    a = deserialize()
    print(a.getName())
    a.setName("paul")
    print(a.getName())
    pass
