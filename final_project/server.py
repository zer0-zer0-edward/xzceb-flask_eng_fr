"""
This Python file is for the flask server
"""

from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    """ This function uses the translator package on the webpage """
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    frenchText = translator.english_to_french(textToTranslate)
    return f"Translated text to French: {frenchText}"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    """ This function uses the translator package on the webpage """
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    englishText = translator.french_to_english(textToTranslate)
    return f"Translated text to English: {englishText}"

@app.route("/")
def renderIndexPage():
    """ This function renders the webpage template using index.html """
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
