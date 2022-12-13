#NIA 113371
class DNI:

    def algoritmoValidez(self, dni):
        listaLetras = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
        acc = 0
        dni2 = dni[0:8]
        dni3 = dni[1:8]
        if dni2[0] == "X":
            "0"+dni3
        if dni2[0] == "Y":
            "1"+dni3
        if dni2[0] == "Z":
            "2"+dni3
        for x in range(7):
            acc += int(dni3[x])
            moddedNum = acc%23
            print("El acumulador es", acc)
        print("El modded num es", moddedNum)
        print("La letra que corresponde al moddednum es", listaLetras[moddedNum])
        return listaLetras[moddedNum]

    def comprobarValidez(self, dni):
        tamanno = 9
        letras_dni = ["U","I","O","Ñ"]
        letras_nie = ["X","Y","Z"]
        if len(dni) == tamanno and dni[8].isalpha():
            if dni[8] in letras_dni:
                return False
            else:
                for x in dni[0:7]:
                    if x.isalpha():
                        if dni[0] in letras_nie:
                            if DNI.algoritmoValidez(self, dni) == dni[8]:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        if DNI.algoritmoValidez(self, dni) == dni[8]:
                            return True
                        else:
                            return False
        else:
            return False
