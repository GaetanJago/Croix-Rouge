import data
import unittest
from data import *


class TestDataClasses(unittest.TestCase):
    """
    Class to test data file classes
    """
    def setUp(self):
        """Init variables needed for all tests"""
        self.listMembre = []
        self.listMembre.append("bras gauche")
        self.listMembre.append("bras droit")
        self.exercice = data.Exercice("Mouvement des bras",self.listMembre,"Pour rééducation", "ex/path")
        self.exercice_a = data.Exercice("Mouvement des jambes",self.listMembre,"Pour rééducation", "ex/path")
        self.exercice_b = data.Exercice("Mouvement des hanches",self.listMembre,"Pour rééducation", "ex/path")
        self.exercice_1 = data.Exercice("Mouvement des",self.listMembre,"Pour rééducation", "ex/path")
        self.exercice_2 = data.Exercice("Mouvement hanches",self.listMembre,"Pour rééducation", "ex/path")

        self.patient = data.Patient("Claude" , "123")
        self.patient_b = data.Patient("Gaetan" , "789")

        self.patient_1 = data.Patient("JP" , "456")
        self.patient_2 = data.Patient("JN" , "654")

        self.listExo = [self.exercice_a,self.exercice_b]
        self.listExo_b = [self.exercice_1,self.exercice_2]
        self.program_a = data.Program(self.listExo,self.patient_b)
        self.program_b = data.Program(self.listExo_b,self.patient_b)

        self.bib_a = [self.exercice,self.exercice_a,self.exercice_b]
        self.bib_b = [self.exercice_1,self.exercice_2]

        self.listP_a = [self.patient,self.patient_b]
        self.listP_b = [self.patient_1,self.patient_2]

        self.allData = data.AppData(self.bib_a,self.listP_a,[self.program_a,self.program_b])

    def test_Exercice_GetName(self):
        self.assertEqual("Mouvement des bras", self.exercice.getName())

    def test_Exercice_GetMemberList(self):
        self.assertIn("bras gauche", self.exercice.getMemberList())
        self.assertIn("bras droit", self.exercice.getMemberList())

    def test_Exercice_GetDescription(self):
        self.assertEqual("Pour rééducation", self.exercice.getDescription())

    def test_Exercice_GetVideoPath(self):
        self.assertEqual("ex/path", self.exercice.getVideoPath())

    def test_Exercice_SetName(self):
        self.exercice.setName("Mouvement des ")
        self.assertEqual("Mouvement des ", self.exercice.getName())

    def test_Exercice_SetMemberList(self):
        liste = []
        liste.append("bras g")
        liste.append("bras d")
        self.exercice.setMemberList(liste)
        self.assertIn("bras g", self.exercice.getMemberList())
        self.assertIn("bras d", self.exercice.getMemberList())
    
    def test_Exercice_SetDescription(self):
        self.exercice.setDescription("Pour quelque chose")
        self.assertEqual("Pour quelque chose", self.exercice.getDescription())

    def test_Exercice_SetVideoPath(self):
        self.exercice.setVideoPath("c://cr")
        self.assertEqual("c://cr", self.exercice.getVideoPath())

    def test_Patient_GetName(self):
        self.assertEqual("Claude", self.patient.getName())

    def test_Patient_GetIpp(self):
        self.assertEqual("123", self.patient.getIpp())

    def test_Patient_SetName(self):
        self.patient.setName("François")
        self.assertEqual("François", self.patient.getName())

    def test_Patient_SetIpp(self):
        self.patient.setIPP("321")
        self.assertEqual("321", self.patient.getIpp())
    
    def test_Program_GetPatient(self):
        self.assertEqual("Gaetan",self.program_a.getPatient().getName())

    def test_Program_GetListExo(self):
        self.assertIn(self.exercice_a,self.program_a.getListExercice())
        self.assertIn(self.exercice_b,self.program_a.getListExercice())

    def test_Program_SetPatient(self):
        self.program_a.setPatient(self.patient)
        self.assertEqual(self.patient,self.program_a.getPatient())

    def test_Program_SetListExo(self):
        
        self.program_a.setListExercice([self.exercice_1,self.exercice_2])
        self.assertIn(self.exercice_1,self.program_a.getListExercice())
        self.assertIn(self.exercice_2,self.program_a.getListExercice())
    
    def test_AppData_GetBibliotheque(self):
        self.assertEqual(self.bib_a,self.allData.getBibliotheque())

    def test_AppData_SetBibliotheque(self):
        self.allData.setBibliotheque(self.bib_b)
        self.assertEqual(self.bib_b,self.allData.getBibliotheque())

    def test_AppData_GetListPatient(self):
        self.assertIn(self.patient,self.allData.getListPatient())

    def test_AppData_SetListPatient(self):
        self.allData.getListPatient().append(self.patient_1)
        self.assertIn(self.patient_1,self.allData.getListPatient())


    # SERIALIZATION

    def test_serialization(self):
        data.seralize(self.allData,"test.dat")
        data_out = data.deserialize("test.dat")
        self.assertEqual(self.allData.getListPatient()[0].getName(),
            data_out.getListPatient()[0].getName())

if __name__ == "__main__":
    """Launch tests""" 
    unittest.main()
    pass