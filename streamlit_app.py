import streamlit as st

# ----------------------------------
# PAGE CONFIG
# ----------------------------------
st.set_page_config(
    page_title="Scenario-Based Decision Simulation",
    layout="centered"
)

# ----------------------------------
# INITIALIZE SESSION STATE
# ----------------------------------
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.decisions = []
    st.session_state.profile = {
        "environmental": 0,
        "economic": 0,
        "social": 0,
        "governance": 0
    }

# ----------------------------------
# HELPER FUNCTIONS
# ----------------------------------
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
# INTRO PAGE (LEVEL 0)
# ----------------------------------
if st.session_state.step == 0:
    st.title("🌱 Sustainable Digital Transformation at GreenRetail Ltd.")

    st.write("""
You are the **Digital Strategy Lead** at *GreenRetail Ltd.*, a mid-sized retail company
operating both online and physical stores.

The organization plans to modernize its digital infrastructure to improve efficiency,
customer experience, and data-driven decision-making. Senior leadership has committed
to ensuring that all digital initiatives align with **environmental, social, economic,
and governance sustainability goals**.

You will now make a series of strategic decisions.  
There are **no perfect answers** — only trade-offs.
""")

    if st.button("Start Scenario"):
        st.session_state.step = 1
        st.experimental_rerun()

# ----------------------------------
# LEVEL 1 – CLOUD INFRASTRUCTURE
# ----------------------------------
elif st.session_state.step == 1:
    st.subheader("Decision 1: Cloud Infrastructure Strategy")

    choice = st.radio(
        "Which cloud infrastructure strategy should the company adopt?",
        [
            "Low-cost cloud provider powered mainly by fossil fuels",
            "Renewable-powered cloud provider",
            "Hybrid cloud (on-premise + cloud)"
        ]
    )

    if st.button("Confirm Decision"):
        if choice.startswith("Low-cost"):
            update_profile({"environmental": -2, "economic": 2, "governance": -1})
            st.info("Lower costs achieved, but environmental impact and regulatory risks increase.")
        elif choice.startswith("Renewable"):
            update_profile({"environmental": 2, "economic": -1, "governance": 1})
            st.info("Environmental performance improves, though operational costs rise.")
        else:
            update_profile({"environmental": 1, "economic": 0, "governance": 0})
            st.info("A balanced approach that introduces operational complexity.")

        st.session_state.decisions.append(choice)
        st.session_state.step = 2
        st.experimental_rerun()

# ----------------------------------
# LEVEL 2 – DATA MANAGEMENT
# ----------------------------------
elif st.session_state.step == 2:
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
            st.info("Analytics potential increases, but privacy risks and energy use rise.")
        elif choice.startswith("Apply"):
            update_profile({"environmental": 1, "social": 2, "governance": 1})
            st.info("Data responsibility improves with limited analytics scope.")
        else:
            update_profile({"economic": 1, "governance": -1})
            st.info("Operational simplicity improves, but transparency decreases.")

        st.session_state.decisions.append(choice)
        st.session_state.step = 3
        st.experimental_rerun()

# ----------------------------------
# LEVEL 3 – AI & AUTOMATION
# ----------------------------------
elif st.session_state.step == 3:
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
            st.info("Efficiency improves, but energy and ethical concerns increase.")
        elif choice.startswith("Selective"):
            update_profile({"economic": 1, "environmental": 0, "social": 1})
            st.info("Balanced innovation with controlled sustainability risks.")
        else:
            update_profile({"environmental": 1, "economic": -1})
            st.info("Sustainability risks are reduced, but competitiveness may suffer.")

        st.session_state.decisions.append(choice)
        st.session_state.step = 4
        st.experimental_rerun()

# ----------------------------------
# LEVEL 4 – EMPLOYEE UPSKILLING
# ----------------------------------
elif st.session_state.step == 4:
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
            st.info("Short-term savings achieved, but workforce readiness declines.")
        elif choice.startswith("Targeted"):
            update_profile({"economic": 0, "social": 1})
            st.info("Workforce capability improves without excessive cost.")
        else:
            update_profile({"economic": -1, "social": 2})
            st.info("Strong long-term resilience with higher investment.")

        st.session_state.decisions.append(choice)
        st.session_state.step = 5
        st.experimental_rerun()

# ----------------------------------
# LEVEL 5 – SUSTAINABILITY GOVERNANCE
# ----------------------------------
elif st.session_state.step == 5:
    st.subheader("Decision 5: Sustainability Governance")

    choice = st.radio(
        "How should sustainability performance be governed?",
        [
            "Annual sustainability reporting",
            "Real-time sustainability KPIs in dashboards",
            "Focus mainly on financial KPIs"
        ]
    )

    if st.button("Confirm Decision"):
        if choice.startswith("Annual"):
            update_profile({"governance": 0})
            st.info("Transparency exists, but responsiveness is limited.")
        elif choice.startswith("Real-time"):
            update_profile({"governance": 2})
            st.info("Continuous accountability and informed decision-making improve.")
        else:
            update_profile({"economic": 1, "governance": -2})
            st.info("Financial focus increases, but sustainability oversight weakens.")

        st.session_state.decisions.append(choice)
        st.session_state.step = 6
        st.experimental_rerun()

# ----------------------------------
# FINAL OUTCOME + REFLECTION
# ----------------------------------
else:
    st.title("📈 Sustainability Outcome Summary")

    for dim, score in st.session_state.profile.items():
        st.write(f"**{dim.capitalize()} sustainability:** {qualitative_label(score)}")

    st.divider()

    st.subheader("Reflection (Manual Assessment)")
    reflection = st.text_area(
        "Reflect on your decisions and sustainability trade-offs:",
        height=200,
        max_chars=1200
    )

    st.caption("Suggested length: 200–250 words")

    if st.button("Submit Reflection"):
        st.success("Simulation completed. Reflection recorded for manual grading.")
