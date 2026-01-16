import os
from fractions import Fraction

class SimplexVista:
    @staticmethod
    def limpiar_pantalla():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def formatear_numero(n):
        """Muestra fracción si el decimal es largo o periódico."""
        if n.denominator == 1:
            return str(n.numerator)
        decimal_val = float(n)
        if abs(decimal_val - round(decimal_val, 2)) < 1e-10:
            return str(round(decimal_val, 2))
        return f"{n.numerator}/{n.denominator}"

    def pedir_numero(self, mensaje):
        while True:
            dato = input(mensaje).strip()
            try:
                if not dato: return Fraction(0)
                return Fraction(dato)
            except ValueError:
                print("❌ Error: Ingrese un valor válido (ej: 5, 0.5 o 1/3).")

    def mostrar_tabla(self, tabla, encabezado, titulo):
        print(f"\n--- {titulo} ---")
        header = " | ".join(f"{h:^10}" for h in encabezado)
        print(header)
        print("-" * len(header))
        for fila in tabla:
            print(" | ".join(f"{self.formatear_numero(val):^10}" for val in fila))

    def mostrar_resultados(self, variables, encabezado, beneficio, n_restr):
        print("\n" + "="*55)
        print(f"{'🏁 RESULTADOS FINALES':^55}")
        print("="*55)
        for nombre, valor in variables.items():
            print(f"  Variable {nombre} = {self.formatear_numero(valor)}")
        print("-" * 55)
        print(f"  BENEFICIO TOTAL (P) = {self.formatear_numero(beneficio)}")
        print("="*55)
