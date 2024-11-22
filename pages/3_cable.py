import streamlit as st
import sympy as sp
from sympy.physics.continuum_mechanics.cable import Cable

def main():
    st.title("Análisis de Cables")
    
    st.markdown("""
    ## Teoría de Cables
    
    Los cables son elementos estructurales flexibles que trabajan únicamente a tracción. 
    Son ampliamente utilizados en puentes colgantes, líneas de transmisión y sistemas de anclaje.
    
    ### Conceptos Principales:
    - Catenaria
    - Tensión axial
    - Deflexión
    - Cargas distribuidas
    """)
    
    st.header("Ejemplo de Cable Colgante")
    
    # Variables interactivas
    length = st.slider("Longitud del cable (m)", 10, 50, 20)
    load = st.slider("Carga distribuida (N/m)", 0, 1000, 500)
    
    # Crear instancia de Cable
    cable = Cable(length)
    
    # Aplicar carga distribuida
    cable.apply_load(load, 0, length)
    
    # Mostrar ecuaciones
    st.subheader("Ecuaciones del Cable")
    st.write("Ecuación de la forma del cable:")
    st.latex(str(cable.slope()))
    
    # Cálculos adicionales
    max_tension = load * length / 2
    st.write(f"Tensión máxima en el cable: {max_tension:.2f} N")

if __name__ == "__main__":
    main()
