import openai

#AI ChatGPT한테 전송하는 코드

apikey = "put your gpt api key"
openai.api_key = apikey

response = openai.File.create(
  # file=open("exsample2.jsonl", "rb"),
  file=open("conversation.jsonl", "rb"),
  purpose='fine-tune'
)

print(response)