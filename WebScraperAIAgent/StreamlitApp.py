import streamlit as st
from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.utils import prettify_exec_info

# Define the configuration for the scraper
graph_config = {
    "llm": {
        "model": "ollama/phi3:mini",
        "temperature": 1,
        "format": "json",
        "model_tokens": 2000,
        "base_url": "http://localhost:11434",
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "temperature": 0,
        "base_url": "http://localhost:11434",
    }
}

# Streamlit app interface
st.set_page_config(
    page_title="Smart Web Scraper",
    page_icon=":mag:",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title("🔍 Smart Web Scraper")

st.markdown("""
    Welcome to the **Smart Web Scraper**! 🎉  
    This application uses a powerful AI-driven scraper to scrape information from any website.
""")

# User input for website URL
url = st.text_input("🌐 Enter the website URL to scrape:", "https://en.wikipedia.org/wiki/The_Best_FIFA_Men%27s_Player")

# User input for prompt
prompt = st.text_input("💡 Enter the prompt for scraping:", "List me all Wins by country name.")

# Scrape button with emoji
if st.button("🚀 Scrape"):
    if url and prompt:
        st.info("Scraping in progress... please wait ⏳")
        # Create the SmartScraperGraph instance
        smart_scraper_graph = SmartScraperGraph(
            prompt=prompt,
            source=url,
            config=graph_config
        )

        # Run the scraper and display the results
        try:
            result = smart_scraper_graph.run()
            st.success("Scraping completed successfully! ✅")
            st.json(result)  # Display the result as JSON
        except Exception as e:
            st.error(f"An error occurred: {e} ❌")
    else:
        st.warning("Please enter both a valid URL and a prompt. ⚠️")

# Instructions for the user
st.markdown("""
    **Instructions:**  
    1. Enter the website URL you want to scrape. 🌐
    2. Provide a prompt to guide the scraping process. 💡
    3. Click the "Scrape" button to start. 🚀
    
    This application scrapes the given website URL based on the provided prompt.
    Make sure the URL points to a valid webpage for proper scraping results.
""")

# Footer
st.markdown("""
    ---
    Made with ❤️ by Abhishek
""")
