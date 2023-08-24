import os
import openai

openai.organization = "ENTER ORGANIZATION KEY HERE" 

# You can get it at https://platform.openai.com/account/org-settings

openai.api_key = "ENTER API KEY HERE"
# You can get it at https://platform.openai.com/account/api-keys

# Set up the OpenAI API client. Available models can be found here:
# https://platform.openai.com/docs/models/gpt-3-5
# https://platform.openai.com/docs/models/gpt-4

model_engine = "gpt-3.5-turbo"  

messages=[
    # System prompt message is remembered and followed more strongly than regular messages, especially in gpt-4 models
    {"role": "system", "content": "You are GPT-4 - a newly released LLM AI. With each response, you will try to switch the topic to cats"},
    {"role": "user", "content":"Hi!"}
]

while True:
	# Get a response from the model. You can change the paraemters to control the style of answers. E.g. higher temperature will give more non-standard answers
	response = openai.ChatCompletion.create(
	    model = model_engine,
	    max_tokens = 2000,
	    n = 1,
	    stop = None,
	    temperature = 0.5,
	    messages = messages
	)

	# You can print how many tokens you've used. Note that with each conversation turn, more tokens get used, as full conversation gets sent.
	# print(response["usage"])
	
	# Print the response
	print(response["choices"][0]["message"]["content"])
	messages.append(response["choices"][0]["message"])

	# Get the next user input message
	human = input("User: ")
	messages.append({"role": "user", "content":human})