import streamlit as st

st.title('Hello World')
st.write('this is a simple Streamlit app.')
if st.button('Say Hello'):
		st.text('Hello streamlit')
		
name=st.text_input ('Please Enter Your Name :')

f name:
	st.write(f'Hello,{name}!')
	
	if st.file_uploder('Please upload a file : ',type=['txt','cvs']):
	st.write('Thanks for uploading a file')
