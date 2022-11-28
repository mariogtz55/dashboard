import streamlit as st  # 🎈 data web app development
from lectura import lect
import pandas as pd
import time
st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)
def get_data() :
    return lect()

rows = get_data()
df=pd.DataFrame(rows, columns=['id', 'timeStamp','current'])
st.dataframe(df)
df_corriente=df["current"]
st.line_chart(df_corriente)
time.sleep(100)
st.experimental_rerun()
