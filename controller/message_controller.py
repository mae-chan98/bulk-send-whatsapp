from model.message_model import personalize_message
import pywhatkit

def send_whatsapp_message(name: str, phone: str, message_template: str):
    personalized_message = personalize_message(message_template, name)
    pywhatkit.sendwhatmsg_instantly(phone, personalized_message, wait_time=10, tab_close=True)