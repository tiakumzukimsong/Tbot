# import re 

# def chat_response(response):

#     responses={
#         "hello": "Hi, How can i help you?",
#         "bye": "Goodbye! Have a nice day!",
#         "how are you": "I'm just a bot, but I'm doing great! How about you?"

#     }

#     for pattern,response2 in  responses.items():
#         if re.search(pattern,response, re.IGNORECASE):
#             return response2
        
#     return "I'm sorry, I don't understand that"

# def main():
#     print("Tbot: Hi! I am your assistant. Type 'bye' to exit.")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == "bye":
#             print("Tbot: Goodbye! Have a nice day!")
#             break
#         response = chat_response(user_input)
#         print(f"Tbot: {response}")

# if __name__ == "__main__":
#     main()


from transformers import pipeline

# Load pre-trained model
chatbot = pipeline('conversational', model='microsoft/DialoGPT-medium')

def chat():
    print("Chatbot: Hi! I am your assistant. Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = chatbot(user_input)
        print(f"Chatbot: {response[0]['generated_text']}")

if __name__ == "__main__":
    chat()
