from .llm import LLM
import vertexai
from vertexai.generative_models import GenerativeModel

class Gemini(LLM):
    def setup(self, poject:str, location:str, api_key:str, model_name:str):
        vertexai.init(project=poject, location=location, api_key=api_key)
        self.model = GenerativeModel(model_name)
        return super().setup()

    def generate_content(self, prompt):
        return self.model.generate_content(prompt)
    
