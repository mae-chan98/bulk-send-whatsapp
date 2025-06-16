import tkinter as tk
from tkinter import filedialog, messagebox
from controller.message_controller import send_whatsapp_message, send_bulk_messages
from model.contact_model import load_contacts_from_csv

loaded_headers = []
loaded_contacts = []


def start_app():
    def on_send():
        name = name_entry.get().strip()
        phone = phone_entry.get().strip()
        message_template = message_entry.get("1.0", tk.END).strip()

        if not name or not phone or not message_template:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            send_whatsapp_message(name, phone, message_template)
            messagebox.showinfo("Sent", f"Message sent instantly to {name}!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def on_load_csv():
        global loaded_headers, loaded_contacts
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return
        try:
            headers, contacts = load_contacts_from_csv(file_path)
            loaded_headers = headers
            loaded_contacts = contacts
            header_display.config(state="normal")
            header_display.delete("1.0", tk.END)
            header_display.insert(tk.END, ", ".join(headers))
            header_display.config(state="disabled")
            messagebox.showinfo("CSV Loaded", f"Loaded {len(contacts)} contacts.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV: {e}")

    def on_send_bulk():
        message_template = message_entry.get("1.0", tk.END).strip()
        if not loaded_contacts or not message_template:
            messagebox.showerror("Error", "Please load a CSV file and enter a message template.")
            return
        try:
            send_bulk_messages(loaded_contacts, message_template)
            messagebox.showinfo("Bulk Sent", f"Messages sent to {len(loaded_contacts)} contacts.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    root = tk.Tk()
    root.title("WhatsApp Sender 💬")
    root.geometry("450x500")

    tk.Label(root, text="Recipient Name").pack(pady=2)
    name_entry = tk.Entry(root, width=40)
    name_entry.pack()

    tk.Label(root, text="Phone Number (+62...)").pack(pady=2)
    phone_entry = tk.Entry(root, width=40)
    phone_entry.pack()

    tk.Label(root, text="Message Template (use {name}, etc.)").pack(pady=2)
    message_entry = tk.Text(root, height=6, width=50)
    message_entry.pack()

    tk.Button(root, text="Send Now Instantly 💥", command=on_send).pack(pady=10)

    tk.Label(root, text="--- OR ---").pack()

    tk.Button(root, text="📂 Load CSV", command=on_load_csv).pack(pady=5)

    tk.Label(root, text="CSV Headers (use in template):").pack(pady=2)
    header_display = tk.Text(root, height=2, width=50, state="disabled")
    header_display.pack()

    tk.Button(root, text="📤 Send to All in CSV", command=on_send_bulk).pack(pady=10)

    root.mainloop()

