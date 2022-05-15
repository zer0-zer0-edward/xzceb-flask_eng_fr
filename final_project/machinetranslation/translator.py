"""
This Python file instantiates all required packages for the
IBM Language Translator service to function.
"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

""" Load environment parameters from the .env file """
load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

""" Load IBM Language Translator """
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('{APIKEY}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

""" Instantiate the IBM Language Translator Service """
language_translator.set_service_url('{URL}')

""" Test - list all supported languages for translation """
languages = language_translator.list_languages().get_result()
print(json.dumps(languages, indent=2))

""" This function will translate English to French """
def englishToFrench(englishText):
    # write the code here 
    text_to_translate = language_translator.translate(text=englishText, 
                                                      model_id='en-fr').get_result()
    json_response = json.dumps(text_to_translate, indent=2, ensure_ascii=False)
    frenchText = json_response["translations"]["translation"]
    return frenchText
    
""" This function will translate French to English """
def frenchToEnglish(frenchText):
    # write the code here 
    text_to_translate = language_translator.translate(text=frenchText, 
                                                      model_id='fr-en').get_result()
    json_response = json.dumps(text_to_translate, indent=2, ensure_ascii=False)
    englishText = json_response["translations"]["translation"]
    return englishText
    