import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import markdown

genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_response():
    data = request.get_json()
    user_input = data.get('user_input', '').strip() 
    
    if user_input.lower() != 'exit' and user_input: 
        response = chat.send_message(user_input)
        bot_response = response.text 
        bot_response_html = markdown.markdown(bot_response)
    else:
        bot_response_html = markdown.markdown("Please provide a valid input.")
    
    return jsonify(user_input=user_input, bot_response=bot_response_html)

if __name__ == '__main__':
    app.run(debug=True)
