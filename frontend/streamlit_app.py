# import streamlit as st
# import requests
# import time

# API_URL = "http://127.0.0.1:8000/chat"

# st.set_page_config(
#     page_title="Ride-Hailing AI Operations Copilot",
#     page_icon="🚗",
#     layout="wide"
# )

# # ------------------------------
# # Custom UI Styling
# # ------------------------------

# st.markdown("""
# <style>
# .chat-container {
#     max-height: 600px;
#     overflow-y: auto;
# }

# .chat-message {
#     padding: 1rem;
#     border-radius: 10px;
#     margin-bottom: 10px;
# }

# .user-msg {
#     background-color: #f0f2f6;
# }

# .ai-msg {
#     background-color: #eef6ff;
# }
# </style>
# """, unsafe_allow_html=True)

# # ------------------------------
# # Sidebar
# # ------------------------------

# st.sidebar.title("🚗 AI Operations Copilot")

# st.sidebar.markdown("""
# This AI assistant helps answer questions related to:

# • Rider support  
# • Driver payments  
# • Pricing & surge  
# • Safety policies  
# • Lost items  
# • Trip disputes
# """)

# # ------------------------------
# # Topic Filter (Industry Feature)
# # ------------------------------

# st.sidebar.markdown("### Topic Filter")

# topic = st.sidebar.selectbox(
#     "Select topic",
#     [
#         "All",
#         "Pricing",
#         "Driver Payments",
#         "Safety",
#         "Lost Items",
#         "Trip Disputes"
#     ]
# )

# # ------------------------------
# # Backend Status
# # ------------------------------

# st.sidebar.markdown("### System Status")

# try:
#     requests.get("http://127.0.0.1:8000/health")
#     st.sidebar.success("Backend Connected")
# except:
#     st.sidebar.error("Backend Not Running")

# # ------------------------------
# # Example Questions
# # ------------------------------

# st.sidebar.markdown("### Example Questions")

# example_questions = [
#     "How does surge pricing work?",
#     "How do I report a lost item?",
#     "How are driver earnings calculated?",
#     "How can I dispute a trip charge?"
# ]

# for q in example_questions:
#     if st.sidebar.button(q):
#         st.session_state["example_query"] = q

# # Clear conversation
# if st.sidebar.button("Clear Conversation"):
#     st.session_state.messages = []

# # ------------------------------
# # Main Title
# # ------------------------------

# st.title("🚗 Ride-Hailing AI Operations & Support Copilot")

# st.markdown(
#     "Ask questions about **driver support, trip issues, pricing, safety, and rider support.**"
# )

# # ------------------------------
# # Chat History
# # ------------------------------

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# chat_container = st.container()

# with chat_container:

#     for message in st.session_state.messages:

#         if message["role"] == "user":
#             with st.chat_message("user"):
#                 st.markdown(message["content"])

#         else:
#             with st.chat_message("assistant"):
#                 st.markdown(message["content"])

# # ------------------------------
# # User Input
# # ------------------------------

# user_input = st.chat_input("Ask a question about ride-hailing support...")

# # If example clicked
# if "example_query" in st.session_state:
#     user_input = st.session_state["example_query"]
#     del st.session_state["example_query"]

# if user_input:

#     # Save user message
#     st.session_state.messages.append({
#         "role": "user",
#         "content": user_input
#     })

#     with st.chat_message("user"):
#         st.markdown(user_input)

#     # Call backend
#     with st.chat_message("assistant"):

#         with st.spinner("Uber AI Copilot is thinking..."):

#             try:

#                 start = time.time()

#                 response = requests.post(
#                     API_URL,
#                     json={"query": user_input}
#                 )

#                 end = time.time()

#                 answer = response.json()["response"]
#                 latency = round(end - start, 2)

#             except:
#                 answer = "Error connecting to backend."
#                 latency = None

#         st.markdown(answer)

#         if latency:
#             st.caption(f"Response time: {latency}s")

#     # Save AI message
#     st.session_state.messages.append({
#         "role": "assistant",
#         "content": answer
#     })

# # ------------------------------
# # Footer
# # ------------------------------

# st.markdown("---")
# st.markdown(
#     "Built with **FastAPI + RAG + ChromaDB + SentenceTransformers + Gemini API + Streamlit**"
# )
import streamlit as st
import requests
import time

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title="Ride-Hailing AI Operations Copilot",
    page_icon="🚗",
    layout="wide"
)

# ------------------------------
# Custom UI Styling
# ------------------------------

st.markdown("""
<style>
.chat-container {
    max-height: 600px;
    overflow-y: auto;
}

.chat-message {
    padding: 1rem;
    border-radius: 10px;
    margin-bottom: 10px;
}

.user-msg {
    background-color: #f0f2f6;
}

.ai-msg {
    background-color: #eef6ff;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# Sidebar
# ------------------------------

st.sidebar.title("🚗 AI Operations Copilot")

st.sidebar.markdown("""
This AI assistant helps answer questions related to:

• Rider support  
• Driver payments  
• Pricing & surge  
• Safety policies  
• Lost items  
• Trip disputes
""")

# ------------------------------
# Topic Filter
# ------------------------------

st.sidebar.markdown("### Topic Filter")

topic = st.sidebar.selectbox(
    "Select topic",
    [
        "All",
        "Pricing",
        "Driver Payments",
        "Safety",
        "Lost Items",
        "Trip Disputes"
    ]
)

# ------------------------------
# Backend Status
# ------------------------------

st.sidebar.markdown("### System Status")

try:
    requests.get("http://127.0.0.1:8000/health")
    st.sidebar.success("Backend Connected")
except:
    st.sidebar.error("Backend Not Running")

# ------------------------------
# Example Questions
# ------------------------------

st.sidebar.markdown("### Example Questions")

example_questions = [
    "How does surge pricing work?",
    "How do I report a lost item?",
    "How are driver earnings calculated?",
    "How can I dispute a trip charge?"
]

for q in example_questions:
    if st.sidebar.button(q):
        st.session_state["example_query"] = q

# Clear conversation
if st.sidebar.button("Clear Conversation"):
    st.session_state.messages = []

# ------------------------------
# Main Title
# ------------------------------

st.title("🚗 Ride-Hailing AI Operations & Support Copilot")

st.markdown(
    "Ask questions about **driver support, trip issues, pricing, safety, and rider support.**"
)

# ------------------------------
# Chat History
# ------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

chat_container = st.container()

with chat_container:

    for message in st.session_state.messages:

        if message["role"] == "user":
            with st.chat_message("user"):
                st.markdown(message["content"])

        else:
            with st.chat_message("assistant"):
                st.markdown(message["content"])

# ------------------------------
# User Input
# ------------------------------

user_input = st.chat_input("Ask a question about ride-hailing support...")

# If example clicked
if "example_query" in st.session_state:
    user_input = st.session_state["example_query"]
    del st.session_state["example_query"]

if user_input:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Call backend
    with st.chat_message("assistant"):

        with st.spinner("Uber AI Copilot is thinking..."):

            try:

                start = time.time()

                response = requests.post(
                    API_URL,
                    json={"query": user_input}
                )

                end = time.time()

                data = response.json()

                answer = data["answer"]
                sources = data["sources"]
                retrieval_count = data["retrieval_count"]

                latency = round(end - start, 2)

            except:
                answer = "Error connecting to backend."
                sources = []
                retrieval_count = 0
                latency = None

        st.markdown(answer)

        # Retrieval information
        st.caption(f"Retrieved {retrieval_count} knowledge documents")

        # Sources
        if sources:
            st.markdown("**Sources used:**")

            for s in sources:
                st.caption(f"Document ID: {s}")

        # Response time
        if latency:
            st.caption(f"Response time: {latency}s")

    # Save AI message
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

# ------------------------------
# Footer
# ------------------------------

st.markdown("---")

st.markdown(
    "Built with **FastAPI + RAG + ChromaDB + SentenceTransformers + Gemini API + Streamlit**"
)

st.caption(
    "AI responses are generated using internal policy documents. "
    "For critical support issues please contact official platform support."
)