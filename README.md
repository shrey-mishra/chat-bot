OpenAI Virtual Assistant Chatbot

This project implements a simple chatbot using OpenAI's API. The chatbot saves conversation history to a text file and allows continuous interaction until the user types 'quit'.

Features
-Sends messages to an OpenAI assistant and retrieves responses.
-Saves the conversation history to a text file with timestamps.
-Provides a continuous conversation loop for user interaction.

Prerequisites
-Python 3.x
-openai Python package
-python-dotenv package for loading environment variables


Installation
1. Clone the repository:
git clone https://github.com/yourusername/openai-chatbot.git
cd openai-chatbot

2.Install the required packages:
pip install openai python-dotenv

3.Create a .env file in the project directory to store your OpenAI API key and any other environment variables:
touch .env
Add your OpenAI API key to the .env file:
OPENAI_API_KEY=your_openai_api_key

4.Ensure you have the keys.py file in the project directory containing the thread_id and assistant_id:
# keys.py
thread_id = "your_thread_id"
assistant_id = "your_assistant_id"

USAGE
1.Run the chatbot script:
python chatbot.py

2.Enter your messages when prompted. Type quit to exit the conversation.

Contributing
Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
