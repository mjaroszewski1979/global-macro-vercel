## AI Detector

### This is a Python-based web application developed using the Django framework. This project leverages the Huggingface API to provide users with a tool to detect AI-generated content using the Roberta AI content detector.

#### In an era where AI-generated content is becoming increasingly common, distinguishing between human-written and AI-generated text is crucial. This application addresses the need for a reliable tool to identify the authenticity of text content.

### How It Works
* User Input: Users submit text content via the web interface.
* API Integration: The application connects to the Huggingface API.
* Content Analysis: Utilizes the Roberta AI model to analyze the text.
* Result: Provides a probability score indicating the likelihood of the content being AI-generated.

### Features

* Easy-to-Use Interface: Simple and intuitive web interface for content submission.
* Accurate Detection: Utilizes advanced machine learning algorithms from Huggingface's Roberta AI.
* Python & Django: Built with Python for simplicity and Django for scalability.

### Installation

1. Clone the repository:
  ```bash
  git clone https://github.com/mjaroszewski1979/global-macro-vercel.git
  cd golden-cross-v1
  ```
2. Create a virtual environment:
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```
3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
4. Apply migrations and start the server:
  ```bash
  python manage.py migrate
  python manage.py runserver
  ```

### Usage
* Access the web application via the local server.
* Enter the text you want to analyze.
* Submit the text to get the AI content probability score.

### Testing

1. Run unit tests:
   ```bash
   python manage.py test
   ```

### Technologies Used
* Django: Web framework for building the application.
* Huggingface API: Enables users to execute hosted models for different tasks.
* RoBERTa: Interpreting, analyzing, and generating human-like text.

### Contributing
* Fork the repository.
* Create a new branch (git checkout -b feature-branch).
* Make your changes and commit them (git commit -m 'Add new feature').
* Push to the branch (git push origin feature-branch).
* Open a pull request.

### Contact
For questions or feedback, please contact [mjaroszewski1979.](https://github.com/mjaroszewski1979)

![caption](https://github.com/mjaroszewski1979/global-macro-vercel/blob/main/ai_detector_mockup.png) 

  Live | Code | Technologies
  ---- | ---- | ------------
  [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/vercel.png">](https://global-macro-vercel.vercel.app/) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/github_g.png">](https://github.com/mjaroszewski1979/global-macro-vercel) | <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/python_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/django_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/html_g.png"> <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/css_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/bulma_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/huggingface_logo.png">
