# AI-Based Markdown Editor

## Introduction

This project presents an AI-Based Markdown Editor, a web-based tool designed to enhance the writing and editing process through advanced AI features. Built with HTML, CSS, Django, Python and JavaScript, this editor integrates cutting-edge AI models and APIs to provide functionalities like speech-to-text transcription, real-time language processing, and more, aimed at increasing productivity while notetaking. 

## Features

- **Transcribe Video**: Leverages the OpenAI Whisper model for speech-to-text to transcribe audio from a video into markdown format.
- **Inline LLM Calls**: Utilizes OpenAI's GPT-3.5-turbo for processing natural language queries and embedding responses directly into the editor.
- **Save and Load Markdown Files**: Offers functionality to save your current work as a Markdown file and load existing Markdown files into the editor.
- **Toggle Preview**: Enables a split-screen mode to preview your Markdown content in real-time.
- **Export to PDF**: Converts your Markdown documents into PDF format for easy sharing and printing.

## Getting Started


1. Clone the repository to your local machine:
   ```bash
   mkdir ai-editor
   git clone https://github.com/orlovt/ai-markdown.git
   ```
2. Set up your virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Add your OpenAI API key to `vid_transcript/transcript_app/views.py`. You can find instructions on how to obtain this key from the OpenAI documentation.
5. Start the Django webserver:
   ```bash
   python manage.py migrate  # Apply database migrations
   python manage.py runserver
   ```
6. Navigate to `http://127.0.0.1:8000` in your web browser to view the application.

## Skills Demonstrated

- Connecting to and utilizing APIs and AI models, such as OpenAI's `Whisper` and `GPT-3.5-turbo`.
- Front-end web development using `HTML, CSS`, and `JavaScript`.
- Backend logic with `Python` and `Django`. 
- Implementing a user-friendly interface and ensuring a seamless user experience.


## Future Improvements

- Introduce more AI-based features to further assist with content creation.
- Enhance the user interface for a more engaging and intuitive experience.

## How to Contribute

Provide instructions for how others can contribute to your project. Include guidelines for submitting issues, pull requests, and any coding standards or practices they should follow.

## License

State the license under which your project is available. Open-source projects typically use licenses like MIT, GPL, or Apache 2.0. Provide a link or a full copy of the license text.
