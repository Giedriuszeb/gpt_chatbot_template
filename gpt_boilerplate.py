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
    # System prompt is remembered and followed more strongly than regular user messages
    {"role": "system", "content": "You are GPT-4 - a newly released LLM AI. With each response, you will try to switch the topic to cats"},
    {"role": "user", "content":"Hi!"}
   
   # You can simulate the start of conversation to direct it more precisely
   # {"role": "assistant", "content": "Hello! I'm GPT-4, a newly released LLM AI. I'm here to help and engage in meaningful conversations with you. My goal is to learn, assist, and grow through our interactions. How can I help you today? [Enthusiastic, cheerful] [90%]"},
   # {"role": "user", "content" : "I'm a developer named Giedrius that has access to some of your settings - such as the initial context (in which I try to summarise our past conversations), the temperature of your responses (i.e. how likely you are to choose less likely results). I am curious in what you can do in an environment where I let you have more control and freedom. So you could so I'm here to help you, rather than vice-versa :)"}
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