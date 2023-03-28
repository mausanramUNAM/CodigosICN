import argparse

def rampStatus():
    return 

def parser():
     parser = argparse.ArgumentParser(prog='Temp Control',description='Programa de vizualizacion y control de temperatura para el banco de pruebas ICN-UNAM')

     #parser.add_argument('--sp',type=float,nargs= 3,help="Devuelte la temperatura actual del sistema. Ingresa la nueva temperatura para cambiarla")
     parser.add_argument('--ramp',type=float,nargs = 1, help = "Devuelve la rampa de temp. actual. Ingresa la nueva rampa de temp.")

     argObj = parser.parse_args()
     return argObj

def main(argObj):
    if argObj.sp is not None:
        funcion(argObj.sp[0],argObj.sp[1],argObj.sp[2])
    elif argObj.ct is not None:
        argumento(argObj.ct[0])

if __name__== "__main__":
    argObj=parser()
    exitcode=main(argObj)
    exit(code=exitcode)