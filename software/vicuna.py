# from transformers import pipeline

# pipe = pipeline("text-generation", model="lmsys/vicuna-7b-v1.5")

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

model_path = 'software/vicuna/vicuna-7b-v1.5'

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)