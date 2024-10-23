import PIL.Image
import google.generativeai as genai
from model_settings import safety_settings
from model_settings import model_name
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Configure the generative AI model
genai.configure(api_key=os.environ["API_KEY"])

# Create the generative model with safety settings
model = genai.GenerativeModel(
    model_name=model_name,
    safety_settings=safety_settings,
)

# In the string below, add the image's file name.
# It needs to include the extension, for example, interior_design.jpg.
sample_file = PIL.Image.open("")

# Edit the string below to send a prompt about the picture.
prompt = ""

response = model.generate_content([prompt, sample_file])

print(response.text)