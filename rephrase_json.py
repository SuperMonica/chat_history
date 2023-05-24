import json

with open('conversations.json', 'r') as f:
    data = json.load(f)

history = ['Auto UML for C++', 'Resize Icon with Button', 'Time Duration Correction', 'EF IT/AI Overview', 'Image Data Transfer via Subprocess', 'Midjourney Image Generation.', 'Update Docker on Offline Server', 'Deep Learning Distillation Setup', 'Dockerfile for Anvil Uplink', 'Quant Trading Knowledge List', 'Stock Market Basics', 'Investing in US Stocks', 'Translation Feedback', 'Translation Corrections - Chinese', 'Comprehensive Reading for English', 'Door Detection Algorithm.', 'The Jacksons User Persona', 'Travel Conversation Practice.', 'Revision Request']

for i in data:
    if i['title'] in history:
        for j in i['mapping'].values():
            if j['message']:
                if j['message']['author']['role'] == 'user':
                    print(j['message']['content']['parts'])

