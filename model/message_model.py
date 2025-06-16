def personalize_message(template: str, name: str) -> str:
    return template.replace("{name}", name)