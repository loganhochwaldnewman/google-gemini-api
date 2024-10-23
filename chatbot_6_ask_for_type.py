import google.generativeai as genai
from model_settings import safety_settings
from model_settings import model_name
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Configure the generative AI model
genai.configure(api_key=os.environ["API_KEY"])

# Ask the user what kind of chatbot they want
chatbot_type = input("")

# Put the answer to the prompt into system_instruction. You will need an F-string.
model = genai.GenerativeModel(
    model_name=model_name,
    safety_settings=safety_settings,
    system_instruction=""
)

# while loop

    # Get user input


    # Check if the user wants to stop

    # Generate a response

