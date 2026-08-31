import streamlit as st
from agent import agent

# page configuration

st.set_page_config(
    page_title="ChatMate",
    page_icon="🤖",
    layout="centered"
)

# title

st.title("🤖 ChatMate")

st.caption(
    "Simple AI Chatbot with Tools"
)


# session chat history

if "messages" not in st.session_state:

    st.session_state.messages = []


# previous msg

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])



# input box

question = st.chat_input(
    "Ask ChatMate anything..."
)


# process question

if question:

    with st.chat_message("user"):

        st.markdown(question)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )


    # generate Ai response

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = agent.invoke(
                    {
                        "messages": [
                            {
                                "role": "user",
                                "content": question
                            }
                        ]
                    }
                )

                answer = response["messages"][-1].content

                st.markdown(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            except Exception as e:

                error_message = (
                    f"Something went wrong:\n\n"
                    f"`{str(e)}`"
                )

                st.error(error_message)