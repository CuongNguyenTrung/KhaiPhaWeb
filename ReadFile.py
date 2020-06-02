import json
import io

with io.open('input.json', 'r', encoding='utf8') as f:
    data = json.load(f)
    print(len(data))
    for i in range(0, len(data)):
        print(data[i]['comment'].strip(), ":", data[i]['rating'], end='\n\n')
