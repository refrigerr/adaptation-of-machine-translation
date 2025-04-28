import requests
import json

class LLM:
    
    def __init__(self, model_id, key_path):
        self.MODEL_ID = model_id
        self.COMPLETIONS_ENDPOINT = "https://services.clarin-pl.eu/api/v1/oapi/chat/completions"
        with open(key_path, "r") as file:
            self.API_KEY_CLARIN = file.read().strip()

    def prompt_chat_custom_temperature(self, prompt, temperature = 0.3):
        url = self.COMPLETIONS_ENDPOINT
        headers = {"Authorization": f"Bearer {self.API_KEY_CLARIN}", "Content-Type": "application/json"}
        messages = []
        messages.append({"role": "user", "content": prompt})
        data = {
            "model": self.MODEL_ID,
            "messages": messages,
            "temperature": temperature
        }
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            try:
                data = response.json()
                if isinstance(data, dict) and "choices" in data and data["choices"]:
                    return data["choices"][0].get("message", {}).get("content", None)
                else:
                    return None  # Handle unexpected response structure
            except (ValueError, TypeError, AttributeError):
                return None  # Handle cases where response.json() is None or not as expected
        else:
            return None  # Handle non-200 status codes