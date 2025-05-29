from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Dictionary to store chat sessions using session IDs as keys
sessions = {}

def get_session(session_id: str) -> BaseChatMessageHistory:
    if session_id not in sessions:
        sessions[session_id] = ChatMessageHistory()  # Initialize new session if not found
    return sessions[session_id]

# Ensure 'model' is defined before using it; otherwise, this will raise a NameError.
# This wraps the model with history management to maintain chat context.
chat_message_history_model = RunnableWithMessageHistory(model, get_session)

# Configuration dictionary containing the session ID
config = {'configurable': {'session_id': "Rama01VJ1"}}

# Invokes the model with a user message while maintaining session history
chat_message_history_model.invoke(
    [HumanMessage(content="Hi, This is Rama Suresh and I am an AI engineer.")],
    config=config
)