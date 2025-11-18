import streamlit as st
from pymongo import MongoClient
import datetime

# ------------------------------
# MongoDB Connection
# ------------------------------
MONGO_URI = "mongodb+srv://SDMHUB_DB:SDM123456@sdmhub.anngz6n.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client["studentDB"]
collection = db["registrations"]

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(page_title="SDMHUB Registration", page_icon="🎓", layout="centered")

# ------------------------------
# Custom CSS
# ------------------------------
st.markdown("""
    <style>
        .title-text {
            font-size: 36px;
            font-weight: 700;
            color: #4CAF50;
            text-align: center;
        }
        .sub-text {
            font-size: 18px;
            text-align: center;
            color: #555;
            margin-bottom: 20px;
        }
        .card {
            background-color: #ffffff;
            padding: 35px;
            border-radius: 15px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
            width: 420px;
            margin: auto;
        }
        /* FORCE button to center */
        div.stButton > button {
            width: 60%;
            margin-left: 20% !important;
            margin-right: 20% !important;
            background-color: #4CAF50 !important;
            color: white !important;
            font-size: 20px !important;
            padding: 12px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------------------
# Title
# ------------------------------
st.markdown("<div class='title-text'>🎓 SDMHUB Student Registration</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-text'>Enter your details below to complete the registration.</div>", unsafe_allow_html=True)

# ------------------------------
# Registration Form
# ------------------------------
with st.container():

    with st.form("registration_form"):
        name = st.text_input("👤 Full Name")
        usn = st.text_input("🎓 USN")
        email = st.text_input("📧 College Registered Email")

        submit = st.form_submit_button("Submit")

    st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------
# Handle Submission
# ------------------------------
if submit:
    if name and usn and email:
        data = {
            "name": name,
            "usn": usn,
            "email": email,
            "submitted_at": datetime.datetime.now()
        }
        collection.insert_one(data)

        st.success("🎉 Registration successful!")
        st.balloons()
    else:
        st.error("⚠️ Please fill all fields correctly.")
