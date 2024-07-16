# EchoElite

EchoElite is an interactive web-based voice assistant application that uses speech recognition and text-to-speech technologies to provide responses to user queries. This project uses a Flask backend to handle interactions and responses from an AI model.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## Features

- Voice interaction using Web Speech API for speech recognition and text-to-speech.
- Animated assistant interface.
- Backend interaction with Google Generative AI for generating responses.
- Flask backend for handling requests and responses.

## Installation

### Prerequisites

- Python 3.6 or higher
- Node.js (for frontend dependencies)
- Google Generative AI API Key

### Clone the Repository

```bash
git clone https://github.com/shahram8708/EchoElite.git
cd EchoElite
```

### Backend Setup

1. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Set up your Google Generative AI API key:

```bash
export API_KEY='your_google_api_key'  # On Windows use `set API_KEY=your_google_api_key`
```

### Frontend Setup

1. Install the required frontend dependencies:

```bash
npm install
```

## Usage

1. Start the Flask server:

```bash
flask run
```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Click on the assistant and start interacting by speaking to it.

## Technologies

- **Frontend:**
  - HTML5
  - CSS3
  - JavaScript (Web Speech API for speech recognition and text-to-speech)

- **Backend:**
  - Python 3
  - Flask
  - Google Generative AI API

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b my-new-feature`.
3. Make your changes and commit them: `git commit -am 'Add some feature'`.
4. Push to the branch: `git push origin my-new-feature`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Detailed Code Explanation

### HTML Structure

The HTML file provides the structure for the voice assistant interface, which includes:

- A container for the assistant.
- An assistant element that reacts to user interaction.
- A response container to display the status and response text.

### CSS Animations

Multiple CSS animations are defined for visual effects:

- `@keyframes bounce`: Creates a bouncing effect for the assistant ear.
- Other animation definitions can be added similarly as needed.

### JavaScript Functionality

JavaScript is used to handle voice interactions and communication with the Flask backend:

- Initialize speech recognition.
- Define functions for handling user clicks, starting speech recognition, processing speech recognition results, and sending user input to the backend.
- Handle the assistant's click event to start listening and processing speech.

### Flask Backend

The Flask backend is configured to:

- Serve the main HTML page.
- Handle `/chat` POST requests by processing user input and generating responses using the Google Generative AI API.

## Sample Code

Below is a sample code snippet from the provided HTML and Flask application:

```html
<!DOCTYPE html>
<html lang="en">
<!-- ... HTML structure ... -->
</html>
```

```python
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
```
