import openai


class Agent:
    def __init__(
        self,
        model_name: str,
        prompt: str,
        system_prompt: str = None,
        endpoint_url: str = None,
        api_key: str = None,
    ):
        self.model_name = model_name
        self.prompt = prompt
        self.system_prompt = system_prompt

        # Configure OpenAI client
        if api_key:
            openai.api_key = api_key
        if endpoint_url:
            openai.api_base = endpoint_url

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
            model=self.model_name, messages=messages
        )

        # Extract and return the generated text
        return response.choices[0].message.content.strip()
