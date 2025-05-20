import json
import sys
import os
import subprocess
from antlr4 import *
from antlr4.tree.Trees import Trees
from CSVFilterLexer import CSVFilterLexer
from CSVFilterParser import CSVFilterParser
from MyCSVVisitor import MyCSVVisitor, CSVProcessingError
from CustomErrorListener import CustomErrorListener

def generar_parse_tree_consulta(dsl_code, consulta_id):
    """Genera y muestra el Parse Tree para una consulta específica"""
    try:
        # Crear archivo temporal con el código DSL
        filename = f"consulta_{consulta_id}.dsl"
        with open(filename, 'w') as f:
            f.write(dsl_code)
        
        # Generar árbol gráfico en segundo plano
        if sys.platform == "win32":
            subprocess.Popen(
                ['cmd', '/c', f'antlr4-parse CSVFilter.g4 prog -gui {filename}'],
                creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NO_WINDOW,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        else:
            subprocess.Popen(
                ['antlr4-parse', 'CSVFilter.g4', 'prog', '-gui', filename],
                start_new_session=True
            )
        
        # Generar versión texto del árbol
        input_stream = InputStream(dsl_code)
        lexer = CSVFilterLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CSVFilterParser(stream)
        tree = parser.prog()
        
        print("\n" + "═"*60)
        print(f"🌳 PARSE TREE - CONSULTA {consulta_id}")
        print("═"*60)
        print(Trees.toStringTree(tree, None, parser))
        print("═"*60 + "\n")
        
        # Limpiar archivo temporal después de 2 segundos
        subprocess.Popen(f'sleep 2 && rm {filename}' if sys.platform != "win32" 
                        else f'timeout 2 & del {filename}', shell=True)
        
    except Exception as e:
        print(f"\n⚠️ Error generando árbol: {str(e)}")

def cargar_consultas():
    """Carga las consultas desde el archivo JSON"""
    try:
        with open('consultas.json', 'r', encoding='utf-8') as f:
            return json.load(f)['consultas']
    except Exception as e:
        print(f"\n❌ Error cargando consultas: {str(e)}")
        exit()

def mostrar_menu(consultas):
    """Muestra el menú interactivo de consultas"""
    print("\n=== MENÚ PRINCIPAL ===")
    print("Consultas válidas (1-40):")
    for c in consultas[:40]:
        print(f"{c['id']:2}. {c['nombre']}")
    
    print("\nConsultas de error (41-50):")
    for c in consultas[40:]:
        print(f"{c['id']:2}. {c['nombre']}")
    
    print("\n 0. Salir")

def ejecutar_consulta(dsl_code, consulta_id):
    """Ejecuta un script DSL y muestra su Parse Tree"""
    try:
        # Mostrar Parse Tree
        generar_parse_tree_consulta(dsl_code, consulta_id)
        
        # Ejecutar consulta
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
        
    except Exception as e:
        print(f"\n❌ Error durante la ejecución: {str(e)}")

def main():
    # Configuración inicial
    consultas = cargar_consultas()
    
    while True:
        try:
            mostrar_menu(consultas)
            opcion = input("\nSeleccione una consulta (0 para salir): ").strip()
            
            if not opcion.isdigit():
                print("\n❌ Entrada inválida. Debe ser un número.")
                continue
                
            opcion = int(opcion)
            
            if opcion == 0:
                print("\n¡Hasta luego! 👋")
                break
                
            consulta = next((c for c in consultas if c['id'] == opcion), None)
            
            if consulta:
                print(f"\n▶ Consulta {opcion}: {consulta['nombre']}")
                print(f"   Descripción: {consulta['descripcion']}")
                ejecutar_consulta(consulta['dsl'], opcion)
            else:
                print("\n❌ Opción no válida. Intente nuevamente.")
                
        except KeyboardInterrupt:
            print("\n\nOperación cancelada por el usuario. 🚫")
            break
        except Exception as e:
            print(f"\n❌ Error inesperado: {str(e)}")

if __name__ == "__main__":
    main()