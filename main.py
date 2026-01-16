from controlador import SimplexControlador

if __name__ == "__main__":
    try:
        app = SimplexControlador()
        app.ejecutar()
    except KeyboardInterrupt:
        print("\nPrograma cerrado por el usuario.")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")
