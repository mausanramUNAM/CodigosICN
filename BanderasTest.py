
import time
import argparse
 

def getdata(Flag):
    try:
        #a=flag.t[0])
        time.sleep(1)
        print(Flag.t[0]+'\r')
        Flag.t[0]='True'
    except:
        Flag.t[0]='True' 
    #return Flag

def parser():
    parser = argparse.ArgumentParser(prog='Temp Control',description='Programa de vizualizacion y control de temperatura para el banco de pruebas ICN-UNAM')

    parser.add_argument('-t',type=str,nargs=1)
    argObj=parser.parse_args()
    return argObj

def main(Flag):
    while Flag.t[0]=='True':
        try:
            x=getdata(Flag)
        except:
            print('No se tecleo un numero')
            break


if __name__ == "__main__":
   argObj=parser()
   exitcode=main(argObj)
   exit(code=exitcode)

