import streamlit as st

st.set_page_config(page_title="Abdullah Profile", layout="centered")

# Profile Data
profile = {
    "name": "Abdullah Bin Fahad",
    "dob": "14 August 2006",
    "height": "166 cm",
    "weight": "57.1 kg",
    "blood": "A+",
    "university": "Nanjing Tech University",
    "major": "Automation",
    "goal": "Become Billionaire & Build AI Systems"
}

# UI
st.markdown(
    """
    <style>
    .card {
        background: rgba(255,255,255,0.08);
        padding: 30px;
        border-radius: 20px;
        backdrop-filter: blur(10px);
        text-align: center;
        box-shadow: 0 0 30px rgba(0,0,0,0.3);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="card">', unsafe_allow_html=True)

st.title(profile["name"])
st.caption("Future Builder • Automation Student")

st.write(f"**DOB:** {profile['dob']}")
st.write(f"**Height:** {profile['height']}")
st.write(f"**Weight:** {profile['weight']}")
st.write(f"**Blood Group:** {profile['blood']}")

st.subheader("Education")
st.write(profile["university"])
st.write(profile["major"])

st.subheader("Goal")
st.write(profile["goal"])

st.markdown('</div>', unsafe_allow_html=True)
