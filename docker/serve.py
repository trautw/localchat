# FROM https://github.com/mattesmattes/pca/blob/main/pca.py
# Personal Chat Appliance
# version 0.2 by @mattesmattes et al

from gpt_index import GPTSimpleVectorIndex
import gradio as gr

def chatbot(input_text):
    index = GPTSimpleVectorIndex.load_from_disk('data/index.json')
    response = index.query(input_text, response_mode="compact")
    return response.response

iface = gr.Interface(fn=chatbot,
                     inputs=gr.inputs.Textbox(lines=7, label="Enter your text"),
                     outputs="text",
                     title="Your Personal Chat Appliance")

iface.launch(share=True)
