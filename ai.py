import openai
from decouple import config

openai.api_key = config("OPENAI_API_KEY")
def ai(prompt):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.95,
            max_tokens=3900,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        data = str(response.choices[0].text)
        return data
    except Exception as e:
        return "Something went wrong"