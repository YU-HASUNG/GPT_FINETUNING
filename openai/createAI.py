import openai

#AI 생성하는 코드

apikey = "put your gpt api key"
openai.api_key = apikey

file_id = "file-HJlGJKXoeiAC1QCmjTOOQ3we"
response = openai.FineTuningJob.create(training_file=file_id, model="gpt-3.5-turbo")
print(response)

# 리스트 검색
# response = openai.FineTuningJob.list()

# 파일 상태 검색 (오류난 경우 원인 분석)
# file_details = openai.File.retrieve(id=file_id)
# print(file_details.status_details)