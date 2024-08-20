import vertexai
from vertexai.generative_models import GenerativeModel

vertexai.init(project="genai-autobot", location="us-central1", api_key="AIzaSyBmot9U2-3cuT_dDLSyg8pmedIBpkeQPgo")

model = GenerativeModel("publishers/meta/models/llama3-405b-instruct-maas")
# model = GenerativeModel("gemini-1.5-flash-001")
print(model.generate_content("Why is sky blue?"))
