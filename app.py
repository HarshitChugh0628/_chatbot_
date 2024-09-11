import chainlit as cl

@cl.on_message

async def main(message: cl.Message):
    ## your custom logic here..
    
    ## send a responce back to the user...
    await cl.Message(
        content=f"Recived : {message.content}",
    ).send()