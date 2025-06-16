import csv

def load_contacts_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames
        contacts = [row for row in reader if any(row.values())]  # skip empty rows
    return headers, contacts

