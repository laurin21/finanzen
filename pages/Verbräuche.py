import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np
import time
import gspread

sa = gspread.service_account("service_account.json")
sh = sa.open("verbraeuche_wg")

strom = sh.worksheet("Strom")
strom = pd.DataFrame(aus.get_all_records())

gas = sh.worksheet("Ausgaben")
gas = pd.DataFrame(ein.get_all_records())


st.title("Vebräuche WG")

st.write(gas)
