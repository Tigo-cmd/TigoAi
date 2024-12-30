import gradio as gr
import asyncio
from models.source import TigoGroq, load_dotenv

client = TigoGroq()
load_dotenv()
# Function to reverse text


async def input_message(message: str):
    return await client.get_response_from_ai(message)

# # Create the interface
# iface = gr.Interface(
#     fn=input_message,
#     title="TigoAI",
#     inputs="text",
#     outputs="text",
#     description="GUI Chat with TigoAI",
# )
css = """
/* Custom CSS */
#component-1 {
    margin-right: 20px;
    float: left;
}
#component-2 {
    margin-left: 20px;
    float: left;
}
"""

iface = gr.Interface(
    fn=input_message,
    inputs=gr.Textbox(label="Message TigoAi"),
    outputs=gr.Textbox(),
    title="TigoAI",
    description="GUI Chat with TigoAI",
    css=css
)

if __name__ == '__main__':
    asyncio.run(iface.launch(share=True))

