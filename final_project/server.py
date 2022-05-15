"""
This Python file is for the flask server
"""

from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    frenchText = translator.englishToFrench(textToTranslate)
    return f"Translated text to French: {frenchText}"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    englishText = translator.frenchToEnglish(textToTranslate)
    return f"Translated text to English: {englishText}"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
