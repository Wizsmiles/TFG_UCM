import Model.Nodo as Nodo
from colorama import init as colorInit
from colorama import Fore, Back, Style


class TreeView():

    @staticmethod
    def show(nodo):
        colorInit()
        TreeView.recursiveShow(nodo, 0)

    @staticmethod
    def recursiveShow(nodo, nivel):
        for i in range(0, nivel):
            print('\t', end='', flush=True)

        # Cambiamos el color de la consola con respecto al Estado del nodo
        if nodo.estado == Nodo.Estado.ERROR:
            print(Fore.RED, end='', flush=True)
        elif nodo.estado == Nodo.Estado.VALIDO:
            print(Fore.GREEN, end='', flush=True)
        elif nodo.estado == Nodo.Estado.CONFIAR:
                print(Fore.CYAN, end='', flush=True)
        elif nodo.estado == Nodo.Estado.INACEPTABLE:
            print(Fore.YELLOW, end='', flush=True)
        elif nodo.estado == Nodo.Estado.DESCONOCIDO:
            print(Fore.MAGENTA, end='', flush=True)
        else:
            print(Style.RESET_ALL, end='', flush=True)

        print(nodo.getNombre(), end='', flush=True)
        print(' Entrada: (', nodo.getParamsEntrada(), ')', end='', flush=True)
        print(' Salida: (', nodo.getParamsMods(), ')', end='', flush=True)
        print(' -->', nodo.getValor(), flush=True)

        nivel = nivel + 1

        if len(nodo.hijos) != 0:
            for i in nodo.hijos:
                if i.padre.estado ==  Nodo.Estado.ERROR or i.padre.estado ==  Nodo.Estado.DESCONOCIDO or i.padre.estado ==  Nodo.Estado.INDEFINIDO:
                    TreeView.recursiveShow(i, nivel)
                print(Style.RESET_ALL, end='', flush=True)
        else:
            print(Style.RESET_ALL, end='', flush=True)
