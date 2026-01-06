import streamlit as st
from openai import OpenAI
import os
import json
import random
from transformers import pipeline

os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0"

os.environ["HUGGINGFACE_HUB_TOKEN"] = st.secrets["HF_TOKEN"]
MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"
# Show title and description.
st.title("💬 Chatbot")
st.write(
    "This is a simple chatbot for interacting on topics of Sustainable Digitalization"
)
@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="Qwen/Qwen2.5-0.5B-Instruct",
        device=-1,
        trust_remote_code=True
    )

llm = load_model()

# ----------------------------
# LOAD DATA
# ----------------------------
with open("knowledge_chunks.json", "r", encoding="utf-8") as f:
    KNOWLEDGE = json.load(f)

with open("scenarios.json", "r", encoding="utf-8") as f:
    SCENARIOS = json.load(f)

# ----------------------------
# UTILS
# ----------------------------
def retrieve_knowledge():
    return " ".join([k["text"] for k in random.sample(KNOWLEDGE, 2)])

def generate(prompt, max_tokens=250):
    out = llm(prompt, max_new_tokens=max_tokens, temperature=0.6)
    return out[0]["generated_text"]

# ----------------------------
# SESSION STATE
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------
# UI
# ----------------------------
st.title("🌱 Sustainable Digitalization – AI Tutor")

st.markdown("""
This interactive chatbot helps you test knowledge and reason through
real-world sustainability scenarios.
""")

choice = st.radio(
    "How would you like to proceed?",
    ["Knowledge Check", "Scenario-Based Activity"]
)

# ----------------------------
# KNOWLEDGE CHECK MODE
# ----------------------------
if choice == "Knowledge Check":
    question = st.text_input("Enter a sustainability-related question:")

    answer = st.text_area("Your answer:")

    if st.button("Submit Answer"):
        context = retrieve_knowledge()

        prompt = f"""
SYSTEM:
You are an academic tutor for Sustainable Digitalization.

CONTEXT:
{context}

QUESTION:
{question}

STUDENT ANSWER:
{answer}

TASK:
1. Say if the answer is correct.
2. Correct it if needed.
3. Ask one follow-up question.
"""
        response = generate(prompt)
        st.markdown("### AI Feedback")
        st.write(response)

# ----------------------------
# SCENARIO MODE
# ----------------------------
if choice == "Scenario-Based Activity":
    scenario = random.choice(SCENARIOS)

    st.markdown("### Business Scenario")
    st.write(scenario["scenario"])

    student_solution = st.text_area("Your proposed solution:")

    if st.button("Evaluate Solution"):
        prompt = f"""
SYSTEM:
You are an expert tutor in sustainable digitalization.

SCENARIO:
{scenario["scenario"]}

STUDENT RESPONSE:
{student_solution}

TASK:
1. Identify one sustainability benefit
2. Identify one trade-off or risk
3. Ask ONE probing follow-up question
"""
        feedback = generate(prompt)
        st.markdown("### AI Feedback")
        st.write(feedback)

        reflection = st.text_area("Reflection (optional):")

        if reflection:
            summary_prompt = f"""
SYSTEM:
You are an academic evaluator.

STUDENT REFLECTION:
{reflection}

TASK:
Summarize the key learning in 3–4 lines.
"""
            summary = generate(summary_prompt)
            st.markdown("### Learning Summary")
            st.write(summary)

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
#openai_api_key = st.text_input("OpenAI API Key", type="password")
#if not openai_api_key:
 #   st.info("Please add your OpenAI API key to continue.", icon="🗝️")
#else:

    # Create an OpenAI client.
    #client = OpenAI(api_key=openai_api_key)

    # Create a session state variable to store the chat messages. This ensures that the
    # messages persist across reruns.
    #if "messages" not in st.session_state:
     #   st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
    #for message in st.session_state.messages:
     #   with st.chat_message(message["role"]):
      #      st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message. This will display
    # automatically at the bottom of the page.
    #if prompt := st.chat_input("What is up?"):

        # Store and display the current prompt.
     #   st.session_state.messages.append({"role": "user", "content": prompt})
       # with st.chat_message("user"):
        #    st.markdown(prompt)

        # Generate a response using the OpenAI API.
       # stream = client.chat.completions.create(
       #     model="gpt-3.5-turbo",
       #     messages=[
       #         {"role": m["role"], "content": m["content"]}
        #        for m in st.session_state.messages
       #     ],
       #     stream=True,
      #  )

        # Stream the response to the chat using `st.write_stream`, then store it in 
        # session state.
     #   with st.chat_message("assistant"):
        #    response = st.write_stream(stream)
       # st.session_state.messages.append({"role": "assistant", "content": response})
