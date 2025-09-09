import streamlit as st
import random

# ===== CONFIG =====
SITE_PASSWORD = "our-secret"  # change this before sharing
FINAL_MESSAGE = "Pravisha, I love you more than words. Forever yours 💖"
APP_TITLE = "Love Portal 💕"
# ==================

st.set_page_config(page_title=APP_TITLE, layout="centered")

# Keep session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "answers" not in st.session_state:
    st.session_state.answers = {}

# Password gate
st.title(APP_TITLE)
if not st.session_state.authenticated:
    pw = st.text_input("Enter our secret password:", type="password")
    if pw == SITE_PASSWORD:
        st.session_state.authenticated = True
        st.success("Password accepted — welcome, my love! 🎉")
    st.stop()

# Questions (mix of romantic, funny, flirty)
questions = [
    "Do you love me? 💖",
    "Do you miss me when I’m not around? 🥺",
    "Do you think I’m the cutest human alive? 😏",
    "Will you always be my partner-in-crime? 🕵️‍♀️",
    "Do you want unlimited hugs forever? 🤗",
    "Do you think about me before you sleep? 🌙",
    "Do you promise to keep laughing at my bad jokes? 🤡",
    "Do you secretly think I’m hotter than your favorite celebrity? 🔥",
    "Do you want endless kisses? 😘",
    "Would you say yes if I asked you on 1,000 more dates? 💍",
    "Do you want me to annoy you forever with my love? 🐒",
    "Do you want a lifetime of cuddles, even when I steal the blanket? 🛌",
    "Will you let me spoil you like my queen? 👑",
    "Do you get butterflies when you see me? 🦋",
    "Do you want me to be your forever headache and happiness? 💕",
]

st.write("Answer these questions (hint: you can only click **Yes** 😏):")

# Render questions
for idx, q in enumerate(questions):
    st.write(f"**{q}**")

    col1, col2 = st.columns([1, 1])

    # Yes button
    if col1.button("Yes 💖", key=f"yes_{idx}"):
        st.session_state.answers[idx] = "Yes"

    # Fake "No" button that can't be clicked (moves randomly)
    x_shift = random.randint(-60, 60)
    y_shift = random.randint(-20, 20)
    no_style = f"margin-left:{x_shift}px;margin-top:{y_shift}px;"

    col2.markdown(
        f'<button disabled style="{no_style}background-color:pink;border:none;'
        f'padding:6px 12px;border-radius:6px;cursor:not-allowed;">No 🚫</button>',
        unsafe_allow_html=True,
    )

# Submit button
if st.button("Submit & Reveal 💌"):
    st.success(FINAL_MESSAGE)
    st.balloons()
