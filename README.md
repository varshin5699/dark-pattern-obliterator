# Dark Patterns Buster

---

## Overview

Dark Patterns Buster is a web extension built using Flask, which interfaces with an LLM Mistral 7b model to detect and classify dark patterns on websites. The front end of the application utilizes JavaScript and HTML for scraping websites and displaying the results. This README provides information about the project, including an explanation of dark patterns, the technology stack used, and details about the LLM Mistral 7b model.

## Dark Patterns

Dark patterns are user interface design choices crafted to manipulate users into taking actions they may not otherwise choose to take. These deceptive design tactics are often used to trick users into subscribing to unwanted services, making unintended purchases, or divulging sensitive information. Dark Patterns Buster aims to identify and raise awareness about these manipulative practices on websites.

## Technology Stack

### Backend
- **Flask**: Flask is a lightweight Python web framework used for building the web application backend.
- **LLM Mistral 7b Model**: LLM (Large Language Models) Mistral 7b is a state-of-the-art natural language processing model used for detecting and classifying dark patterns.

### Frontend
- **JavaScript**: JavaScript is used to interact with the DOM and perform website scraping.
- **HTML**: HTML is used for structuring the front end of the web extension.

## LLM Mistral 7b Model

LLM Mistral 7b is a powerful large language model trained on vast amounts of text data. It has been fine-tuned specifically for detecting dark patterns on websites. The model utilizes advanced natural language processing techniques to analyze website content and identify patterns indicative of manipulative user interfaces.

## How Dark Patterns Buster Works

1. **User Interaction**: Users install the Dark Patterns Buster web extension in their browser.
2. **Website Analysis**: When a user visits a website, the extension scrapes the content and sends it to the Flask backend.
3. **Model Prediction**: The backend utilizes the LLM Mistral 7b model to analyze the website content and detect any dark patterns present.
4. **Display Results**: The results of the analysis are displayed to the user through the web extension interface, highlighting any detected dark patterns and providing explanations.

## Installation

To install Dark Patterns Buster, follow these steps:

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the Flask application running the ipynb on google colab.
4. Load the extension in your browser.

## Contributing

Contributions to Dark Patterns Buster are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.



