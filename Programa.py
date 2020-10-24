from FechaHora import FechaHora

####################################################VALIDA EN MAIN##
def bisiesto(a):
    if a %4==0 and a %100 !=0 or a %400==0:
        return True
    else:
        return False

def valida (d, mes, a, h, m, s):
    if (a in range (3000)):
        if (mes in range(13)):
            if (mes==11 or mes==4 or mes==6 or mes==9):
                if (d in range(30)):
                    if (h in range(24)):
                        if (m in range(60)):
                            if (s in range(60)):
                                return True
                            else:
                                print("Los valores válidos son de 0..59")
                                return False
                        else:
                            print("Los valores válidos son de 0..59")
                            return False
                    else:
                        print("Los valores válidos son de 1..23")
                        return False
                else:
                    print("Los valores válidos para dias en el mes ", mes," son de 1..30")
                    return False
            else:
                if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==10 or mes==12):
                    if (d in range(31)):
                        if (h in range(24)):
                            if (m in range(60)):
                                if (s in range(60)):
                                    return True
                                else:
                                    print("Los valores válidos son de 0..59")
                                    return False
                            else:
                                print("Los valores válidos son de 0..59")
                                return False
                        else:
                            print("Los valores válidos son de 1..23")
                            return False
                    else:
                        print("Los valores válidos para dias en el mes ", mes, " son de 1..31")
                        return False
                else:
                    if (mes==2 and bisiesto(a)):
                        if (d in range(1, 30)):
                            if (h in range(24)):
                                if (m in range(60)):
                                    if (s in range(60)):
                                        return True
                                    else:
                                        print("Los valores válidos son de 0..59")
                                        return False
                                else:
                                    print("Los valores válidos son de 0..59")
                                    return False
                            else:
                                print("Los valores válidos son de 1..23")
                                return False
                        else:
                            print("Los valores válidos para dias en el mes ", mes, " son de 1..29")
                            return False
                    else:
                        if (d in range(1,29)):
                            if (h in range(24)):
                                if (m in range(60)):
                                    if (s in range(60)):
                                        return True
                                    else:
                                        print("Los valores válidos son de 0..59")
                                        return False
                                else:
                                    print("Los valores válidos son de 0..59")
                                    return False
                            else:
                                print("Los valores válidos son de 1..23")
                                return False
                        else:
                            print("Los valores válidos para dias en el mes ", mes, " son de 1..28")
                            return False

####################################################FIN VALIDA###





if __name__ == '__main__':

    d=int(input("\n -Ingrese Dia: "))
    mes=int(input("\n -Ingrese Mes: "))
    a=int(input("\n -Ingrese Año: "))
    h=int(input("\n -Ingrese Hora: "))
    m=int(input("\n -Ingrese Minutos: "))
    s=int(input("\n -Ingrese Segundos: "))

    ##validar = valida()CREAR CLASE VALIDA

    if valida(d, mes, a, h, m, s):
        r =FechaHora()
        r2 =FechaHora()
        r1 =FechaHora(d, mes, a)
        print ('______________________________________________________\n ')
        r2 =FechaHora(d, mes, a, h, m, s)
        r.Mostrar()
        r1.Mostrar()
        r2.Mostrar()
        input('\n >> Presione enter para continuar')
        r.ponerEnHora(5)
        r.Mostrar()
        input('\n >> Presione enter para continuar')
        r2.ponerEnHora(13, 30)
        r2.Mostrar()
        input('\n >> Presione enter para continuar')
        r.ponerEnHora(14, 30, 25)
        r.Mostrar()
        input('\n >> Presione enter para continuar')
        r.AdelantarHora(3)
        r.Mostrar()
        r.AdelantarHora(7, 30, 35)
        r.Mostrar()
        input('\n >> Presione enter para continuar')
        r1.AdelantarHora(1, 15)
        r1.Mostrar()
        r2.AdelantarHora(0, 15, 30)
        r2.Mostrar()
    else:
        print('______________________________________________________ ')
        print('\n\t >> Ingreso de datos incorrecto << ')
        print(' \t >> Intentelo de nuevo más tarde <<')
        print('______________________________________________________\n ')