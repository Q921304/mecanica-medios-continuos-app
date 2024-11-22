# Aplicación de Mecánica de Medios Continuos

Esta aplicación web, desarrollada con Streamlit y SymPy, proporciona una interfaz interactiva para explorar conceptos de Mecánica de Medios Continuos, específicamente en las áreas de Beam (Vigas), Truss (Armaduras) y Cable.

## Estructura del Proyecto

```
.
├── streamlit_app.py
├── pages/
│   ├── 1_beam.py
│   ├── 2_truss.py
│   └── 3_cable.py
├── requirements.txt
└── README.md
```

## Instalación

1. Clonar el repositorio:
```bash
git clone [URL-del-repositorio]
```

2. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecutar la aplicación:
```bash
streamlit run streamlit_app.py
```

## Características

- **Página Principal**: Introducción a la Mecánica de Medios Continuos
- **Beam**: Análisis de vigas con cálculos interactivos
- **Truss**: Simulación de armaduras y análisis estructural
- **Cable**: Estudio de sistemas de cables y catenarias

## Tecnologías Utilizadas

- Python
- Streamlit
- SymPy
- NumPy
- Matplotlib

## Contribuir

1. Fork el repositorio
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request
