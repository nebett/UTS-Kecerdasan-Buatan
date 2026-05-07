import aiml
import os

kernel = aiml.Kernel()

kernel.learn("basic.aiml")
kernel.learn("jarvis.aiml")

print("Jarvis aktif...")

while True:
    message = input("User : ")

    if message == "quit":
        break

    response = kernel.respond(message)

    print("Bot :", response)
