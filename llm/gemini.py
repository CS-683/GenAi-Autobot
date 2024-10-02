from .llmAbs import LLMAbs
import vertexai
from vertexai.generative_models import GenerativeModel, SafetySetting, Part
from google.api_core.exceptions import GoogleAPIError


class Gemini(LLMAbs):
    generation_config = {
        "max_output_tokens": 8192,
        "temperature": 1,
        "top_p": 0.95,
    }

    safety_settings = [
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
    ]

    def initialize(self, project: str, location: str, model_name: str):
        try:
            vertexai.init(project=project, location=location)
            self.model = GenerativeModel(model_name)
            return super().initialize()
        except GoogleAPIError as e:
            print(f"Error initializing Gemini model: {e}")
            return False  # Indicate failure

    def generate_content(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(
                prompt,
                generation_config=self.generation_config,
                safety_settings=self.safety_settings,
            )
            return response.text  # Use response.text for direct access to the generated text

        except GoogleAPIError as e:
            print(f"Error generating content: {e}")
            return ""  # Return empty string on error

        except AttributeError as e:
            print(f"Error accessing response content: {e}.  Is the model initialized correctly?")
            return ""
