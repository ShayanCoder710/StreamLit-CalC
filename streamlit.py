import streamlit as st

st.markdown("""
            
<style>
            
    .stTextInput > div > div > input {
        padding: 15px 30px;
        border: 4px solid black;
        border-radius: 10px;
        font-size: 18px;
        text-align: center;
    }

    .stButton > button {
        margin: 10px auto;
        background-color: #4CAF50;
        color: white;
        font-size: 20px;
        padding: 10px 20px;
        border: 4px solid black;
        border-radius: 15px;
    }

</style>
            
""", unsafe_allow_html=True)



st.set_page_config(
    page_title="CalC",
    layout="centered"
)



st.title("CalC")

phrase = st.text_input("Enter the mathematical phrase:")

ac = set("0123456789+-*/() .")


if st.button("🔲Calculate🔲"):

    if all(char in ac for char in phrase):

        result = eval(phrase)

        st.success(f"Result: **{result}**")


    else:
        st.error("Invalid phrase ! Only numbers and operators [() , * , / , + , -] are allowed. Example: 10 + 20 * 10 / 5")