from model.message_model import personalize_message, sanitize_phone_number
import webbrowser
import urllib.parse
import time

import pywhatkit

def send_whatsapp_message(name: str, phone: str, message_template: str):
    personalized_message = personalize_message(message_template, {"name": name})
    pywhatkit.sendwhatmsg_instantly(phone, personalized_message, wait_time=10, tab_close=True)

def open_whatsapp_link(phone: str, message: str):
    encoded_message = urllib.parse.quote(message)
    link = f"https://wa.me/{phone}?text={encoded_message}"
    print(f"📤 Opening WhatsApp chat: {link}")
    webbrowser.open(link)
    time.sleep(3) 

def send_bulk_messages(contacts, template):
    for contact in contacts:
        try:
            clean_data = {k: (v or "") for k, v in contact.items()}
            cleaned_phone = sanitize_phone_number(clean_data.get("phone", ""))

            if not cleaned_phone:
                print(f"⚠️ Skipped {contact.get('name', 'Unknown')} - invalid phone number")
                continue

            message = personalize_message(template, clean_data)
            print(f"✅ Opening chat for {contact['name']} at {cleaned_phone}")
            open_whatsapp_link(cleaned_phone, message)

        except Exception as e:
            print(f"❌ Failed for {contact.get('name', 'Unknown')} - {e}")

def send_whatsapp_message(name: str, phone: str, message_template: str):
    personalized_message = personalize_message(message_template, {"name": name})
    cleaned_phone = sanitize_phone_number(phone)
    if not cleaned_phone:
        raise ValueError("Invalid phone number.")
    pywhatkit.sendwhatmsg_instantly(cleaned_phone, personalized_message, wait_time=10, tab_close=True)