import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv('OPEN_AI_API_KEY')

def chatgpt_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=2000
    )
    response_dict = response.get("choices")
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]["text"]
    return prompt_response