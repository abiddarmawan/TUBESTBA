import streamlit as st
import string 


st.set_page_config(layout="wide")
st.title("Lexical Analyzer")


col1, col2, col3 = st.columns(3)


with col2:
    st.header("NOUN")
    st.write("Bapak")
    st.write("Mak")
    st.write("Wa")
    st.write("Bakso")
    st.write("Ayam")
    st.write("Oto")
with col3:
    st.header("VERB")
    st.write("Belanjo")
    st.write("Nangkok")
    st.write("Bawak")
with col1 : 
        st.image("https://img.freepik.com/free-vector/rafflesia-flower_9378-9.jpg?w=740")

    
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
 
sentence = st.text_input("Masukkan Kata", "")
sentence = sentence.lower()+'#'
cek = st.button("cek hasil")

while s != 'accept' :
        now = sentence[idx]
        curToken += now
        s = transition[(s, now)]
        if s == 'q5' :
                st.write("curtoken :",curToken,"Valid")
                curToken = ''

        if s == 'error' :
                st.write("error")
                break
        idx+=1
if s == 'accept' :
       st.success(f"Semua token di input  *'{sentence}'* Valid")
else : 
       st.error(f'sentence **{sentence}** Tidak Diterima')
        
#parse 

token = sentence.lower().split()
token[len(token) - 1] = token[len(token) - 1][:len(token[len(token) - 1]) - 1]

print(token)
token.append('EOS')

non_terminal = ['S', 'NN', 'VB']
terminal = ['bapak', 'mak', 'wa', 'bakso', 'ayam', 'oto', 'belanjo', 'nangkok', 'bawak']

parse_table = {}

parse_table[('S', 'bapak')] = ['NN', 'VB', 'NN']
parse_table[('S', 'mak')] = ['NN', 'VB', 'NN']
parse_table[('S', 'wa')] = ['NN', 'VB', 'NN']
parse_table[('S', 'bakso')] = ['NN', 'VB', 'NN']
parse_table[('S', 'ayam')] = ['NN', 'VB', 'NN']
parse_table[('S', 'oto')] = ['NN', 'VB', 'NN']
parse_table[('S', 'belanjo')] = ['error']
parse_table[('S', 'nangkok')] = ['error']
parse_table[('S', 'bawak')] = ['error']
parse_table[('S', 'EOS')] = ['error']

parse_table[('NN', 'bapak')] = ['bapak']
parse_table[('NN', 'mak')] = ['mak']
parse_table[('NN', 'wa')] = ['wa']
parse_table[('NN', 'bakso')] = ['bakso']
parse_table[('NN', 'ayam')] = ['ayam']
parse_table[('NN', 'oto')] = ['oto']
parse_table[('NN', 'belanjo')] = ['error']
parse_table[('NN', 'nangkok')] = ['error']
parse_table[('NN', 'bawak')] = ['error']
parse_table[('NN', 'EOS')] = ['error']

parse_table[('VB', 'bapak')] = ['error']
parse_table[('VB', 'mak')] = ['error']
parse_table[('VB', 'wa')] = ['error']
parse_table[('VB', 'bakso')] = ['error']
parse_table[('VB', 'ayam')] = ['error']
parse_table[('VB', 'oto')] = ['error']
parse_table[('VB', 'belanjo')] = ['belanjo']
parse_table[('VB', 'nangkok')] = ['nangkok']
parse_table[('VB', 'bawak')] = ['bawak']
parse_table[('VB', 'EOS')] = ['error']

stack = []
stack.append('#')
stack.append('S')

idx_token = 0
symbol = token[idx_token]

while len(stack) > 0 :
  top = stack[len(stack) - 1]
  #st.write('top = ', top)
  #print('symbol = ', symbol)
  if top in terminal :
    #st.write('top adalah simbol terminal')
    if top == symbol :
      stack.pop()
      idx_token += 1
      symbol = token[idx_token]
      if symbol == 'EOS' :
        #st.write('isi stack = ', stack)
        stack.pop()
    else :
        #st.write('error')
        break
  elif top in non_terminal :
    #st.write('top adalah simbol non terminal')
    if parse_table[(top, symbol)][0] != 'error' :
      stack.pop()
      symbol_push = parse_table[(top, symbol)]
      for i in range(len(symbol_push)-1, -1, -1) :
        stack.append(symbol_push[i])
    else : 
      #st.write('error')
      break
  else :
    #write('error')
    break
  #st.write('isi stack = ', stack, end='\n\n')

if symbol == 'EOS' and len(stack) == 0 :
  st.success(f"input string :  *'{sentence}'* Valid")
else :
  st.success(f"error,input string *'{sentence}'* tidak diterima,tidak sesuai grammar")




    

