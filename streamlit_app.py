import streamlit as st

# ----------------------------------
# PAGE CONFIG
# ----------------------------------
st.set_page_config(page_title="Scenario-Based Decision Simulation")

# ----------------------------------
# INITIALIZE SESSION STATE
# ----------------------------------
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.last_feedback = ""
    st.session_state.profile = {
        "environmental": 0,
        "economic": 0,
        "social": 0,
        "governance": 0
    }

def update_profile(impact):
    for k, v in impact.items():
        st.session_state.profile[k] += v

def qualitative_label(score):
    if score >= 2:
        return "Strong positive alignment"
    elif score >= 0:
        return "Moderate alignment"
    else:
        return "Weak alignment"

# ----------------------------------
# INTRO PAGE
# ----------------------------------
if st.session_state.step == 0:
    st.title("🌱 Sustainable Digital Transformation at GreenRetail Ltd.")

    st.write("""
You are the **Digital Strategy Lead** at GreenRetail Ltd.
Your task is to guide the company through a digital transformation
while balancing **economic performance**, **environmental responsibility**,
**social trust**, and **governance compliance**.
""")

    if st.button("Start Scenario"):
        st.session_state.step = 1.0
        st.experimental_rerun()

# ----------------------------------
# DECISION 1
# ----------------------------------
elif st.session_state.step == 1.0:
    st.subheader("Decision 1: Cloud Infrastructure Strategy")

    choice = st.radio(
        "Which strategy should the company adopt?",
        [
            "Low-cost cloud provider powered mainly by fossil fuels",
            "Renewable-powered cloud provider",
            "Hybrid cloud (on-premise + cloud)"
        ]
    )

    if st.button("Confirm Decision"):
        if choice.startswith("Low-cost"):
            update_profile({"environmental": -2, "economic": 2, "governance": -1})
            st.session_state.last_feedback = (
                "Short-term cost efficiency improves, but carbon emissions "
                "and long-term regulatory risks increase."
            )
        elif choice.startswith("Renewable"):
            update_profile({"environmental": 2, "economic": -1, "governance": 1})
            st.session_state.last_feedback = (
                "Environmental performance improves significantly, "
                "though operational costs rise."
            )
        else:
            update_profile({"environmental": 1})
            st.session_state.last_feedback = (
                "A balanced approach that reduces risk but increases system complexity."
            )

        st.session_state.step = 1.1
        st.experimental_rerun()

elif st.session_state.step == 1.1:
    st.info(st.session_state.last_feedback)
    if st.button("Continue to next decision"):
        st.session_state.step = 2.0
        st.experimental_rerun()

# ----------------------------------
# DECISION 2
# ----------------------------------
elif st.session_state.step == 2.0:
    st.subheader("Decision 2: Data Management Strategy")

    choice = st.radio(
        "How should customer data be managed?",
        [
            "Collect and store all available customer data",
            "Apply data minimization principles",
            "Outsource data management to third-party vendors"
        ]
    )

    if st.button("Confirm Decision"):
        if choice.startswith("Collect"):
            update_profile({"environmental": -1, "social": -2, "governance": -1})
            st.session_state.last_feedback = (
                "Analytics potential increases, but privacy risks "
                "and energy consumption grow."
            )
        elif choice.startswith("Apply"):
            update_profile({"environmental": 1, "social": 2, "governance": 1})
            st.session_state.last_feedback = (
                "Responsible data practices improve trust "
                "and sustainability alignment."
            )
        else:
            update_profile({"economic": 1, "governance": -1})
            st.session_state.last_feedback = (
                "Operational simplicity improves, but transparency decreases."
            )

        st.session_state.step = 2.1
        st.experimental_rerun()

elif st.session_state.step == 2.1:
    st.info(st.session_state.last_feedback)
    if st.button("Continue to next decision"):
        st.session_state.step = 3.0
        st.experimental_rerun()

# ----------------------------------
# DECISION 3
# ----------------------------------
elif st.session_state.step == 3.0:
    st.subheader("Decision 3: Use of AI and Automation")

    choice = st.radio(
        "How should AI be deployed?",
        [
            "Extensive AI deployment across all processes",
            "Selective AI use for high-impact areas",
            "Avoid AI due to ethical and energy concerns"
        ]
    )

    if st.button("Confirm Decision"):
        if choice.startswith("Extensive"):
            update_profile({"economic": 2, "environmental": -1, "social": -1})
            st.session_state.last_feedback = (
                "Efficiency increases, but ethical and environmental concerns rise."
            )
        elif choice.startswith("Selective"):
            update_profile({"economic": 1, "social": 1})
            st.session_state.last_feedback = (
                "Innovation is balanced with sustainability considerations."
            )
        else:
            update_profile({"environmental": 1, "economic": -1})
            st.session_state.last_feedback = (
                "Sustainability risks are minimized, but competitiveness may decline."
            )

        st.session_state.step = 3.1
        st.experimental_rerun()

elif st.session_state.step == 3.1:
    st.info(st.session_state.last_feedback)
    if st.button("Continue to next decision"):
        st.session_state.step = 4.0
        st.experimental_rerun()

# ----------------------------------
# DECISION 4
# ----------------------------------
elif st.session_state.step == 4.0:
    st.subheader("Decision 4: Employee Digital Upskilling")

    choice = st.radio(
        "How should employees be supported?",
        [
            "Minimal training to reduce costs",
            "Targeted digital and sustainability training",
            "Extensive long-term reskilling programs"
        ]
    )

    if st.button("Confirm Decision"):
        if choice.startswith("Minimal"):
            update_profile({"economic": 1, "social": -2})
            st.session_state.last_feedback = (
                "Short-term savings are achieved, but workforce readiness declines."
            )
        elif choice.startswith("Targeted"):
            update_profile({"social": 1})
            st.session_state.last_feedback = (
                "Employees gain necessary skills without excessive investment."
            )
        else:
            update_profile({"economic": -1, "social": 2})
            st.session_state.last_feedback = (
                "Long-term resilience improves through strong workforce development."
            )

        st.session_state.step = 4.1
        st.experimental_rerun()

elif st.session_state.step == 4.1:
    st.info(st.session_state.last_feedback)
    if st.button("Continue to next decision"):
        st.session_state.step = 5.0
        st.experimental_rerun()

# ----------------------------------
# DECISION 5
# ----------------------------------
elif st.session_state.step == 5.0:
    st.subheader("Decision 5: Sustainability Governance")

    choice = st.radio(
        "How should sustainability be governed?",
        [
            "Annual sustainability reporting",
            "Real-time sustainability KPIs in dashboards",
            "Focus mainly on financial KPIs"
        ]
    )

    if st.button("Confirm Decision"):
        if choice.startswith("Annual"):
            update_profile({"governance": 0})
            st.session_state.last_feedback = (
                "Transparency exists, but responsiveness is limited."
            )
        elif choice.startswith("Real-time"):
            update_profile({"governance": 2})
            st.session_state.last_feedback = (
                "Continuous accountability and informed decision-making improve."
            )
        else:
            update_profile({"economic": 1, "governance": -2})
            st.session_state.last_feedback = (
                "Financial focus increases, but sustainability oversight weakens."
            )

        st.session_state.step = 5.1
        st.experimental_rerun()

elif st.session_state.step == 5.1:
    st.info(st.session_state.last_feedback)
    if st.button("View Final Outcome"):
        st.session_state.step = 6
        st.experimental_rerun()

# ----------------------------------
# FINAL OUTCOME + REFLECTION
# ----------------------------------
else:
    st.title("📊 Sustainability Outcome Summary")

    for dim, score in st.session_state.profile.items():
        st.write(f"**{dim.capitalize()}**: {qualitative_label(score)}")

    st.divider()

    st.subheader("Reflection (Manual Assessment)")
    st.text_area(
        "Reflect on your decisions, trade-offs, and sustainability priorities:",
        height=220
    )

    st.caption("Suggested length: 200–250 words")
