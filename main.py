import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up the client with NVIDIA's API endpoint
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.environ.get("NVIDIA_API_KEY")
)

def generate_response(prompt, max_tokens=1024, temperature=0.7):
    try:
        completion = client.chat.completions.create(
            model="nvidia/llama-3.1-nemotron-70b-instruct",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature,
            stream=True
        )

        # Print the response as it's generated
        full_response = ""
        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                print(content, end="", flush=True)
                full_response += content
        
        print("\n")  # Add a newline at the end
        return full_response

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def chat_loop():
    print("Welcome to the NVIDIA Llama-3.1-Nemotron-70B-Instruct chat!")
    print("Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        print("\nAssistant:", end=" ")
        response = generate_response(user_input)
        if not response:
            print("I'm sorry, I couldn't generate a response. Please try again.")

# Example usage
if __name__ == "__main__":
    chat_loop()
