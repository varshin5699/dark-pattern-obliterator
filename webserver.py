from flask import Flask
from flask import Flask, jsonify, request
from flask_cors import CORS
import torch
import os
import sys
import json
#sys.path.append(os.path.abspath("/Users/srivarshinees/dpbh_hackathon/dpbh/darkpatterndetect"))
from darkpatterndetect.model import model_load, generate_prompt, get_completion_2

model,tokenizer=model_load()

app=Flask(__name__)
@app.route('/', methods=['POST'],port=5000)
CORS(app)

#!pip install -U flask-cors
#give above command in the host gc

def main():
    if request.method == 'POST':
        output = []
        data = request.get_json().get('tokens')
        
        #check if the entire json file can be sent in as input query and find the format of answer in that case
        
        for token in data:
            
            token_=dict(enumerate(token)))
            result = get_completion_2(model,query=token_,tokenizer=tokenizer)
            output.append(result[0])

        dark = [data[i] for i in range(len(output)) if output[i] != 'H']
        for d in dark:
            print(d)
        
        print(len(dark))

        message = '{ \'result\': ' + str(output) + ' }'
        print(message)

        json = jsonify(message)

        return json

if __name__ == '__main__':
    app.run(threaded=True, debug=True)
