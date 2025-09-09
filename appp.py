import streamlit as st
import random
import time

# --------------------------
# CONFIG
# --------------------------
APP_TITLE = "Pravisha's Portal 💕"
SITE_PASSWORD = "loveyou"  # change this password if you want

# --------------------------
# PAGE SETUP
# --------------------------
st.set_page_config(page_title=APP_TITLE, layout="centered")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# --------------------------
# CSS for romantic effects
# --------------------------
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #ffdde1 0%, #ee9ca7 100%);
    background-size: cover;
}

h1, h2, h3, h4, h5, h6, label, .css-16huue1, .css-10trblm {
    font-family: "Comic Sans MS", cursive, sans-serif !important;
    color: #d63384 !important;
}

button[kind="secondary"] {
    background-color: #ffb6c1 !important;
    color: #fff !important;
    border-radius: 20px !important;
    border: none !important;
}

button[kind="primary"] {
    background-color: #ff69b4 !important;
    color: white !important;
    border-radius: 20px !important;
    border: none !important;
}

.heart {
    position: fixed;
    font-size: 30px;
    animation: floatUp 3s linear forwards;
}

@keyframes floatUp {
    from { transform: translateY(0); opacity: 1; }
    to { transform: translateY(-200px); opacity: 0; }
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --------------------------
# LOGIN
# --------------------------
st.title(APP_TITLE)

if not st.session_state.authenticated:
    pw = st.text_input("Enter our secret password:", type="password")
    if pw == SITE_PASSWORD:
        st.session_state.authenticated = True
        st.success("Password accepted — welcome to your portal, Pravisha! 🎉")
    else:
        st.stop()

# --------------------------
# QUESTIONS
# --------------------------
questions = [
    "Do you love me? 💖",
    "Will you be mine forever? 💍",
    "Do you like my silly jokes? 😂",
    "Can I get unlimited kisses from you? 😘",
    "Are you the best part of my life? 🌎",
    "Do you want cuddles right now? 🤗",
    "Will you go on a date with me soon? 🍷",
    "Do you like being pampered by me? 💆‍♀️",
    "Wanna plan a surprise trip together? ✈️",
    "Do you promise never to leave me? 💞",
]

st.header("Answer these, my love 💕")

for q in questions:
    col1, col2 = st.columns([1,1])

    with col1:
        yes_btn = st.button("Yes 💖", key=f"yes_{q}")
        if yes_btn:
            st.success(f"Yay!! You clicked YES for: {q}")
            # trigger hearts
            for i in range(10):
                st.markdown(
                    f"<div class='heart' style='left:{random.randint(10,90)}%; top:{random.randint(60,90)}%;'>❤️</div>",
                    unsafe_allow_html=True
                )
                time.sleep(0.05)

    with col2:
        st.markdown(
            f"""
            <button id="no_btn_{q}" style="
                background-color:#ffcccc; 
                border:none; 
                padding:8px 20px; 
                border-radius:20px;
                cursor:pointer;">
                No 💔
            </button>
            <script>
            const btn = document.getElementById("no_btn_{q}");
            btn.addEventListener("mouseover", function() {{
                const x = Math.floor(Math.random() * 200) - 100;
                const y = Math.floor(Math.random() * 200) - 100;
                btn.style.transform = `translate(${{x}}px, ${{y}}px)`;
            }});
            </script>
            """,
            unsafe_allow_html=True
        )
