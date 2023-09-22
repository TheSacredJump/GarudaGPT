import openai
import gradio

#Get the OpenAI API Key
openai.api_key = open('LLM Project/OpenAI_API_Key', 'r').read()

messages=[]

#Create a custom chatgpt model
def custom_chatgpt(query):
    messages.append({"role": "user", "content": query})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    chatgpt_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "user", "content": chatgpt_reply})
    return chatgpt_reply



demo = gradio.Interface(fn=custom_chatgpt, inputs="text", outputs="text", title="Garuda GPT")

demo.launch()
