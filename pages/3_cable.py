import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def calculate_cable_curve(span, sag, num_points=100):
    """
    Calcula la curva del cable usando la ecuación de la parábola
    """
    x = np.linspace(0, span, num_points)
    # Ecuación parabólica simplificada para el cable
    y = -4 * sag * (x/span) * (x/span - 1)
    return x, y

def calculate_tension(weight_per_unit, span, sag):
    """
    Calcula la tensión aproximada en el cable
    """
    # Tensión horizontal aproximada
    H = weight_per_unit * span**2 / (8 * sag)
    # Tensión máxima en los soportes
    T_max = H * np.sqrt(1 + (4 * sag / span)**2)
    return H, T_max

def main():
    st.title("Análisis de Cables")
    
    st.markdown("""
    ## Teoría de Cables
    
    Los cables son elementos estructurales flexibles que trabajan únicamente a tracción. 
    Son ampliamente utilizados en:
    - Puentes colgantes
    - Líneas de transmisión
    - Sistemas de anclaje
    - Teleféricos
    
    ### Conceptos Principales:
    - Catenaria y aproximación parabólica
    - Tensión axial
    - Deflexión
    - Cargas distribuidas
    """)
    
    st.header("Simulación de Cable Colgante")
    
    # Parámetros interactivos
    col1, col2 = st.columns(2)
    with col1:
        span = st.slider("Longitud del cable (m)", 10, 100, 50)
        sag = st.slider("Flecha máxima (m)", 1, 20, 5)
    
    with col2:
        weight = st.slider("Peso por unidad de longitud (N/m)", 10, 1000, 100)
    
    # Calcular la curva del cable
    x, y = calculate_cable_curve(span, sag)
    
    # Calcular tensiones
    H, T_max = calculate_tension(weight, span, sag)
    
    # Crear gráfica
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, 'b-', linewidth=2)
    ax.grid(True)
    ax.set_xlabel('Distancia horizontal (m)')
    ax.set_ylabel('Altura (m)')
    ax.set_title('Perfil del Cable')
    
    # Ajustar los límites y aspecto de la gráfica
    ax.set_xlim(-span*0.1, span*1.1)
    ax.set_ylim(-sag*1.2, sag*0.2)
    ax.axis('equal')
    
    # Mostrar la gráfica en Streamlit
    st.pyplot(fig)
    
    # Mostrar resultados
    st.subheader("Resultados del Análisis")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Tensión Horizontal", f"{H/1000:.2f} kN")
    with col2:
        st.metric("Tensión Máxima", f"{T_max/1000:.2f} kN")
    
    st.markdown("""
    ### Notas:
    - La tensión horizontal es constante a lo largo del cable
    - La tensión máxima ocurre en los puntos de soporte
    - El análisis asume una carga uniformemente distribuida
    - Se utiliza una aproximación parabólica para la forma del cable
    """)
    
    # Añadir explicaciones teóricas
    with st.expander("Ver más detalles teóricos"):
        st.markdown("""
        #### Ecuaciones Fundamentales:
        
        1. **Ecuación de la parábola:**
           - y = -4h(x/L)(x/L-1)
           donde:
           - h es la flecha máxima
           - L es la longitud del vano
           
        2. **Tensión horizontal:**
           - H = wL²/8h
           donde:
           - w es el peso por unidad de longitud
           - L es la longitud del vano
           - h es la flecha máxima
           
        3. **Tensión máxima:**
           - Tmax = H√(1 + (4h/L)²)
        """)

if __name__ == "__main__":
    main()
