import streamlit as st
from src.chat_session import ChatSession
from src.log_analyzer import analyze_log
from src.retriever import LogRetriever

st.set_page_config(page_title="Log Debug AI", layout="wide")

st.title("🔧 Log Debug AI")

# SESSION INIT
if "chat" not in st.session_state:
    st.session_state.chat = ChatSession()

if "retriever" not in st.session_state:
    st.session_state.retriever = None

if "logs" not in st.session_state:
    st.session_state.logs = ""

if "last_chunks" not in st.session_state:
    st.session_state.last_chunks = []

if "log_loaded" not in st.session_state:
    st.session_state.log_loaded = False

# SIDEBAR
st.sidebar.header("Load Logs")

uploaded_file = st.sidebar.file_uploader("Upload Log")
pasted_log = st.sidebar.text_area("Paste Log")

# LOAD BUTTON
if st.sidebar.button("Load"):

    with st.spinner("Loading and indexing logs..."):

        if uploaded_file:
            data = uploaded_file.read().decode()
            st.session_state.logs = data
            st.session_state.retriever = LogRetriever(data)
            st.session_state.log_loaded = True

            # PRO UX FEEDBACK
            st.toast("✅ Log file loaded successfully")
            st.sidebar.success("Log file loaded")
            st.success(f"Log loaded successfully! ({len(data)} characters)")

        elif pasted_log:
            st.session_state.logs = pasted_log
            st.session_state.retriever = LogRetriever(pasted_log)
            st.session_state.log_loaded = True

            # PRO UX FEEDBACK
            st.toast("✅ Pasted log loaded successfully")
            st.sidebar.success("Pasted log loaded")
            st.success(f"Log loaded successfully! ({len(pasted_log)} characters)")

        else:
            st.toast("⚠️ Please upload or paste a log")
            st.sidebar.warning("Upload or paste log first")

# CHAT DISPLAY
for msg in st.session_state.chat.get_messages():
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# CHAT INPUT
prompt = st.chat_input("Ask about logs...")

if prompt:

    st.session_state.chat.add_user_message(prompt)

    with st.chat_message("user"):
        st.markdown(prompt)

    if st.session_state.retriever:

        with st.spinner("Analyzing logs..."):

            chunks = st.session_state.retriever.get_relevant_chunks(prompt)
            context = "\n\n".join(chunks)

            messages = [
                {"role": "system", "content": f"Relevant log data:\n{context}"},
                {"role": "user", "content": prompt}
            ]

            response = analyze_log(messages)

        st.session_state.chat.add_ai_message(response)

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.last_chunks = chunks

    else:
        st.toast("⚠️ Load logs first")
        st.warning("Please load logs before asking questions")

# OPTIONAL EVIDENCE
with st.expander("🔍 Show Evidence Used"):
    for c in st.session_state.last_chunks:
        st.code(c)
