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

st.write(df)

st.line_chart(df["Stunden"])
