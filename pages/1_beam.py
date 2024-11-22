import streamlit as st
import sympy as sp
from sympy.physics.continuum_mechanics.beam import Beam
from sympy import symbols

def main():
    st.title("Análisis de Vigas (Beam)")
    
    st.markdown("""
    ## Teoría de Vigas
    
    Una viga es un elemento estructural diseñado para soportar cargas principalmente mediante flexión. 
    Las vigas son fundamentales en la construcción y se utilizan en diversos tipos de estructuras.
    
    ### Conceptos Principales:
    - Momento flector
    - Fuerza cortante
    - Deflexión
    - Condiciones de apoyo
    """)
    
    st.header("Ejemplo Práctico")
    
    # Variables simbólicas
    E, I = symbols('E I')
    b = Beam(4, E, I)
    
    # Ejemplo interactivo
    st.subheader("Viga Simple con Carga Puntual")
    load_magnitude = st.slider("Magnitud de la carga (N)", 0, 1000, 500)
    load_position = st.slider("Posición de la carga (m)", 0.0, 4.0, 2.0)
    
    # Aplicar carga y condiciones de apoyo
    b.apply_load(load_magnitude, load_position, -1)
    b.bc_deflection = [(0, 0), (4, 0)]
    
    # Mostrar resultados
    st.write("### Resultados")
    st.write("Ecuación del momento flector:")
    st.latex(str(b.bending_moment()))
    st.write("Ecuación de la deflexión:")
    st.latex(str(b.deflection()))

if __name__ == "__main__":
    main()
