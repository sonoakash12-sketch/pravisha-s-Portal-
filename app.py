import streamlit as st
import random

# ===== CONFIG =====
SITE_PASSWORD = "our-secret"  # change this before sharing
FINAL_MESSAGE = "Pravisha, I love you more than words. Forever yours 💖"
APP_TITLE = "Pravisha's Portal 💕"
# ==================

st.set_page_config(page_title=APP_TITLE, layout="centered")

# Custom CSS + JS for background and floating hearts
st.markdown("""
<style>
body {
    background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fbc2eb, #a6c1ee);
    background-size: 400% 400%;
    animation: gradient 12s ease infinite;
}
@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Floating heart animation */
.heart {
    position: fixed;
    font-size: 24px;
    animation: floatUp 5s linear infinite;
    bottom: -10%;
}
@keyframes floatUp {
    from {transform: translateY(0);}
    to {transform: translateY(-120vh);}
}
</style>

<script>
// Function to spawn hearts
function spawnHearts() {
    for (let i = 0; i < 15; i++) {
        let heart = document.createElement("div");
        heart.innerHTML = "💖";
        heart.className = "heart";
        heart.style.left = Math.random() * 100 + "vw";
        heart.style.fontSize = Math.random() * 20 + 20 + "px";
        document.body.appendChild(heart);
        setTimeout(() => heart.remove(), 5000);
    }
}

// Runaway No button
function makeNoRun(buttonId) {
    const btn = document.getElementById(buttonId);
    if (!btn) return;
    btn.onmouseover = function() {
        btn.style.position = "absolute";
        btn.style.left = Math.random() * 80 + "vw";
        btn.style.top = Math.random() * 80 + "vh";
    }
}
</script>
""", unsafe_allow_html=True)

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
        st.success("Password accepted — welcome to your portal, Pravisha! 🎉")
    st.stop()

# Questions (romantic, funny, flirty)
questions = [
    "Do you love me? 💖",
    "Do you miss me when I’m not around? 🥺",
    "Do you think I’m the cutest human alive? 😏",
    "Will you always be my partner-in-crime? 🕵️‍♀️",
    "Do you want unlimited hugs forever? 🤗",
    "Do you think about me before you sleep? 🌙",
    "Do you promise to keep laughing at my bad jokes? 🤡",
    "Do you want me to do fucky fucky you every night? 🔥",
    "Do you want endless kisses? 😘",
    "Would you say yes if I asked you on 1,000 more dates? 💍",
    "Do you want me to annoy you forever with my love? 🐒",
    "Do you want a lifetime of cuddles, even when I steal the blanket? 🛌",
    "Do you enjoy my Dicky? 👑",
    "Do you get butterflies when you see me? 🦋",
    "Do you want me to be your forever headache and happiness? 💕",
]

st.write("Answer these questions (hint: you can only click **Yes** 😏):")

# Render questions
for idx, q in enumerate(questions):
    st.write(f"**{q}**")

    col1, col2 = st.columns([1, 1])

    # Yes button with emoji explosion
    if col1.button("Yes 💖", key=f"yes_{idx}"):
        st.session_state.answers[idx] = "Yes"
        st.markdown("<script>spawnHearts();</script>", unsafe_allow_html=True)

    # No button that runs away
    button_id = f"no_btn_{idx}"
    col2.markdown(
        f'<button id="{button_id}" style="background-color:pink;border:none;'
        f'padding:6px 12px;border-radius:6px;cursor:pointer;">No 🚫</button>'
        f'<script>makeNoRun("{button_id}");</script>',
        unsafe_allow_html=True,
    )

# Submit button
if st.button("Submit & Reveal 💌"):
    st.markdown(
        f"<h2 style='color:#e75480; text-align:center;'>{FINAL_MESSAGE}</h2>",
        unsafe_allow_html=True,
    )
    st.balloons()

