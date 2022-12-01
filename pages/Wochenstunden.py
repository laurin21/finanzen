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

avg_lst = []

for i in range(len(df["Stunden"])):
	current_avg = (df["Stunden"][:i].sum()/i)
	avg_lst.append(current_avg)

df["Average"] = avg_lst

average = avg_lst[-1]
average_money = round(((average * 14) - (average * 14 * 0.036)) * 4.33, 3)

avg_soll = 7.42
delta = round(average - avg_soll, 3)

st.title("Wochenstunden")

sum_h = df["Stunden"].sum()

rente = round(sum_h * 14 * 0.036, 3)


####

st.line_chart(df[["Stunden", "Average"]])

st.write(f"Durchschnittlicher Verdienst pro Monat: {average_money}€")

st.write(f"Delta zum Mindestdurchschnitt: {delta}h")

st.write(f"Durchschnittliche Stundenanzahl pro Woche: {average}h")

st.write(f"Stunden insgesamt: {sum_h}h")

st.write(f"Eingezahlt in Rentenkasse: {rente}€")
