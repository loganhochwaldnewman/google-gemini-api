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
    safety_settings=safety_settings
)

# Create a function
    # It will get user input and store the conversation history in a list

# List to store the conversation

# Create while loop

# Get user input for the prompt


# Exit the loop if the user types "exit"


# Generate AI response


# Store the user input and AI response in the conversation list


# Display the AI response

# Call the method