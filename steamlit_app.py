import streamlit

streamlit.title("My Parents' New Healthy Dinner")

streamlit.header("🥣 Breakfast Menu")
streamlit.text("🥗 Omega 3 and Blueberry Oatmeal")
streamlit.text("🐔 Kale, Spinach and Rocket Smoothie")
streamlit.text("🥑🍞 Hard-Boiled Free Range Egg")

streamlit.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(my_fruit_list)
