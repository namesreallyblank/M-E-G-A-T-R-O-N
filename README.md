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
   git clone https://github.com/namesreallyblank/NVIDIA-3.1-Nemotron-CLI-Chatbot.git
   cd NVIDIA-3.1-Nemotron-CLI-Chatbot
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

   Obtain your NVIDIA Nemotron API key by visiting [NVIDIA Build](https://build.nvidia.com/nvidia/llama-3_1-nemotron-70b-instruct) and create a `.env` file in the root directory of the project to add your API key:

   ```plaintext
   NVIDIA_API_KEY=your_api_key_here
   ```

## Usage

Run the chatbot using the following command:

```bash
python main.py
```

- Type your prompts into the console.
- Type `exit` to end the conversation.

## Code Overview

- **main.py**: Contains the main logic for the chatbot, including the chat loop and response generation.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- NVIDIA for providing the Llama-3.1-Nemotron-70B-Instruct model.
- OpenAI for the API interface.
