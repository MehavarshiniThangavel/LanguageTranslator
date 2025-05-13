# 🌍 LangChain Translator Bot

This is a simple and interactive command-line translator built using:

- 🧠 *LangChain* + *OpenAI* LLM
- 🌐 Translates any word into any language
- 🛠 Python script with dynamic prompt templates

---
## 🚀 Features

- Translate any English word into your desired language
- Simple terminal-based interaction
- Built with LangChain’s prompt template system
- Uses .env for API key security

---
## 📁 Project Structure

langchain_translator_bot/
    translator_bot.py # Main Python script
    .env # Stores your OpenAI API key
    requirements.txt # Python dependencies


1. Create a Virtual Environment (optional)

  python -m venv venv
  source venv/bin/activate 

2. Install Requirements
.txt file include
(txt
Copy code
langchain
openai
python-dotenv)

  pip install -r requirements.txt

3. Add OpenAI API Key
   Create a .env file in the root directory and paste your API key:

4.Run
python translator_bot.py

Sample interaction:

Welcome to the LangChain Translator Bot!
Enter a word to translate: hello
Translate to which language?: French
Translation: bonjour
🧠 Example Languages
French
German
Hindi
Tamil
Arabic
Any other supported by OpenAI!

-----------------
