import unittest
import dni

class MyTestCase(unittest.TestCase):
    def test_dni_todo_ceros(self):
        testdni = dni.DNI()
        ejemplodni = "000000000"
        tmp = testdni.comprobarValidez(ejemplodni)
        self.assertFalse(tmp)

    def test_dni_valido(self):
        testdni = dni.DNI()
        ejemplodni = "58015711M"
        tmp = testdni.comprobarValidez(ejemplodni)
        self.assertTrue(tmp)

    def test_dni_excede_tamanno(self):
        testdni = dni.DNI()
        ejemplodni = "0000000000M"
        tmp = testdni.comprobarValidez(ejemplodni)
        self.assertFalse(tmp)

    def test_dni_incluir_letra(self):
        testdni = dni.DNI()
        ejemplodni = "00000000M"
        tmp = testdni.comprobarValidez(ejemplodni)
        self.assertFalse(tmp)

    def test_dni_letra_en_medio(self):
        testdni = dni.DNI()
        ejemplodni = "L8015711N"
        tmp = testdni.comprobarValidez(ejemplodni)
        self.assertFalse(tmp)

    def test_contiene_U(self):
        testdni = dni.DNI()
        ejemplodni = "00000000U"
        tmp = testdni.comprobarValidez(ejemplodni)
        self.assertFalse(tmp)

    def test_contiene_I(self):
        testdni = dni.DNI()
        ejemplodni = "00000000I"
        tmp = testdni.comprobarValidez(ejemplodni)
        self.assertFalse(tmp)

    def test_contiene_Ñ(self):
        testdni = dni.DNI()
        ejemplodni = "00000000Ñ"
        tmp = testdni.comprobarValidez(ejemplodni)
        self.assertFalse(tmp)

    def test_contiene_O(self):
        testdni = dni.DNI()
        ejemplodni = "00000000O"
        tmp = testdni.comprobarValidez(ejemplodni)
        self.assertFalse(tmp)

    def test_contiene_X_NIE(self):
        testdni = dni.DNI()
        ejemplonie = "X0000000T"
        tmp = testdni.comprobarValidez(ejemplonie)
        self.assertTrue(tmp)

    def test_contiene_Y_NIE(self):
        testdni = dni.DNI()
        ejemplonie = "Y0000000M"
        tmp = testdni.comprobarValidez(ejemplonie)
        self.assertTrue(tmp)

    def test_contiene_Z_NIE(self):
        testdni = dni.DNI()
        ejemplonie = "Z0000000M"
        tmp = testdni.comprobarValidez(ejemplonie)
        self.assertTrue(tmp)

    def test_contiene_X_NIE(self):
        testdni = dni.DNI()
        ejemplonie = "R0000000M"
        tmp = testdni.comprobarValidez(ejemplonie)
        self.assertFalse(tmp)

    def test_calculo_es_correcto(self):
        testdni = dni.DNI()
        ejemplonie = "00000000T"
        tmp = testdni.comprobarValidez(ejemplonie)
        self.assertTrue(tmp)

    def test_calculo_es_correcto_dos(self):
        testdni = dni.DNI()
        ejemplonie = "09812300T"
        tmp = testdni.comprobarValidez(ejemplonie)
        self.assertTrue(tmp)

    def test_calculo_es_fake_dos(self):
        testdni = dni.DNI()
        ejemplonie = "09812200T"
        tmp = testdni.comprobarValidez(ejemplonie)
        testdni.algoritmoValidez(ejemplonie)
        self.assertFalse(tmp)

    def test_calculo_nie(self):
        testdni = dni.DNI()
        ejemplonie = "Y9812200C"
        tmp = testdni.comprobarValidez(ejemplonie)
        self.assertFalse(tmp)



