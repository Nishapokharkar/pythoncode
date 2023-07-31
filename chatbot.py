import nltk
from nltk.chat.util import Chat, reflections
responses = {
    "hi": "Hello! How can I assist you today?",
    "how are you doing?": "I'm doing well, thank you.",
    "what is your name": "I'm a chatbot .",
    "can you help me?":"Sure, I'd be happy to help with your chatbot!"
    
}
pairs = [
    [r"(.*)hi(.*)", ["Hello! How can I assist you today?"]],
    [r"(.*)how are you doing?(.*)", ["I'm doing well, thank you."]],
    [r"(.*)what is your name(.*)", ["I'm a chatbot."]],
    [r"(.*)can you help me?(.*)", ["I'd be happy to help with your chatbot!"]]
]

chatbot = Chat(pairs, reflections)

def chat_with_user():
    print("Hello! I'm your chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'exit':
            print("Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print("Chatbot:", response)


chat_with_user()
