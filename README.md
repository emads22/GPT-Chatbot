# GPT Chatbot

## Overview
GPT Chatbot is a Python GUI application powered by OpenAI's GPT models, built using `PyQt6`. It allows users to interact with the chatbot by sending messages and receiving responses generated by the AI. The application supports different GPT models, providing flexibility in response generation based on user preferences.

## Features
- **Message Sending**: Users can send messages to the chatbot.
- **Response Generation**: The chatbot generates responses to user messages using OpenAI's GPT models.
- **User Interface**: The application provides a graphical user interface for interacting with the chatbot.
- **Responsive Input**: The GUI is responsive to the Enter key being pressed, allowing users to send messages quickly.

## Technologies Used
- **openai**: A library for accessing OpenAI's GPT-3 and GPT-4 models.
- **PyQt6**: A set of Python bindings for the Qt application framework.
- **python-dotenv**: A library for managing environment variables in .env files.
- **threading**: A module for creating and managing threads in concurrent programming.

## Setup
1. Clone the repository.
2. Ensure Python 3.x is installed.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Configure the necessary parameters such as `OPENAI_API_KEY`, `GPT_MODEL`, `TOKENS`, and `TEMPERATURE` in `constants.py`.
   - Update `GPT_MODEL` to change the GPT model used by the chatbot.
   - Adjust `TOKENS` to set the maximum number of tokens (words) allowed in the response.
   - Set `TEMPERATURE` to control the randomness of the response generation.
5. Run the script using `python main.py`.

## Usage
1. Run the script using `python main.py`.
2. Type your message in the input field and press Enter or click the Send button to send it to the chatbot.
3. The chatbot will generate a response to your message and display it in the chat area.
4. You can continue the conversation by sending more messages and receiving responses from the chatbot.

## Threading
The application uses threading to handle API requests for generating responses from the chatbot. By running API requests in separate threads, the main GUI thread remains responsive, preventing the application from becoming unresponsive or laggy while waiting for a response from the server. This improves the user experience and ensures smooth interaction with the chatbot. Threading also allows the application to handle multiple user inputs and responses concurrently, enabling a more fluid conversation experience.

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.