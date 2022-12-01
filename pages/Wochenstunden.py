import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np
import time
import gspread

sa = gspread.service_account("service_account.json")
sh = sa.open("wochenstunden")

df = sh.worksheet("Tabelle1")
df = pd.DataFrame(df.get_all_records())

df["Stunden"] = df["Stunden"].map(float)
df["Stunden"] = df["Stunden"].div(100)

st.title("Wochenstunden")

avg_lst = []

for i in range(len(df["Stunden"])):
	current_avg = (df["Stunden"][:i].sum()/i)
	avg_lst.append(current_avg)

df["Average"] = avg_lst

st.line_chart(df[["Stunden", "Average"]])


average = avg_lst[-1]
average_money = (average * 14) - (average * 14 * 0.036)
st.write(f"Durchschnittlicher Verdienst pro Monat: {average_money}")
