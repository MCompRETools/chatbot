import streamlit as st
from scenarios import SCENARIO
from impact_model import update_impact
from feedback import interpret_impact

st.set_page_config(page_title="Scenario-Based Simulation", layout="centered")

# Initialize state
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.impact = {"env": 0, "econ": 0, "soc": 0, "gov": 0}
    st.session_state.responses = []

st.title(SCENARIO["title"])
st.write(SCENARIO["context"])

# Decision flow
if st.session_state.step < len(SCENARIO["decisions"]):
    decision = SCENARIO["decisions"][st.session_state.step]
    choice = st.radio(decision["question"], list(decision["options"].keys()))

    if st.button("Confirm Decision"):
        impact = decision["options"][choice]
        st.session_state.impact = update_impact(st.session_state.impact, impact)
        st.session_state.responses.append((decision["id"], choice))
        st.session_state.step += 1
        st.experimental_rerun()

# Final outcome
else:
    st.subheader("Sustainability Outcome Summary")

    for dim, score in st.session_state.impact.items():
        st.write(f"**{dim.upper()}**: {interpret_impact(score)}")

    st.subheader("Reflection")
    reflection = st.text_area(
        "Explain the trade-offs behind your decisions:",
        max_chars=300
    )

    if st.button("Submit Reflection"):
        st.success("Simulation completed. Thank you.")
