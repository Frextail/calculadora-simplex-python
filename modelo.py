import numpy as np
from fractions import Fraction

class SimplexModelo:
    def __init__(self, c, A, b):
        self.c = c
        self.A = A
        self.b = b
        self.n_vars = len(c)
        self.n_restr = len(b)
        
        # [ Variables X | Holguras S | P | CONSTANTE ]
        self.cols = self.n_vars + self.n_restr + 2
        self.filas = self.n_restr + 1
        self.tabla = np.zeros((self.filas, self.cols), dtype=object)
        self.tabla.fill(Fraction(0))
        
        self.encabezado = ([f"X{i+1}" for i in range(self.n_vars)] + 
                          [f"S{i+1}" for i in range(self.n_restr)] + 
                          ["P", "CONST"])
        self.inicializar()

    def inicializar(self):
        for i in range(self.n_restr):
            for j in range(self.n_vars):
                self.tabla[i, j] = self.A[i][j]
            self.tabla[i, self.n_vars + i] = Fraction(1)
            self.tabla[i, -1] = self.b[i]
        
        for j in range(self.n_vars):
            self.tabla[-1, j] = -self.c[j]
        self.tabla[-1, -2] = Fraction(1)
        self.tabla[-1, -1] = Fraction(0)

    def pivotear(self, fila_p, col_p):
        pivote = self.tabla[fila_p, col_p]
        self.tabla[fila_p] = self.tabla[fila_p] / pivote
        for i in range(self.filas):
            if i != fila_p:
                factor = self.tabla[i, col_p]
                self.tabla[i] = self.tabla[i] - (factor * self.tabla[fila_p])

    def obtener_resultados(self):
        res = {}
        for j in range(self.n_vars):
            columna = self.tabla[:-1, j]
            if np.sum(columna == 1) == 1 and np.sum(columna == 0) == self.n_restr - 1:
                idx = np.where(columna == 1)[0][0]
                res[f"X{j+1}"] = self.tabla[idx, -1]
            else:
                res[f"X{j+1}"] = Fraction(0)
        return res, self.tabla[-1, -1]
