import streamlit as st
import sympy as sp

def main():
    st.title("Mecánica de Medios Continuos")
    
    st.markdown("""
    # Bienvenido a la Aplicación de Mecánica de Medios Continuos
    
    Esta aplicación está diseñada para ayudar a entender y visualizar conceptos fundamentales 
    de la Mecánica de Medios Continuos, específicamente enfocándose en tres áreas principales:
    
    1. **Beam (Vigas)**: Análisis de deformación y esfuerzos en vigas
    2. **Truss (Armaduras)**: Estudio de estructuras compuestas por elementos rectos
    3. **Cable**: Análisis de cables y sus comportamientos
    
    ## ¿Qué es la Mecánica de Medios Continuos?
    
    La Mecánica de Medios Continuos es una rama de la física que se ocupa del análisis del 
    comportamiento cinemático y mecánico de los materiales modelados como un medio continuo. 
    Esta disciplina es fundamental en ingeniería civil y mecánica, ya que proporciona las bases 
    teóricas para el análisis de estructuras y materiales.
    
    ### Aspectos principales:
    
    - Estudio de deformaciones y tensiones
    - Análisis de comportamiento elástico y plástico
    - Modelado de estructuras complejas
    - Predicción de fallos y comportamiento estructural
    
    ## Navegación
    
    Utilice la barra lateral para navegar entre las diferentes secciones de la aplicación:
    
    - **Beam**: Análisis y cálculos relacionados con vigas
    - **Truss**: Estudio de sistemas de armaduras
    - **Cable**: Análisis de sistemas de cables
    """)

if __name__ == "__main__":
    main()
