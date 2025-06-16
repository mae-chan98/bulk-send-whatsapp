def personalize_message(template: str, data: dict) -> str:
    if not data or not isinstance(data, dict):
        raise ValueError("Personalization data is missing or not a dictionary.")
    

    message = template
    for key, value in data.items():
        message = message.replace(f"{{{key}}}", str(value or ""))

    return message


def sanitize_phone_number(phone) -> str:
    if phone is None:
        return ""

    # Ensure it's a string
    phone = str(phone).strip().lstrip('+')

    # Fix local Indonesian format like 08xx → 628xx
    if phone.startswith('0'):
        phone = '62' + phone[1:]

    # Reject anything not starting with 62 or not all digits
    if not phone.startswith('62') or not phone.isdigit():
        print(f"Error at processing phone number: {phone}")
        # return ""

    return phone

