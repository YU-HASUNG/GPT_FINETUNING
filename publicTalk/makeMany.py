import os
import json

#파일 생성하는

# JSON 파일이 있는 디렉토리 경로
json_dir = r'C:\Users\dbgkt\python\publicTalk\sample' #본인의 파일 경로

data_list = []

# 디렉토리 내의 모든 JSON 파일에 대해 반복
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):  # JSON 파일인 경우
        json_path = os.path.join(json_dir, filename)
        with open(json_path, 'r', encoding='utf-8') as json_file:
            json_data = json.load(json_file)
            info = json_data.get("info", [])

            json_str = json.dumps(json_data)
            if "남성" not in json_str and "30대" not in json_str and "40대" not in json_str and "50대" not in json_str and "60대" not in json_str and "70대" not in json_str and "80대" not in json_str:
                data_list.extend(info)
            
            # speaker = info.get("speaker", {})
            # sex = speaker.get("sex", "")
            # age = speaker.get("age", "")

                # 조건을 만족하지 않는 경우에만 추가
            # if sex == "여성" and age == "20대":
            #   data_list.append(info)

            # 필터링된 "info" 데이터를 결과 리스트에 추가
            # data_list.extend(info)

for item in data_list:
  # 주어진 데이터
  data = [item]

  # JSONL 형식의 메시지 객체 생성
  messages = [{"role": "system", "content": "friend"}]
  for item in data:
      for line in item["annotations"]["lines"]:
          message = {
              "role": "user" if line["id"] % 2 == 1 else "assistant",
              "content": line["text"],  # "text" 키를 사용
          }
          messages.append(message)

  # JSONL 파일로 저장 (기존 파일에 추가)
  with open("conversation.jsonl", "a", encoding="utf-8") as jsonl_file:
      jsonl_file.write("\n")
      jsonl_file.write("{\"messages\": [")
      for i, message in enumerate(messages):
          if (i % 2!= 0 and i == len(messages) - 1) != True:
          
            message["content"] = message["content"].replace("1 : ", "").replace("2 : ", "").replace("3 : ", "").replace("키키", "ㅋㅋ")

            if i % 2 != 0 and i > 1:
                jsonl_file.write("\n")
                jsonl_file.write("{\"messages\": [{\"role\": \"system\", \"content\": \"friend\"}, ")
                
            json.dump(message, jsonl_file, ensure_ascii=False)
            if i == 0 :
                jsonl_file.write(", ")

            if i % 2 == 0 and i > 1:
                jsonl_file.write("]}")

            if i % 2!= 0 :
                jsonl_file.write(", ")

        #   if i < len(messages) - 1:  # 마지막 메시지가 아니라면 쉼표를 추가
        #       jsonl_file.write(", ")
    #   jsonl_file.write("]}")