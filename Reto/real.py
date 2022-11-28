import time  # to simulate a real time data, time loop
from lectura import *
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import matplotlib.pyplot as plt
import streamlit as st  # 🎈 data web app development
from scipy.signal import lfilter
import keyboard
from datetime import datetime
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

def get_data():
    rows = lect()
    return rows

# dashboard title
st.title("Real-Time / Live Data Science Dashboard")

# creating a single-element container
placeholder = st.empty()

data=160000
ini=1
fin=1
n=30
b=[1.0/n]*n
a=1
# near real-time / live feed simulation

while True:
    df=pd.DataFrame(get_data(), columns=['id', 'timeStamp','vibracion'])
    df['corriente'] = np.random.randint(-5, 5, df.shape[0])
    df['rpm'] = np.random.randint(-5, 5, df.shape[0])
    df['Date'] = pd.to_datetime(df['timeStamp']).dt.date
    df['hours'] = pd.to_datetime(df['timeStamp']).dt.hour
    df['minutes']= pd.to_datetime(df['timeStamp']).dt.minute
    df['seconds']=pd.to_datetime(df['timeStamp']).dt.second
    # creating KPIsS

    with placeholder.container():

        date1=min(df['Date'])
        date2=max(df['Date'])
        
        if ini==1:
            datei=date1
            datef=date2
        else:
            datei=sel1
            datef=sel2
            
        sel1 = st.date_input(
            "Fecha inical",
            datei,min_value=date1,max_value=date2,key=('inicial'+str(ini)))
        sel2 = st.date_input(
            "Fecha final",
            datef,min_value=date1,max_value=date2,key=('fianl'+str(ini)))
        
        if sel1==sel2:
            df1=df[df['Date'] == sel1]
        else:
            df1=df[(df['Date'] >= sel1) & (df['Date'] <= sel2)]
        
        avg_curr = round(np.mean(df1["corriente"]),3)

        avg_vibracion =round(np.mean(df1['vibracion']),3)

        avg_rpm = round(np.mean(df1["rpm"]),3)
            # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

            # fill in those three columns with respective metrics or KPIs
        kpi1.metric(
                label="Corriente ⚡",
                value=avg_curr,
            )
            
        kpi2.metric(
                label="Vibracion 🔉",
                value=avg_vibracion,
            )
            
        kpi3.metric(
                label="RPM 🔁​",
                value=avg_rpm,
            )

            # create three columns for charts
        fig_col1, fig_col2, fig_col3 = st.columns(3)
        with fig_col1:
            st.markdown("### Corriente")
            df_corriente=df1["corriente"]
            df_corriente=df_corriente.tail(data)
            yy=lfilter(b,a,df_corriente)
            fig, ax = plt.subplots()
            ax.plot(yy)
            ax.set_ylim(-6, 6) 
            st.pyplot(fig)
            
        with fig_col2:
            st.markdown("### Vibración")
            df_vibracion=df1["vibracion"]
            df_vibracion=df_vibracion.tail(data)
            yy=lfilter(b,a,df_vibracion)
            fig, ax = plt.subplots()
            ax.plot(yy)
            ax.set_ylim(-6, 6) 
            st.pyplot(fig)
            
        with fig_col3:
            st.markdown("### RPM")
            df_rpm=df1["rpm"]
            df_rpm=df_rpm.tail(data)
            yy=lfilter(b,a,df_rpm)
            fig, ax = plt.subplots()
            ax.plot(yy)
            ax.set_ylim(-6, 6) 
            st.pyplot(fig)
        st.markdown("### Datos completos")    
        st.dataframe(df1[['timeStamp','vibracion','corriente','rpm']],height=600, use_container_width=True)
        ini=ini+1
        fin=fin+1
        
        time.sleep(10)
        
        if keyboard.is_pressed("q"):
            print("q pressed, ending loop")
            plt.pyplot.close('all')
            break
