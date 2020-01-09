import data
import unittest
from data import *

class RandomTest(unittest.TestCase):

    def setUp(self):
        listMembre = []
        listMembre.append("bras gauche")
        listMembre.append("bras droit")
        self.exercice = data.Exercice("Mouvement des bras",listMembre,"Pour rééducation", "ex/path")

    def test_ExerciceGetName(self):
        self.assertEqual("Mouvement des bras", self.exercice.getName())

    def test_ExerciceGetMemberList(self):
        self.assertIn("bras gauche", self.exercice.getMemberList())
        self.assertIn("bras droit", self.exercice.getMemberList())

    def test_ExerciceGetDescription(self):
        self.assertEqual("Pour rééducation", self.exercice.getDescription())

    

if __name__ == "__main__":
    unittest.main()
    pass