import os
from google import genai

# 1. Initialize your GenAI client
client = genai.Client(
    vertexai=True,
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION"),
)

# 2. List available models (page_size is optional)
for model in client.models.list(config={"page_size": 50}):
    if model.name.startswith("publishers/google/models/image"):
        print(model)
