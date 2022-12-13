
class DNI:

    def algoritmoValidez(self, dni):
        listaLetras = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
        acc = 0
        dni2 = dni[0:7]
        dniIntegers = list(map(int, dni2))
        for x in dniIntegers:
            acc += dniIntegers[x]
            moddedNum = acc%23
        print(acc)
        return listaLetras[moddedNum]

    def comprobarValidez(self, dni):
        tamanno = 9
        letras_dni = ["U","I","O","Ñ"]
        letras_nie = ["X","Y","Z"]
        if len(dni) == tamanno and dni[8].isalpha():
            if dni[8] in letras_dni:
                return False
            else:
                if DNI.algoritmoValidez(self, dni) == dni[8]:
                    return True
                else:
                    for x in dni[0:7]:
                        if x.isalpha():
                            if dni[0] in letras_nie:
                                return True#calculo
                            else:
                                return False
                        else: #Si X es dígito
                            return True
        else:
            return False
