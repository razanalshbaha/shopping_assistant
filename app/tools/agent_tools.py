from langchain_community.tools.tavily_search import TavilySearchResults
from app.config import TAVILY_API_KEY
import os

os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY


def get_product_links(product_description: str) -> str:
    product_search = TavilySearchResults()
    result= product_search.run(product_description)
    print(result)
    urls = [item["url"] for item in result]
    print(urls)
    return urls