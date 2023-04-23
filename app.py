import openai
import gradio as gr

openai.api_key = "sk-" # Replace this with your API key: https://beta.openai.com/docs/quickstart/add-your-api-key

def openai_chat(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

def chatbot(key, input, history=[]):
    openai.api_key = key
    output = openai_chat(input)
    history.append((input, output))
    return history, history

gr.Interface(fn = chatbot,
             inputs = ["text","text",'state'],
             outputs = ["chatbot",'state']).launch(debug = True)