import streamlit as st

from crew import ask_question


st.set_page_config(
    page_title="AI Q&A Assistant",
    page_icon="💬"
)

st.title("AI Q&A Assistant")
st.write("Ask any question and get an answer from Gemini.")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


question = st.chat_input("Ask your question...")


if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                answer = ask_question(question)

                st.markdown(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            except Exception as error:
                st.error(f"Error: {error}")