# NVIDIA Llama-3.1-Nemotron-70B-Instruct Chatbot

This project is a Python-based chatbot that utilizes the NVIDIA Llama-3.1-Nemotron-70B-Instruct model. The chatbot allows users to interact with the model through a command-line interface, providing responses to user prompts.

## Features

- Interactive chat loop for continuous conversation.
- Utilizes NVIDIA's API with OpenAI-compatible interface.
- Supports environment variable configuration for API keys.

## Prerequisites

- Python 3.6 or higher
- NVIDIA API key

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/nvidia-chatbot.git
   cd nvidia-chatbot
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**

   Create a `.env` file in the root directory of the project and add your NVIDIA API key:

   ```plaintext
   NVIDIA_API_KEY=your_api_key_here
   ```

## Usage

Run the chatbot using the following command:
