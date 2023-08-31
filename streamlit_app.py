import streamlit
import pandas

streamlit.title('First App Title')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣   Omaga 3')
streamlit.text('🥗 Kale')
streamlit.text('🐔 Hard boiled egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
