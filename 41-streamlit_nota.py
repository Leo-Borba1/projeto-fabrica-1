import streamlit as st
import nota as nt

st.title('MÉDIA')
st.caption('Veja sua média!   hehehe')
st.write('****')

with st.form('formulario_notas'):
    nota1 = st.number_input('nota1:',min_value=0.0,max_value=10.0)
    nota2 = st.number_input('nota2:',min_value=0.0,max_value=10.0)
    nota3 = st.number_input('nota3:',min_value=0.0,max_value=10.0)
    nota4 = st.number_input('nota4:',min_value=0.0,max_value=10.0)


    calcular = st.form_submit_button('Calcular a média')

    if calcular:
        valor_nota = nt.calcula_media(nota1, nota2, nota3, nota4)
        status = nt.tabela_nota(valor_nota)

        
        if status == "aprovado":
            st.success(f"{valor_nota:.2f}")
            st.write('**aprovado**')

        elif status == "recuperação":
            st.warning(f"{valor_nota:.2f}")
            st.write('**recuperação**')
            
        else:
            st.error(f"{valor_nota:.2f}")
            st.write('**Reprovado**')


with st.sidebar:
    st.subheader('Programas')