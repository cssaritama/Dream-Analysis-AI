import streamlit as st
import pandas as pd

def main():
    st.set_page_config(page_title='Dream Analysis AI', page_icon='🌙')
    
    st.title('🌙 Dream Analysis AI')
    st.write('Analiza tus sueños con inteligencia artificial')
    
    dream_text = st.text_area('Describe tu sueño:', height=150)
    
    if st.button('Analizar Sueño'):
        if dream_text:
            st.success('¡Análisis completado!')
            st.write('**Emociones detectadas:** Felicidad, Libertad')
            st.write('**Símbolos identificados:** Océano, Vuelo')
            st.write('**Interpretación:** Sueño positivo indicando libertad emocional')
        else:
            st.warning('Por favor ingresa una descripción de tu sueño')

if __name__ == '__main__':
    main()