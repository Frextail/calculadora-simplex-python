from modelo import SimplexModelo
from vista import SimplexVista
import numpy as np

class SimplexControlador:
    def __init__(self):
        self.vista = SimplexVista()

    def ejecutar(self):
        self.vista.limpiar_pantalla()
        print("=== CONFIGURACIÓN DEL PROBLEMA SIMPLEX ===")
        nv = int(self.vista.pedir_numero("Número de variables (X): "))
        nr = int(self.vista.pedir_numero("Número de restricciones (<=): "))

        c_obj = [self.vista.pedir_numero(f"Coeficiente X{i+1}: ") for i in range(nv)]
        a_res = []
        b_const = []
        for i in range(nr):
            print(f"\nRestricción {i+1}:")
            a_res.append([self.vista.pedir_numero(f"  X{j+1}: ") for j in range(nv)])
            b_const.append(self.vista.pedir_numero("  Constante b: "))

        mod = SimplexModelo(c_obj, a_res, b_const)
        self.vista.mostrar_tabla(mod.tabla, mod.encabezado, "MATRIZ INICIAL")

        it = 1
        while True:
            # CONDICIÓN: Solo variables X en la última fila
            fila_objetivo_X = mod.tabla[-1, :mod.n_vars]
            if all(coef >= 0 for coef in fila_objetivo_X):
                break

            col_p = np.argmin(fila_objetivo_X)
            
            ratios = []
            filas_v = []
            for i in range(mod.n_restr):
                if mod.tabla[i, col_p] > 0:
                    ratios.append(mod.tabla[i, -1] / mod.tabla[i, col_p])
                    filas_v.append(i)
            
            if not ratios:
                print("Error: Problema no acotado."); return

            fila_p = filas_v[np.argmin(ratios)]
            mod.pivotear(fila_p, col_p)
            
            self.vista.mostrar_tabla(mod.tabla, mod.encabezado, f"ITERACIÓN {it}")
            it += 1

        vars_f, p_f = mod.obtener_resultados()
        self.vista.mostrar_resultados(vars_f, mod.encabezado, p_f, mod.n_restr)
