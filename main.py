import streamlit as st
import random

st.set_page_config(page_title="Pikachu Game", layout="centered")

st.title("🔷 Pikachu Matching Game")

# Tải ảnh Pokémon
image_files = ["pikachu.png", "bulbasaur.png", "charmander.png", "squirtle.png"]
image_files *= 2  # tạo cặp
random.shuffle(image_files)

# Trạng thái session
if "revealed" not in st.session_state:
    st.session_state.revealed = [False] * len(image_files)
if "clicked" not in st.session_state:
    st.session_state.clicked = []

def reset_game():
    random.shuffle(image_files)
    st.session_state.revealed = [False] * len(image_files)
    st.session_state.clicked = []

st.button("🔄 Chơi lại", on_click=reset_game)

cols = st.columns(4)
for i in range(len(image_files)):
    with cols[i % 4]:
        if st.session_state.revealed[i]:
            st.image(f"images/{image_files[i]}", width=100)
        else:
            if st.button("❓", key=i):
                st.session_state.revealed[i] = True
                st.session_state.clicked.append(i)

# So khớp
if len(st.session_state.clicked) == 2:
    idx1, idx2 = st.session_state.clicked
    if image_files[idx1] != image_files[idx2]:
        st.session_state.revealed[idx1] = False
        st.session_state.revealed[idx2] = False
    st.session_state.clicked = []
