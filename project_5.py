import streamlit as st

if "room" not in st.session_state:
    st.session_state.room = "start"

if "solved" not in st.session_state:
    st.session_state.solved = {"room1": False, "room2": False, "room3": False}


def go_to(room_name):
    st.session_state.room = room_name

st.title("Riddle Adventure")

if st.session_state.room == "start":
    st.write("You are in a quiet hallway with three locked doors.")
    if st.button("Enter Room 1"):
        go_to("room1")

elif st.session_state.room == "room1":
    st.subheader("Room 1: The Locked door")
    st.write("Riddle: What has keys but no locks?")
    answer = st.text_input("Your answer:", key="r1")
    if answer:
        if answer.lower() == "keyboard":
            st.success("Correct! The door unlocks.")
            st.session_state.solved["room1"] = True
        else:
            st.error("Incorrect answer.")
        if st.session_state.solved["room1"]:
            if st.button("Go to Room 2"):
                go_to("room2")

elif st.session_state.room == "room2":
    st.subheader("Room 2: John Wick")
    st.write("Riddle: I’m tall when I’m young and short when I’m old. What am I?")
    answer = st.text_input("Your answer:", key="r2")
    if answer:
        if answer.lower() == "candle":
            st.success("Correct!")
            st.session_state.solved["room2"] = True
        else:
            st.error("Try again.")
        if st.session_state.solved["room2"]:
            if st.button("Go to Room 3"):
                go_to("room3")

elif st.session_state.room == "room3":
    st.subheader("Room 3: The Final Riddle")
    st.write("Riddle: What gets wetter the more it dries?")
    answer = st.text_input("Your answer:", key="r3")
    
    if answer:
        if answer.lower() == "towel":
            st.success("You solved the final riddle!")
            st.session_state.solved["room3"] = True
        else:
            st.error("Wrong answer.")
        if st.session_state.solved["room3"]:
            if st.button("Finish Game"):
                go_to("win")

elif st.session_state.room == "win":
    st.success("Congratulations! You completed the riddle adventure.")