import openai
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv('API_KEY')

# Set the API key for OpenAI
openai.api_key = api_key

# create a chat completion 

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Listen to your"}
    ],
    max_tokens = 2, # ajusta o número máximo de tokjens permitidos na response.
    n = 5 , # controla o número de respostas enviadas de volta no modelo
    temperature = 2
)

# Convert the response to a dictionary and print it
#response_dict = response.to_dict()

#print(response_dict)

#print(response.choices[0].message.content)

# The first OUTPUT, without any parameters for adjust the response: heart and trust your instincts. They will guide you in the right direction. 
# Trust in yourself and have faith in your decisions. It's important to stay true to yourself and listen 
# o what truly brings you happiness and fulfillment. Trust in your own intuition and stay true to your 
# values and beliefs. Remember to always follow your heart and trust your instincts, they will never steer you wrong.

for i in range(len(response.choices)):
    print(response.choices[i].message.content)
