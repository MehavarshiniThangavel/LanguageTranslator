import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Load the API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Set up OpenAI LLM
llm = OpenAI(openai_api_key=api_key, temperature=0)

# Create a prompt template
prompt = PromptTemplate(
    input_variables=["word", "language"],
    template="Translate the word '{word}' into {language}. Only return the translated word."
)

# Interactive loop
print("Welcome to the LangChain Translator Bot!")
print("Type 'exit' anytime to quit.\n")

while True:
    word = input("Enter a word to translate: ").strip()
    if word.lower() == "exit":
        break

    language = input("Translate to which language?: ").strip()
    if language.lower() == "exit":
        break

    # Format the prompt
    formatted_prompt = prompt.format(word=word, language=language)

    # Get translation from OpenAI
    translation = llm(formatted_prompt)

    print(f"Translation: {translation.strip()}\n")