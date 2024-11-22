import streamlit as st
import sympy as sp
import numpy as np

def main():
    st.title("Análisis de Armaduras (Truss)")
    
    st.markdown("""
    ## Teoría de Armaduras
    
    Una armadura es una estructura compuesta por elementos rectos conectados en sus extremos 
    mediante juntas o nodos. Las armaduras son eficientes para soportar cargas y son ampliamente 
    utilizadas en puentes, techos y torres.
    
    ### Conceptos Principales:
    - Elementos a tracción y compresión
    - Análisis de nodos
    - Método de los nudos
    - Estabilidad estructural
    """)
    
    st.header("Ejemplo de Análisis de Armadura Simple")
    
    # Ejemplo interactivo de una armadura simple
    st.subheader("Armadura de 3 Barras")
    
    # Inputs interactivos
    F = st.slider("Carga Vertical (N)", 0, 1000, 500)
    L = st.slider("Longitud de la base (m)", 1, 5, 3)
    H = st.slider("Altura (m)", 1, 5, 2)
    
    # Cálculos
    theta = np.arctan(H/L)
    R1 = F/2  # Reacción en apoyo izquierdo
    R2 = F/2  # Reacción en apoyo derecho
    
    # Fuerzas en las barras
    F_diagonal = F/(2*np.sin(theta))
    F_horizontal = F_diagonal*np.cos(theta)
    
    # Mostrar resultados
    st.write("### Resultados")
    st.write(f"Fuerza en barra diagonal: {F_diagonal:.2f} N")
    st.write(f"Fuerza en barra horizontal: {F_horizontal:.2f} N")
    st.write(f"Reacciones en los apoyos: {R1:.2f} N")

if __name__ == "__main__":
    main()
