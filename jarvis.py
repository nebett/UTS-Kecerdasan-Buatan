import aiml
import os
import threading
from tkinter import *

# =========================
# MEMBUAT BOT
# =========================
bot = aiml.Kernel()
bot.learn("chatbot.aiml")

# =========================
# FUNGSI SUARA
# =========================
def suara(jawaban):
    os.system(f'espeak.exe -s 100 -ven+f2 "{jawaban}"')

# =========================
# FUNGSI KIRIM PESAN
# =========================
def kirim():
    pesan = entry.get()

    if pesan == "":
        return

    # Menampilkan pesan user
    chat.insert(END, "YOU : " + pesan + "\n", "user")
    chat.see(END)

    # Hapus input
    entry.delete(0, END)

    # Loading typing
    chat.insert(END, "JARVIS is typing...\n", "typing")
    chat.see(END)

    # Update GUI
    root.update()

    # Delay sedikit
    root.after(1000)

    # Hapus tulisan typing
    chat.delete("end-2l", "end-1l")

    # Bot menjawab
    jawaban = bot.respond(pesan)

    # Tampilkan jawaban
    chat.insert(END, "JARVIS : " + jawaban + "\n\n", "bot")
    chat.see(END)

    # Jalankan suara
    threading.Thread(target=suara, args=(jawaban,)).start()

# =========================
# WINDOW UTAMA
# =========================
root = Tk()
root.title("JARVIS AI")
root.geometry("700x600")
root.configure(bg="#0f172a")

# =========================
# ICON / LOGO KECIL
# =========================
logo = PhotoImage(file="jarvis.png")

# Mengecilkan logo
logo = logo.subsample(12, 12)

logo_label = Label(
    root,
    image=logo,
    bg="#0f172a",
    bd=0
)

logo_label.place(x=10, y=10)

# =========================
# JUDUL
# =========================
title = Label(
    root,
    text="JARVIS AI ASSISTANT",
    font=("Orbitron", 20, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)
title.pack(pady=15)

# =========================
# AREA CHAT
# =========================
chat = Text(
    root,
    font=("Consolas", 12),
    bg="#111827",
    fg="white",
    insertbackground="white",
    bd=0,
    padx=10,
    pady=10,
    height=14
)

chat.pack(padx=20, pady=10, fill=BOTH, expand=True)

# Warna teks
chat.tag_config("user", foreground="#22c55e")
chat.tag_config("bot", foreground="#38bdf8")
chat.tag_config("typing", foreground="#facc15")

# =========================
# FRAME INPUT
# =========================
frame = Frame(root, bg="#0f172a")
frame.pack(fill=X, padx=20, pady=15)

# =========================
# INPUT USER
# =========================
entry = Entry(
    frame,
    font=("Consolas", 14),
    bg="#1e293b",
    fg="white",
    insertbackground="white",
    bd=0
)

entry.pack(side=LEFT, fill=X, expand=True, ipady=10, padx=(0,10))

# =========================
# TOMBOL SEND
# =========================
button = Button(
    frame,
    text="SEND",
    font=("Arial", 11, "bold"),
    bg="#38bdf8",
    fg="black",
    activebackground="#0ea5e9",
    bd=0,
    padx=20,
    pady=10,
    command=kirim
)

button.pack(side=RIGHT)

# =========================
# ENTER KEY
# =========================
root.bind('<Return>', lambda event: kirim())

# =========================
# WELCOME MESSAGE
# =========================
welcome = "Hello, I am ready to assist you."

chat.insert(END, "JARVIS : " + welcome + "\n\n", "bot")

# Suara welcome
threading.Thread(target=suara, args=(welcome,)).start()

# =========================
# RUN PROGRAM
# =========================
root.mainloop()