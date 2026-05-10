import aiml

bot = aiml.Kernel()

bot.learn("chatbot.aiml")

print("Chatbot aktif! Ketik 'quit' untuk keluar.")

while True:
    pesan = input("User : ")

    if pesan.lower() == "quit":
        print("Bot : Goodbye!")
        break

    jawaban = bot.respond(pesan)

    print("Bot :", jawaban)