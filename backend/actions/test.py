####################################
#########Connect llm to rasa########
####################################
import sys
import os
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from .local_llm import ask_llm

class ActionAskLLM(Action):
    def name(self):
        return "action_ask_llm"

    def run(self, dispatcher, tracker, domain):
        user_input = tracker.latest_message.get("text")
        llm_response = ask_llm(user_input)
        dispatcher.utter_message(text=llm_response)
        return []