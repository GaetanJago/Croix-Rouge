
import os
import pickle


class Exercice(object):
    """
    Class dedicated to save exercices
    """
    def __init__(self,name,memberList,description,videoPath):
        """Constructor of exercice class"""
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


class Patient(object):
    """
    Class dedicated to save Patients
    """
    def __init__(self,name,ipp):
        """Constructor of patient class"""
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


class Program(object):
    """
    Class dedicated to save Programms of patients
    """
    def __init__(self,listExercice,patient):
        """Constructor of program class"""
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


class AppData(object):
    """
    Class dedicated to save all patients, all programs and all exercice
    """
    def __init__(self,bibliotheque,listPatient,listProgram):
        """Constructor of appdata classe"""
        self.bibliotheque = bibliotheque
        self.listPatient = listPatient
        self.listProgram = listProgram

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


def readAllParts(file = 'categories.txt'):
    """
    Parser of categories
    """
    parts = []
    
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, file )
    fp = open(my_file)
    line = fp.readline()
    while line != '':  # The EOF char is an empty string
        line = line.rstrip() #skip \n
        if(line[0] != '-'):#if "-" is read, it's a main part
            parts.append(line)
        line = fp.readline()
    fp.close()
    return parts


def seralize(obj,file = 'data.dat'):
    """
    Serialize class appData in data.dat file
    """
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data')
    my_file = os.path.join(my_file, file)
    fp = open(my_file,'wb')
    pickle.dump(obj, fp)
    fp.close()



def deserialize(file = 'data.dat'):
    """
    Deserialize class appData in data.dat file
    """
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data')
    my_file = os.path.join(my_file, file)
    fp = open(my_file,'rb')
    obj = pickle.load(fp)
    fp.close()
    return obj

def initEmptyData():
    """
    Function to clear all data previously serialized
    """
    biblioteque = []
    patients = []
    program = []
    data = AppData(biblioteque, patients, program)
    seralize(data)
    print('data cleared')

if __name__ == "__main__":
    print("main launched")
    #initEmptyData()
    pass
