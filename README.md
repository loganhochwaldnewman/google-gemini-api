# Create Your Own Chatbots

## Setup

This guide will help you get started with setting up your project by selecting the correct Python interpreter, creating a virtual environment, and managing your API keys.

### Step 1: Get an API Key
You will need an API key for this project. After obtaining your API key, you will store it in a `.env` file for security purposes.

1. **Get your API key**: Obtain the API key from me.
2. **Create a `.env` file**: In your project folder, create a new file named `.env`. This file will store sensitive information like your API key.
3. **Add your API key**: Open the `.env` file and add your API key. It should look just like the example file, `.env.example`

This format ensures that your key is securely stored and can be accessed by your application without hardcoding it into your codebase.

### Step 2: Set Up a Python Virtual Environment
Creating a virtual environment ensures that the dependencies for this project are isolated from other Python projects on your system.

1. Open your terminal in VSCode. Make sure it's in the proper project directory.
2. Create a virtual environment by running the following command:
  ```
    python -m venv env
  ```
This will create a folder named `env` that contains the virtual environment files.

3. **Activate the virtual environment**:
  ```
  source env/bin/activate
  ```

4. To deactivate the environment when you're done working:
  ```
    deactivate
  ```

### Step 3: Select the Python Interpreter in VSCode
It’s important to configure VSCode to use the correct Python interpreter for your project, especially after setting up a virtual environment.

1. **Open the Command Palette**:
- Raspberry Pi: Press `Control + Shift + P`
- macOS: Press `Cmd + Shift + P`

2. **Select the Python interpreter**:
- In the Command Palette, start typing `Python: Select Interpreter`. VSCode will auto-complete the command for you.
- From the list of available interpreters, choose **Python 3.11.2** (or the version installed in your environment).

This ensures VSCode will use the correct Python version from your virtual environment to run your code.
Now that you've configured your environment, you're ready to start coding and using the API!

### Step 4: Install the Libraries
- You only need to run this once:
  ```
    pip install -r requirements.txt
  ```
This installs the libraries required for this code.

---

## Problems

*DO NOT SPAM THE CHATBOT REQUESTS!*
You are allowed a certain amount per day. This is the [current pricing](https://ai.google.dev/pricing#1_5flash).

### `chatbot_1_basic.py`
The file has been done for you. The lines that you need to understand are:
```
response = model.generate_content("I'm learning how to use AI!")
print(response.text)
```
- When you press play, look at the response you get in the terminal.
- Now, edit the code so that you get a response about giraffes.
- Add a comment at the bottom of the file that explains what you did.

**It is okay if you get an error in your code! Undo it and try again; this is supposed to be fun and exploratory.**

### `chatbot_2_history.py`
You will be storing the chat history in a list. Follow along with the comments to complete this file.
You will need to use an [F-String](https://www.w3schools.com/python/python_strings_format.asp)

### `chatbot_3_personality.py`
The file has been done for you. The new line that you need to understand is:
```
    system_instruction="You are another student who is learning Python but you are optimistic about the learning process. You should give me reassurance when I don't understand something. Don't offer to help."
```
- Send a response and see what it says. Does it say anything about Python?
- If it doesn't, what could you say to get a response about Python?
- Now change the personality of the bot and send the same prompt you sent earlier. Is there a different personality it's taken on?
- Change it to respond as your favourite celebrity. Ask it specific questions about the celebrity to see if it responds properly.
- Make your prompt even more detailed to make the response even better. In a comment at the bottom of the file, tell me what you changed about your prompt to make it better.

### `chatbot_4_image.py`
You can send images to the Google Gemini API!
- Go to [unsplash](https://unsplash.com/) and find an image you like.
- Download it and name it something relevant.
- Move that picture into this project. You should see it in the list of files on the left.
- Follow along with the comments in the file. You should be able to send a picture with a prompt about it.
- Optional Challenge: Can you figure out how to ask the user for a picture? You will need to do some googling and you might need to install a new library.

### `chatbot_5_speech.py`
This has been done for you. This one is more complicated, so I won't have you change anything.
- Look at the code and put descriptive comments for what each line is doing. If you don't know, use Google to try and figure it out.

### `chatbot_6_ask_for_type.py`
Follow along with the comments to ask the user for the chatbot personality. You'll set that as the setting, and then use a while loop
to have them converse with AI until they indicate that they'd like to stop.

### `chatbot_7_tkinter.py`
This has been done for you. Run it and notice what is going on. Add a comment at the bottom of the file describing what you think is happening.
- Edit the code so that the new window looks completely different. Even if you don't understand the tkinter library, you can still figure out what it is doing.
- For example, Arial is a font name. If you used a different font name, what do you think would happen?


### Issues:
There was an issue on the rapsberry pis where they could not handle unicode characters in the terminal. This was the fix:
- Open a pi terminal.
- Run `nano ~/.bashrc`
- At the bottom of the file, write:
  ```
  # Unicode Encoding Python Terminal
  export PYTHONIOENCODING=utf-8
  ```
- Hit: CTRL + X, Y, Enter
- In the same terminal, run: `sudo apt-get install fonts-noto-color-emoji`
- In VSCode, open the settings by hitting: CTRL + ,
- In the font option, it should be edited to say: 'Droid Sans Mono', 'monospace', monospace, 'Droid Sans Fallback', 'Noto Color Emoji'
- Closing VSCode and re-opening it should now show emojis and not throw errors when trying to print unicode characters.