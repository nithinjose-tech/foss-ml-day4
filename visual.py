#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
#matplotlib.use('Agg')
import seaborn as sns 
#Remove Warnings
st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("ForestFire_Dataset")

#import dataset
df = pd.read_csv('forestfires.csv')
#First thirty rows
tips = df.head(20)

#Display the table
st.table(tips)
#max
tempmax=np.max(tips['temp'])
st.write('Maximum Temperature is :', tempmax)

#during september
er=df[df['month']=='sep']
st.subheader("During September")
st.table(er.head(20))
st.header("Visualisation Using Seaborn")
#bar plot
st.subheader("Bar Plot")
tips.plot(kind='bar')
st.pyplot()

#Displot
st.subheader("Displot")
sns.displot(tips['day'])
st.pyplot()

#joinplot
st.subheader("JointPlot")
sns.jointplot(x='month',y='temp',data=tips,kind='scatter')
st.pyplot()
#Rugplot
st.subheader("Rugplot")
sns.rugplot(tips['temp'])
st.pyplot()
#Correation
st.subheader("Heatmap")
sns.heatmap(tips.corr(),cmap='coolwarm',annot=True)
st.pyplot()