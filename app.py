import chainlit as cl

@cl.on_chat_start
async def main():
    await cl.Message(content="How can I help you?").send()