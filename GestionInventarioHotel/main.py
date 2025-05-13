import json
import sys
from antlr4 import *
from CSVFilterLexer import CSVFilterLexer
from CSVFilterParser import CSVFilterParser
from MyCSVVisitor import MyCSVVisitor
from CustomErrorListener import CustomErrorListener

def cargar_consultas():
    try:
        with open('consultas.json', 'r', encoding='utf-8') as f:
            datos = json.load(f)
            return datos['consultas']
    except FileNotFoundError:
        print("\n❌ Error: Archivo 'consultas.json' no encontrado")
        exit()
    except json.JSONDecodeError:
        print("\n❌ Error: Archivo JSON mal formado")
        exit()

def mostrar_menu(consultas):
    print("\n=== MENÚ DE CONSULTAS ===")
    print("Consultas válidas (1-40):")
    for c in consultas[:40]:
        print(f"{c['id']:2}. {c['nombre']}")
    
    print("\nConsultas de error (41-50):")
    for c in consultas[40:]:
        print(f"{c['id']:2}. {c['nombre']}")
    
    print("\n 0. Salir")

def ejecutar_consulta(dsl_code):
    input_stream = InputStream(dsl_code)
    
    lexer = CSVFilterLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(CustomErrorListener())
    
    stream = CommonTokenStream(lexer)
    
    parser = CSVFilterParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())
    
    tree = parser.prog()
    visitor = MyCSVVisitor()
    visitor.visit(tree)

def main():
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], 'r') as f:
                dsl_code = f.read()
            print(f"\n▶ Ejecutando archivo: {sys.argv[1]}")
            ejecutar_consulta(dsl_code)
            return
        except FileNotFoundError:
            print(f"\n❌ Archivo no encontrado: {sys.argv[1]}")
            return
    
    consultas = cargar_consultas()
    
    while True:
        mostrar_menu(consultas)
        try:
            opcion = int(input("\nSeleccione una consulta (0 para salir): "))
            if opcion == 0:
                print("\n¡Hasta luego!")
                break
                
            consulta = next((c for c in consultas if c['id'] == opcion), None)
            
            if consulta:
                print(f"\n▶ Consulta {opcion}: {consulta['nombre']}")
                print(f"   Descripción: {consulta['descripcion']}")
                ejecutar_consulta(consulta['dsl'])
            else:
                print("\n❌ Opción no válida. Intente nuevamente.")
                
        except ValueError:
            print("\n❌ Entrada inválida. Debe ingresar un número.")

if __name__ == "__main__":
    main()