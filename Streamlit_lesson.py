import streamlit as st
import pandas as pd

df = pd.read_csv("Berlin_crimes.csv").head(10)
column = df.columns
st.title("Hello Streamlit-er 👋")
st.markdown(
    """ 
    This is a playground for you to try Streamlit and have fun. 

    **There's :rainbow[so much] you can build!**
    
    We prepared a few examples for you to get started. Just 
    click on the buttons above and discover what you can do 
    with Streamlit. 
    """
)

if st.button("Send balloons!"):
    st.balloons()
    column = "Year"
    # st.table(df)

st.table(df[column])

# st.text(column)

st.bar_chart(df, x="Location", y="Robbery")

# print(df.head(10))
# st.line_chart(df)
