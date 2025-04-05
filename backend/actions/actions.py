# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
# actions.py

from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet
import datetime

class ActionTellTime(Action):

    def name(self) -> str:
        return "action_tell_time"  # This name must match what's in domain.yml

    def run(self, dispatcher: CollectingDispatcher,
            tracker,
            domain: DomainDict) -> list:
        
        # Get current system time
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")  # Example: "03:45 PM"

        # Send the response to user
        dispatcher.utter_message(text=f"The current time is {current_time}")

        return []

