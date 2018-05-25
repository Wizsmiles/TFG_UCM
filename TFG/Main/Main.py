'''
Created on 3 ene. 2018
@author: Jose J. Escudero Gomez
'''

import sys
import Model.Nodo as Nodo
from Controller import Controller

arbol = Nodo.Nodo()
cont = 0
contWait = 0
wait = False
argv = sys.argv[1:]

inputfile = ''
function = ''
graphics = False
fusion = False

try:
    if "-g" in argv:
        graphics = True
        del argv[argv.index("-g")]
    if "-f" in argv:
        fusion = True
        del argv[argv.index("-f")]

    inputfile = argv[0]
    function = argv[1]

    if len(argv) > 2:
        raise Exception("Too many arguments")

except Exception:
    if len(argv) == 1:
        print("\nERROR: Missing one argument. A function name is needed")
    elif len(argv) < 1:
        print("\nERROR: Missing two arguments. A input file and a function"
              " name are needed")
    elif len(argv) > 2:
        print("\nERROR: Too many arguments. Only two needed")

    print("Usage: Main.py <inputfile> <function> <-g|-f>\n\t- The -g flag"
          " enables the GUI\n\t- The -f flag enables the node fusion")
    exit()

fileArray = inputfile.split('/')
folder = fileArray[0:len(fileArray)-1]
folder = '/'.join(str(x) for x in folder)

sys.path.insert(0, folder)

file = fileArray[len(fileArray)-1]
file = file.split('.')[0]

def trace_calls(frame, event, arg):
    global wait, cont, contWait, arbol

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


command = "from " + file + " import " + function + " as func"
exec(command)

tr = sys.gettrace()  # Guardo la traza original del programa
sys.settrace(trace_calls)  # Traceo la ejecucion del programa

try:
    func()
except Exception:
    None

sys.settrace(tr)  # Cargo la traza original guardada

if fusion:
    arbol.fusionNodos()
arbol.calcularPeso()

controller = Controller(arbol, graphics)
controller.run()
