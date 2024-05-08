# from util import *
import requests

def get_vicuna_answer(message):
    vicuna_url = "http://127.0.0.1:2020/"
    data = message # 模拟需要提交的数据
    post_data = {"data": str(data)} # 使用post提交的数据
    answer = requests.post(url=vicuna_url, data=post_data)
    return answer.text

file_name = 'models/3/MyModel-LLM-Infer/data/ICEWS14/entity2id.txt'
entity2id = []


out = open("models/3/MyModel-LLM-Infer/data/ICEWS14/entity2llm.txt", "a")

with open(file_name) as f:
    i = 0
    for line in f:
        s = (line.split('\t')[0], line.split('\t')[1]) 
        message = f"You are a wikipidia. Please tell me some information about '{s[0]}'."
        res = get_vicuna_answer(message).split('\n')[0] + '\n'
        print(s)
        print(res)
        out.write(res)
        i += 1

out.close()
