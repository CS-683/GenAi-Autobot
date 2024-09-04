from llms import Gemini
from dotenv import load_dotenv
from os import environ

load_dotenv()

project = environ.get("VERTEXAI_PROJECT")
location = environ.get("VERTEXAI_LOCATION")
api_key = environ.get("VERTEXAI_API_KEY")
model_name = environ.get("VERTEXAI_MODEL")

print([project, location, api_key, model_name])

gemini = Gemini()

gemini.setup(project, location, api_key, model_name)

response = gemini.generate_content("hello, can you read this?")

print(response)

