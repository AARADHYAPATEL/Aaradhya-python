import speech_recognition as sr
import pyttsx3
import requests
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from transformers import pipeline, T5Tokenizer, T5ForConditionalGeneration

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
nltk.download('punkt', force=True)
nltk.download('averaged_perceptron_tagger', force=True)
nltk.download('wordnet', force=True)

# Initialize the lemmatizer and paraphrasing model
lemmatizer = WordNetLemmatizer()
tokenizer = T5Tokenizer.from_pretrained("Vamsi/T5_Paraphrase_Paws")
model = T5ForConditionalGeneration.from_pretrained("Vamsi/T5_Paraphrase_Paws")

# Storage for user inputs
user_inputs = []

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_user_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

def fetch_wikipedia_summary(query):
    url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch={query}&utf8=&srlimit=1"
    response = requests.get(url).json()

    if response['query']['search']:
        title = response['query']['search'][0]['title']
        snippet = response['query']['search'][0]['snippet']
        clean_snippet = snippet.replace('<span class="searchmatch">', '').replace('</span>', '')
        return f"{title}: {clean_snippet}"
    return "Sorry, I couldn't find anything on that topic."

def process_input(user_input):
    tokens = word_tokenize(user_input)
    tagged = pos_tag(tokens)
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]  # Lemmatization
    return lemmatized_tokens

def paraphrase_text(text):
    inputs = tokenizer.encode("paraphrase: " + text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=512, num_beams=5, early_stopping=True)
    paraphrased_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return paraphrased_text

def calculate_expression(expression):
    url = "http://api.mathjs.org/v4/"
    headers = {"Content-Type": "application/json"}
    data = {"expr": expression}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()['result']
    else:
        return "Error in calculation."

def main():
    speak("Hello! Ask me anything.")

    while True:
        user_input = get_user_input()
        if user_input is None:
            continue

        if "exit" in user_input or "goodbye" in user_input:
            speak("Goodbye! Have a great day!")
            break
        elif "calculate" in user_input:
            expression = user_input.replace("calculate", "").strip()
            result = calculate_expression(expression)
            speak(f"The result is {result}")
        else:
            # Store the user input
            user_inputs.append(user_input)

            # Process the user input with NLTK
            lemmatized_query = process_input(user_input)
            query = " ".join(lemmatized_query)  # Convert list back to string

            # Fetch summary from Wikipedia
            summary = fetch_wikipedia_summary(query)

            # Paraphrase the summary
            paraphrased_summary = paraphrase_text(summary)
            speak(paraphrased_summary)

if __name__ == "__main__":
    main()