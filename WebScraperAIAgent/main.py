from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.utils import prettify_exec_info

graph_config = {
    "llm": {
        "model": "ollama/phi3:mini",  # Replace with a your favorite model name if your not gpu poor like me
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

# ************************************************
# Create the SmartScraperGraph instance and run it
# ************************************************

smart_scraper_graph = SmartScraperGraph(
    prompt="List me all Wins by country name.",
    source="https://en.wikipedia.org/wiki/The_Best_FIFA_Men%27s_Player",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)
