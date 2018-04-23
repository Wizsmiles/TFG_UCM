'''
Created on 3 ene. 2018
@author: Jose J. Escudero Gomez
'''

import sys
import Model.Recorridos as Recorridos
import Model.Nodo as Nodo
import Ejemplos
import getopt
import View.Tree as View

arbol = Nodo.Nodo()
cont = 0
contWait = 0
wait = False


def trace_calls(frame, event, arg):
    global wait, cont, contWait

    co = frame.f_code
    f_name = co.co_name

    # Cuando se produce una expcion, se producen tres return basura capturados
    # por la traza, esto hace que el flujo no se vea afectado
    if not wait:
        if event == "return" or event == "exception":

            if f_name != "_ag" and f_name != "encode":

                if event == "exception":
                    arg = arg[1]
                    wait = True

                params = frame.f_locals
                arbol.insertarValor(arg, cont)
                arbol.insertarParamsMods(params, cont)
                cont -= 1

        if event == "call":

            if f_name != "_ag" and f_name != "encode":

                params = frame.f_locals
                cont += 1

                if cont == 1:

                    arbol.setNombre(f_name)
                    arbol.setParamsEntrada(params)

                else:

                    hijo = Nodo.Nodo()
                    hijo.setNombre(f_name)
                    hijo.setParamsEntrada(params)
                    arbol.insertar(hijo, cont)

    # Controla los return basura tras un except. Esta basura provoca fallos en
    # el arbol
    else:
        if contWait < 3:
            contWait += 1
        else:
            wait = False
            contWait = 0

    return trace_calls


# TODO #
# debugFile = ''
# debugMethod = ''
#
# # if len(sys.argv) > 0 and len(sys.argv) <= 2:
# try:
#     opts, args = getopt.getopt(sys.argv,"hf:m:",["file=","method="])
# except getopt.GetoptError:
#     print('Main.py -f <debugfile> -m <debugmethod>')
#     sys.exit(2)
# for opt, arg in opts:
#     if opt == '-h':
#         print('Main.py -f <debugfile> -m <debugmethod>')
#         sys.exit()
#     elif opt in ("-f", "--file"):
#         debugFile = arg
#     elif opt in ("-m", "--method"):
#         debugMethod = arg


prueba = "Ejemplos"
prueba2 = "ejemplo1"
exec("from " + prueba + " import " + prueba2 + " as prueba3")

tr = sys.gettrace()  # Guardo la traza original del programa
sys.settrace(trace_calls)  # Traceo la ejecucion del programa

try:
    prueba3()
except:
    None

sys.settrace(tr)  # Cargo la traza original guardada

arbol.fusionNodos()
arbol.calcularPeso()
# Tras retornar la traza original del programa calculo el nNodos de cada nodo

# recorrido = Recorridos.Recorrido(arbol)
# recorrido.inicializarDQ()

View.initGUI(arbol)
