# laboratorio_strings.py
# Script para manipular cadenas con errores de formato / Script to manipulate strings with format errors

def main():
    # 1. Cadena de prueba con errores / Test string with errors
    cadena_original = " pRoDuCtO dE eJeMpIO "

    # 2. Aplicación de métodos solicitados / Application of requested methods
    
    # .strip() para eliminar espacios laterales / .strip() to remove lateral spaces
    cadena_limpia = cadena_original.strip()
    
    # .lower() y .upper() para normalización / .lower() and .upper() for normalization
    cadena_minusculas = cadena_limpia.lower()
    cadena_mayusculas = cadena_limpia.upper()
    
    # .replace() para cambiar espacios por guiones bajos / .replace() to change spaces to underscores
    cadena_reemplazada = cadena_limpia.replace(" ", "_")
    
    # .split() para fragmentar en una lista / .split() to fragment into a list
    lista_palabras = cadena_limpia.split()

    # 3. Diseño de Salida con f-strings (Tabla) / Output Design with f-strings (Table)
    print("=" * 60)
    print(f"| {'MÉTODO / METHOD':<20} | {'RESULTADO / RESULT':<33} |")
    print("=" * 60)
    
    # Mostrar resultados alineados usando modificadores de ancho / Show aligned results using width modifiers
    print(f"| {'Cadena Original':<20} | '{cadena_original}'{' ':<8} |")
    print(f"| {'.strip()':<20} | '{cadena_limpia}'{' ':<10} |")
    print(f"| {'.lower()':<20} | '{cadena_minusculas}'{' ':<10} |")
    print(f"| {'.upper()':<20} | '{cadena_mayusculas}'{' ':<10} |")
    print(f"| {'.replace()':<20} | '{cadena_reemplazada}'{' ':<10} |")
    print(f"| {'.split()':<20} | {str(lista_palabras):<33} |")
    print("=" * 60)
    print("\nProcesamiento completado / Processing completed.")

if __name__ == "__main__":
    main() 