from llm import Gemini
from dotenv import load_dotenv
from os import environ
from google.cloud import aiplatform

# service_account = "./genai-436917-85e0d288c017.json"

load_dotenv()

project = environ.get("VERTEXAI_PROJECT")
location = environ.get("VERTEXAI_LOCATION")
model_name = environ.get("VERTEXAI_MODEL")


gemini = Gemini()

gemini.initialize(project, location, model_name)

response = gemini.generate_content("hello, can you read this?")

print(response)

