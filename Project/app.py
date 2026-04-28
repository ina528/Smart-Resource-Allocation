import streamlit as st

st.title("🌍 Community Help Matcher")

# Temporary storage (like your lists)
if "requests_list" not in st.session_state:
    st.session_state.requests_list = []

if "volunteers" not in st.session_state:
    st.session_state.volunteers = []

# -----------------------
# Add Help Request
# -----------------------
st.header("Add Help Request")

task = st.text_input("Task")
req_location = st.text_input("Request Location")

if st.button("Submit Request"):
    if task and req_location:
        st.session_state.requests_list.append({
            "task": task,
            "location": req_location
        })
        st.success("Request added!")
    else:
        st.warning("Please fill all fields")

# -----------------------
# Add Volunteer
# -----------------------
st.header("Add Volunteer")

name = st.text_input("Name")
vol_location = st.text_input("Volunteer Location")

if st.button("Register Volunteer"):
    if name and vol_location:
        st.session_state.volunteers.append({
            "name": name,
            "location": vol_location
        })
        st.success("Volunteer added!")
    else:
        st.warning("Please fill all fields")

# -----------------------
# Match Logic
# -----------------------
st.header("Find Matches")

if st.button("Show Matches"):
    matches = []

    for req in st.session_state.requests_list:
        for vol in st.session_state.volunteers:
            if req["location"].lower() == vol["location"].lower():
                matches.append(
                    f"{vol['name']} will help with {req['task']} at {req['location']}"
                )

    if matches:
        for m in matches:
            st.write("✅", m)
    else:
        st.warning("No matches found")
