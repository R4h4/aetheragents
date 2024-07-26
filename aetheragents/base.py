import openai
from typing import List, Optional
from config.settings import AI_API_KEY, AI_ENDPOINT_URL, AI_DEFAULT_MODEL


class Agent:
    def __init__(
            self,
            model_name: str, prompt: str, system_prompt: str = None, endpoint_url: str = None, api_key: str = None
    ):
        self.endpoint_url = endpoint_url or AI_ENDPOINT_URL
        self.api_key = api_key or AI_API_KEY
        self.model_name = model_name or AI_DEFAULT_MODEL
        self.prompt = prompt
        self.system_prompt = system_prompt

        # Configure OpenAI client
        openai.api_key = self.api_key
        openai.api_base = self.endpoint_url

    def process(self, **kwargs) -> str:
        # Fill in the placeholders in the prompt
        filled_prompt = self.prompt.format(**kwargs)

        # Prepare messages for the API call
        messages = []
        if self.system_prompt:
            messages.append({"role": "system", "content": self.system_prompt})
        messages.append({"role": "user", "content": filled_prompt})

        # Make the API call
        response = openai.ChatCompletion.create(
            model=self.model_name,
            messages=messages
        )

        # Extract and return the generated text
        return response.choices[0].message.content.strip()


# Example usage
if __name__ == "__main__":
    endpoint_url = "https://api.openai.com/v1"
    api_key = "your_api_key_here"
    model_name = "gpt-3.5-turbo"
    prompt = "Translate the following English text to {}: '{}'"
    system_prompt = "You are a helpful assistant that translates English to other languages."

    translator_agent = Agent(endpoint_url, api_key, model_name, prompt, system_prompt)

    result = translator_agent.process("French", "Hello, how are you?")
    print(result)