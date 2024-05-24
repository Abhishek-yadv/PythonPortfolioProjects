```markdown
# 💻 Web Scrapping AI Agent

This Streamlit app allows you to scrape a website using the Llama3 language model from Meta and the scrapegraphai library. Simply provide the URL of the website you want to scrape and specify what you want the AI agent to extract from the website.

## Features

- Scrape any website by providing the URL
- Utilize the Llama3 language model from Meta for intelligent scraping
- Customize the scraping task by specifying what you want the AI agent to extract

## How to Get Started?

1. Clone the GitHub repository

```
git clone [https://github.com/Abhishek-yadv/PythonPortfolioProjects/tree/main/WebScraperAIAgent]
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Download and prepare the Llama3 model

- Obtain the Llama3 model from Meta's repository.
- Place the model files in the appropriate directory within the project.

4. Run the Streamlit App

```
streamlit run main.py
```

## How it Works?

- Enter the URL of the website you want to scrape in the provided text input field.
- Specify what you want the AI agent to extract from the website by entering a user prompt.
- The app creates a SmartScraperGraph object using the provided URL, user prompt, and the Llama3 model configuration.
- The SmartScraperGraph object scrapes the website and extracts the requested information using the Llama3 language model.
- The scraped results are displayed in the app for you to view.

```

Make sure to follow the instructions provided by Meta for downloading and setting up the Llama3 model correctly within your project.
