import tkinter as tk
from tkinter import messagebox
from controller.message_controller import send_whatsapp_message

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

    root = tk.Tk()
    root.title("WhatsApp Sender 💬")
    root.geometry("400x350")

    tk.Label(root, text="Recipient Name").pack(pady=5)
    name_entry = tk.Entry(root, width=40)
    name_entry.pack()

    tk.Label(root, text="Phone Number (+62...)").pack(pady=5)
    phone_entry = tk.Entry(root, width=40)
    phone_entry.pack()

    tk.Label(root, text="Message (use {name} for personalization)").pack(pady=5)
    message_entry = tk.Text(root, height=6, width=40)
    message_entry.pack()

    tk.Button(root, text="Send Now Instantly 🚥", command=on_send).pack(pady=20)

    root.mainloop()