import streamlit as st
import string 


#st.set_page_config(layout="wide")
#st.image("https://img.freepik.com/free-vector/rafflesia-flower_9378-9.jpg?w=300")
st.title("Lexical Analyzer dan parser")
st.header("BAHASA BENGKULU")
st.header("Grammar")

col1, col2, col3 = st.columns(3)






    
alpha = list(string.ascii_lowercase)
state = ['q0','q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28','29']

transition = {}
for item1 in state:
      for item2 in alpha:
        transition[(item1, item2)] = 'error'
        transition[(item1, '#')] = 'error'
        transition[(item1, ' ')] = 'error'

transition['q0', ' '] = 'q0'

transition['q0', 'b'] = 'q1'
transition['q1', 'a'] = 'q2'
transition['q2', 'p'] = 'q3'
transition['q3', 'a'] = 'q4'
transition['q4', 'k'] = 'q5'

transition['q0', 'm'] = 'q6'
transition['q6', 'a'] = 'q7'
transition['q7', 'k'] = 'q5'


transition['q0', 'w'] = 'q8'
transition['q8', 'a'] = 'q5'

transition['q2', 'k'] = 'q9'
transition['q9', 's'] = 'q10'
transition['q10', 'o'] = 'q5'

transition['q0', 'a'] = 'q11'
transition['q11', 'y'] = 'q12'
transition['q12', 'a'] = 'q13'
transition['q13', 'm'] = 'q5'


transition['q0', 'o'] = 'q14'
transition['q14', 't'] = 'q15'
transition['q15', 'o'] = 'q5'


transition['q1', 'e'] = 'q16'
transition['q16', 'l'] = 'q17'
transition['q17', 'a'] = 'q18'
transition['q18', 'n'] = 'q19'
transition['q19', 'j'] = 'q20'
transition['q20', 'o'] = 'q5'

transition['q0', 'n'] = 'q21'
transition['q21', 'a'] = 'q22'
transition['q22', 'n'] = 'q23'
transition['q23', 'g'] = 'q24'
transition['q24', 'k'] = 'q25'
transition['q25', 'o'] = 'q26'
transition['q26', 'k'] = 'q5'

transition['q2', 'w'] = 'q27'
transition['q27', 'a'] = 'q28'
transition['q28', 'k'] = 'q5'

transition['q5', ' '] = 'q29'
transition['q5', '#'] = 'accept'
transition['q29', '#'] = 'accept'
transition['q29', ' '] = 'q29'

transition['q29', 'b'] = 'q1'
transition['q29', 'm'] = 'q6'
transition['q29', 'w'] = 'q8'
transition['q29', 'a'] = 'q11'


transition['q29', 'o'] = 'q14'
transition['q29', 'n'] = 'q21'

idx = 0
s = 'q0'
curToken = ''
n = 1
with col1:
    st.header("NOUN")
    st.write("Bapak")
    st.write("Mak")
    st.write("Wa")
    st.write("Bakso")
    st.write("Ayam")
    st.write("Oto")
with col2:
    st.header("VERB")
    st.write("Belanjo")
    st.write("Nangkok")
    st.write("Bawak")

with col3 :
    sentence = st.text_input("Masukkan Kata", "")
    sentence = sentence.lower()+'#'
    cek = st.button("cek hasil")

    while s != 'accept' and cek :
            now = sentence[idx]
            curToken += now
            s = transition[(s, now)]
            if s == 'q5' :
                    st.write("curtoken ",str(n),":",curToken,"Valid")
                    n = n + 1
                    curToken = ''

            if s == 'error' :
                    #st.write("error")
                    break
            idx+=1
st.header("LEXICAL ANALYZER")
if s == 'accept' and cek :
       st.success(f"Semua token di input  *'{sentence}'* Valid")
elif s == "error" and cek: 
       st.error(f'sentence **{sentence}** Tidak Diterima')