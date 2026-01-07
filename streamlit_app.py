import streamlit as st
import time
import csv
from datetime import datetime

# ----------------------------------
# PAGE CONFIG
# ----------------------------------
st.set_page_config(page_title="Sustainable Digitalization Simulation")

# ----------------------------------
# INITIALIZE SESSION STATE
# ----------------------------------
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.start_time = time.time()
    st.session_state.decision_time = None
    st.session_state.last_feedback = ""
    st.session_state.analytics = []
    st.session_state.profile = {
        "environmental": 0,
        "economic": 0,
        "social": 0,
        "governance": 0
    }

# ----------------------------------
# HELPER FUNCTIONS
# ----------------------------------
def log_event(stage, label):
    elapsed = round(time.time() - st.session_state.start_time, 2)
    st.session_state.analytics.append({
        "timestamp": datetime.now().isoformat(),
        "stage": stage,
        "event": label,
        "elapsed_seconds": elapsed
    })
    st.session_state.start_time = time.time()

def update_profile(impact):
    for k, v in impact.items():
        st.session_state.profile[k] += v

def qualitative_label(score):
    if score >= 2:
        return "Strong alignment"
    elif score >= 0:
        return "Moderate alignment"
    else:
        return "Weak alignment"

def save_analytics():
    with open("learning_analytics.csv", "a", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["timestamp", "stage", "event", "elapsed_seconds"]
        )
        if f.tell() == 0:
            writer.writeheader()
        writer.writerows(st.session_state.analytics)

# ----------------------------------
# PROGRESS INDICATOR
# ----------------------------------
def progress(level):
    st.progress(level / 5)
    st.caption(f"Progress: Level {level} of 5")

# ----------------------------------
# INTRO PAGE
# ----------------------------------
if st.session_state.step == 0:
    st.title("🌱 Sustainable Digital Transformation – Teaching Simulation")

    st.write("""
You are the **Digital Strategy Lead** at *GreenRetail Ltd.*  
You must guide digital transformation while balancing:
- Environmental responsibility  
- Economic performance  
- Social trust  
- Governance compliance
""")

    if st.button("Start Scenario"):
        log_event("Intro", "Scenario started")
        st.session_state.step = 1.0
        st.experimental_rerun()

# ----------------------------------
# DECISION TEMPLATE FUNCTION
# ----------------------------------
def decision_page(level, title, question, options, impacts):
    progress(level)
    st.subheader(title)

    choice = st.radio(question, options)

    if st.button("Confirm Decision"):
        update_profile(impacts[choice]["impact"])
        st.session_state.last_feedback = impacts[choice]["feedback"]

        log_event(f"Decision {level}", choice)
        st.session_state.step = level + 0.1
        st.experimental_rerun()

def feedback_page(level):
    progress(level)
    st.info(st.session_state.last_feedback)

    if st.button("Continue"):
        log_event(f"Feedback {level}", "Viewed feedback")
        st.session_state.step = level + 1
        st.experimental_rerun()

# ----------------------------------
# DECISION 1
# ----------------------------------
if st.session_state.step == 1.0:
    decision_page(
        1,
        "Decision 1: Cloud Infrastructure",
        "Which infrastructure strategy should be adopted?",
        [
            "Low-cost fossil-based provider",
            "Renewable-powered provider",
            "Hybrid cloud model"
        ],
        {
            "Low-cost fossil-based provider": {
                "impact": {"environmental": -2, "economic": 2},
                "feedback": "Lower costs achieved, but emissions and regulatory risks increase."
            },
            "Renewable-powered provider": {
                "impact": {"environmental": 2, "economic": -1},
                "feedback": "Environmental alignment improves with higher operational cost."
            },
            "Hybrid cloud model": {
                "impact": {"environmental": 1},
                "feedback": "Balanced approach, but governance complexity increases."
            }
        }
    )

elif st.session_state.step == 1.1:
    feedback_page(1)

# ----------------------------------
# DECISION 2
# ----------------------------------
elif st.session_state.step == 2.0:
    decision_page(
        2,
        "Decision 2: Data Management",
        "How should customer data be handled?",
        [
            "Collect all available data",
            "Apply data minimization",
            "Outsource data analytics"
        ],
        {
            "Collect all available data": {
                "impact": {"social": -2, "environmental": -1},
                "feedback": "Analytics expand, but privacy risks and energy use rise."
            },
            "Apply data minimization": {
                "impact": {"social": 2, "environmental": 1},
                "feedback": "Trust and sustainability improve with limited analytics."
            },
            "Outsource data analytics": {
                "impact": {"economic": 1, "governance": -1},
                "feedback": "Efficiency improves, but transparency declines."
            }
        }
    )

elif st.session_state.step == 2.1:
    feedback_page(2)

# ----------------------------------
# DECISION 3
# ----------------------------------
elif st.session_state.step == 3.0:
    decision_page(
        3,
        "Decision 3: AI Deployment",
        "How should AI be used?",
        [
            "Extensive AI deployment",
            "Selective AI deployment",
            "Avoid AI"
        ],
        {
            "Extensive AI deployment": {
                "impact": {"economic": 2, "environmental": -1},
                "feedback": "Efficiency rises, but energy and ethical risks increase."
            },
            "Selective AI deployment": {
                "impact": {"economic": 1, "social": 1},
                "feedback": "Balanced innovation with controlled sustainability impact."
            },
            "Avoid AI": {
                "impact": {"environmental": 1, "economic": -1},
                "feedback": "Risks decrease, but competitiveness may suffer."
            }
        }
    )

elif st.session_state.step == 3.1:
    feedback_page(3)

# ----------------------------------
# 🚨 REGULATORY SHOCK EVENT
# ----------------------------------
elif st.session_state.step == 4:
    st.warning("""
🚨 **Regulatory Update**

New sustainability regulations now require:
- Carbon reporting transparency
- Stronger data governance
- Evidence of employee digital training

Your remaining decisions must account for stricter compliance.
""")

    log_event("Shock Event", "New regulation introduced")

    if st.button("Acknowledge and Continue"):
        st.session_state.step = 4.0
        st.experimental_rerun()

# ----------------------------------
# DECISION 4
# ----------------------------------
elif st.session_state.step == 4.0:
    decision_page(
        4,
        "Decision 4: Employee Upskilling",
        "How should employees be supported?",
        [
            "Minimal training",
            "Targeted training",
            "Extensive reskilling"
        ],
        {
            "Minimal training": {
                "impact": {"social": -2},
                "feedback": "Cost savings achieved, but compliance risk increases."
            },
            "Targeted training": {
                "impact": {"social": 1},
                "feedback": "Skills improve while managing costs."
            },
            "Extensive reskilling": {
                "impact": {"social": 2, "economic": -1},
                "feedback": "Strong long-term compliance and resilience."
            }
        }
    )

elif st.session_state.step == 4.1:
    feedback_page(4)

# ----------------------------------
# DECISION 5
# ----------------------------------
elif st.session_state.step == 5.0:
    decision_page(
        5,
        "Decision 5: Sustainability Governance",
        "How should sustainability performance be governed?",
        [
            "Annual reporting",
            "Real-time sustainability dashboards",
            "Financial KPIs only"
        ],
        {
            "Annual reporting": {
                "impact": {"governance": 0},
                "feedback": "Transparency exists, but action is delayed."
            },
            "Real-time sustainability dashboards": {
                "impact": {"governance": 2},
                "feedback": "Continuous accountability and regulatory alignment improve."
            },
            "Financial KPIs only": {
                "impact": {"economic": 1, "governance": -2},
                "feedback": "Financial focus increases, but compliance risk rises."
            }
        }
    )

elif st.session_state.step == 5.1:
    feedback_page(5)

# ----------------------------------
# FINAL OUTCOME + REFLECTION EXPORT
# ----------------------------------
else:
    st.title("📊 Final Sustainability Profile")

    for dim, score in st.session_state.profile.items():
        st.write(f"**{dim.capitalize()}**: {qualitative_label(score)}")

    st.divider()
    st.subheader("Reflection (Assessed Manually)")

    reflection = st.text_area(
        "Reflect on your decisions, trade-offs, and response to regulation:",
        height=220
    )

    st.markdown("""
**Assessment rubric (for instructor):**
- Sustainability reasoning (40%)
- Trade-off awareness (30%)
- Response to regulation (30%)
""")

    if st.button("Submit Reflection"):
        save_analytics()

        with open("reflections.csv", "a", newline="") as f:
            writer = csv.writer(f)
            if f.tell() == 0:
                writer.writerow(["timestamp", "reflection_text"])
            writer.writerow([datetime.now().isoformat(), reflection])

        st.success("Simulation completed. Reflection and analytics saved.")
