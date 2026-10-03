import sys
sys.stdout.reconfigure(encoding='utf-8')

import pandas as pd



import pandas as pd


data = {
    "Week": ["Week 1", "Week 2", "Week 3", "Week 4"],
    "Orders": [1200, 1350, 1050, 900],
    "Revenue": [1800000, 2025000, 1575000, 1350000],
    "Returns": [96, 108, 147, 162],
    "Visitors": [45000, 48000, 42000, 38000],
    "AdSpend": [250000, 250000, 280000, 300000]
}

df = pd.DataFrame(data)
df.to_csv("sales_data.csv", index=False)
print(df)

df = pd.read_csv("sales_data.csv")

print(df.head())        
print(df.columns)       
print(df.describe())    

dataset_context = f"""
Columns: {list(df.columns)}
Sample data:
{df.to_string(index=False)}
"""
print(dataset_context)

import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-flash-latest")
#for m in genai.list_models():
    #if 'generateContent' in m.supported_generation_methods:
        #print(m.name)

def ask_question(question):
    prompt = f"""
You are a data analyst. Here is a dataset:

{dataset_context}

Based on this dataset, answer the following question in simple, clear language:
{question}
"""
    response = model.generate_content(prompt)
    return response.text

# Test karo
# print("AI Data Chat shuru ho gaya! 'exit' likho band karne ke liye.\n")

# while True:
#     q = input("tumhara sawaal:"week 4 me kya problem thi)
#     if q.lower() == "exit":
#         print("Chat band ho gaya!")
#         break
#     print("\n" + ask_question(q) + "\n")
# Test karo
answer = ask_question("toh company ki sales badhane ke liye kya measures le")
print(answer)