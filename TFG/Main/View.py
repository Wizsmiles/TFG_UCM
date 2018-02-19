import sys
import Nodo
from colorama import init as colorInit
from colorama import Fore, Back, Style

class TreeView():

    @staticmethod
    def show(nodo):
        colorInit()
        TreeView.recursiveShow(nodo, 0, True)

    @staticmethod
    def recursiveShow(nodo, nivel, first):
        # En caso de que sea el primer nivel, no se tabula
        if nivel != 0:
            print('\t', end='', flush=True)
        # Si es el primer hijo del nodo padre, se tabula tantas veces como
        # profundo sea
        if first == False:
            i = 0;
            while i < nivel-1:
                print('\t', end='', flush=True)
                i = i + 1

        # Cambiamos el color de la consola con respecto al Estado del nodo
        if nodo.estado == Nodo.Estado.ERROR:
            print(Fore.RED, end='', flush=True)
        elif nodo.estado == Nodo.Estado.VALIDO:
            print(Fore.GREEN, end='', flush=True)
        else:
            print(Style.RESET_ALL, end='', flush=True)


        print(nodo.valor, end='', flush=True)

        nivel = nivel + 1

        if len(nodo.hijos) != 0:
            first = True

            for i in nodo.hijos:
                TreeView.recursiveShow(i, nivel, first)
                first = False
        else:
            print()
