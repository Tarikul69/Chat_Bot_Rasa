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



from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import datetime

class ActionTellTime(Action):

    def name(self) -> Text:
        return "action_tell_time"  # This must match the name in domain.yml

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> List[Dict[Text, Any]]:

        # Get the current system time
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")  # Example: "03:45 PM"

        # Send response to the user
        dispatcher.utter_message(text=f"The current time is {current_time}")

        return []
    
class PlaceOrder(Action):
    def name(self) -> Text:
        return "action_place_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> List[Dict[Text, Any]]:
        
        # Extract order details from the tracker
        order_details = tracker.get_slot("order_details")
        
        # Here you would typically process the order (e.g., save to a database)
        # For demonstration, we'll just log it
        print(f"Order placed: {order_details}")

        # Send confirmation message to the user
        dispatcher.utter_message(text=f"Your order for {order_details} has been placed successfully!")

        return []

