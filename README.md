# BlenderBot Chatbot
This my take at a Simple Chatbot powered by the BlenderBot model from facebook (meta) AI, accessed using the Inference API (of huggingface). This chatbot can handle basic conversational interactions including retry logic to handle temporary network issues or understanding issues.

## Features

  1. **Conversational AI** - Uses the BlenderBot-400M-distill model to generate responses
  2. **Retry Mechanism** - To handle network related issues

## Setup
  1. Clone this repository
     * git clone https://github.com/maximistic/Chatbot.git
     * cd BlenderBot
  2. Install the required dependencies.
     * pip install requests
  3. Set your Hugging Face API token in the headers variable in the script.
     * headers = {"Authorization": "Bearer YOUR_HUGGING_FACE_API_TOKEN"}
