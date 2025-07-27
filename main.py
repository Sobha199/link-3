import streamlit as st
import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe, get_as_dataframe
from PIL import Image

# Load logo
st.image("s2m-logo.png", width=150)

# Google Sheets auth
gc = gspread.service_account_from_dict(st.secrets["gspread"])
sh = gc.open("S2M_Production_Data")
worksheet = sh.sheet1

# Login CSV
login_df = pd.read_csv("login coder.csv")

# Login Logic
username = st.text_input("Username")
password = st.text_input("Password", type="password")
if st.button("Login"):
    if (login_df["Username"] == username).any():
        role = login_df.loc[login_df["Username"] == username, "Role"].values[0]
        st.success(f"Logged in as {role}")
        if role.lower() == "coder":
            st.subheader("Coder Form")
            # Form inputs here
        elif role.lower() == "admin":
            st.subheader("Admin Panel")
            df = get_as_dataframe(worksheet).dropna(how="all")
            st.dataframe(df)
    else:
        st.error("Invalid credentials")