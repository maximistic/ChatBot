import requests
import time

API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {"Authorization": "Bearer your_token_from_hugginface"}     #the token should be of the form "Bearer token_from_huggingface" - do not ignore "Bearer".

def query(payload, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.post(API_URL, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
            else:
                print("Chatbot: I'm having trouble responding right now. Let's try again!")
                return None

def chatbot():
    print("Chatbot: Hello! I'm a chatbot powered by BlenderBot. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye! I hope you have a great day. Take care.")
            break
        
        response = query({
            "inputs": user_input,
            "parameters": {"max_length": 100, "temperature": 0.7}
        })
        
        if response and isinstance(response, list) and len(response) > 0:
            if 'generated_text' in response[0]:
                print("Chatbot:", response[0]['generated_text'].strip())
            else:
                print("Chatbot: I'm not sure how to respond to that. Can you try asking something else?")
        else:
            print("Chatbot: I'm having trouble understanding. Could you rephrase that?")

if __name__ == "__main__":
    chatbot()
