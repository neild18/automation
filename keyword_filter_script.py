import streamlit as st 
import pandas as pd
import re
import base64
import io
import time

def main():
	st.text('Filter out all the irrelevant keywords from your downloads from your favourite keyword research tools!')
	st.subheader('What does this tool do?')
	st.text('1\. It will add new columns for \'Intent\', \'Games\',  and for gaming related \'Modifiers\'.')
	st.text('2\. It will create a column called \'Filter\' with Positive or Negative values. Positive being relevant keywords and Negative being irrelevant keywords.')
	st.warning('Make sure that the CSV contains a column titled \'keyword\'.')
	st.text('Once uploaded, go grab a brew (preferably something soft) while the file is being processed.')
	
	uploaded_file = st.file_uploader("Choose a file")
	
	if uploaded_file is not None:
		path = str(uploaded_file)

		def read_file(path):
			csv = re.search(r'csv$', path)
			excel = re.search(r'xlsx$', path)
			if excel:
				return pd.read_excel(path)
			elif csv: 
				return pd.read_csv(path)

		df = read_file(path)
		st.write(df)
		


		

if __name__ == '__main__':
	main()

		
