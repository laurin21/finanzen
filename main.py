import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np
import time

st.title("Finanzen")

# path = "/home/lb21/Server/Mac/finanzen.xlsx"
path = "/Users/laurin/Library/CloudStorage/GoogleDrive-laurin@biermann-home.de/Meine Ablage/Mac/finanzen.xlsx"

aus = pd.read_excel(path, sheet_name = "Ausgaben")
ein = pd.read_excel(path, sheet_name = "Einnahmen")


aus["Datum"] = pd.to_datetime(aus["Datum"], format = "%d.%m.%Y", errors = "coerce")
ein["Datum"] = pd.to_datetime(ein["Datum"], format = "%d.%m.%Y", errors = "coerce")


aus_months = aus.groupby(aus.Datum.dt.month)["Betrag"].sum()
aus_cat = aus.groupby("Kategorie")["Betrag"].sum()
ein_months = aus.groupby(aus.Datum.dt.month)["Betrag"].sum()
ein_cat = ein.groupby("Kategorie")["Betrag"].sum()

start = st.slider("Start", min_value = 1, max_value = 12, value = 1)
end = st.slider("End", min_value = 1, max_value = 12, value = 12)

st.line_chart(aus_months[start:end])
st.line_chart(ein_months)

aus_categories = ["Einkauf", "Essen", "Uni", "Luna", "Verschiedenes", "Freizeit", "Menschen", "Transport", "Urlaub", "Sport", "Kleidung", "Wohnung"]

aus_cat_selection = st.selectbox("Ausgaben Kategorie", options = aus_categories)

aus_selected = aus[aus["Kategorie"] == aus_cat_selection]

sum_aus_selected = aus_selected["Betrag"].sum()

st.write(sum_aus_selected)
st.write(aus_selected)

st.write(aus)
st.write(aus_months)
st.write(ein)
st.write(ein_months)
