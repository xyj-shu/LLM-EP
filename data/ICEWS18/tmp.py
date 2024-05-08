file_name = 'models/3/MyModel-LLM-Infer/data/ICEWS18/entity2id.txt'
entity2id = []

in_file = "models/3/MyModel-LLM-Infer/data/ICEWS18/entity2llm.txt"
out_file = open("models/3/MyModel-LLM-Infer/data/ICEWS18/entity2llm-1.txt", "a")
text = []
with open(in_file) as f:
    for i, line in enumerate(f):
        print(i, line)
        text.append(line)

with open(file_name) as f:
    for i, line in enumerate(f):
        # s = (line.split('\t')[0], line.split('\t')[1]) 
        # # message = f"You are a wikipidia. Please tell me some information about '{s[0]}'."
        # message = f"你是一个百科全书. 请告诉我一些信息关于 '{s[0]}'."
        # res = get_vicuna_answer(message).split('\n')[0] + '\n'
        res = text[i % len(text)]
        print(res)
        out_file.write(res)

# in_file.close()
out_file.close()