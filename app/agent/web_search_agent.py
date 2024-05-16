from langchain_openai import AzureChatOpenAI
from langchain_core.tools import Tool
from app.tools.agent_tools import get_product_links 
from app.tools.azure_bing_search import search_product_by_image
from langchain.agents import(
    create_react_agent,
    AgentExecutor
)
from langchain import hub
from app.config import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_DEPLOYMENT_NAME,
    API_VERSION,
)


async def web_search_agent() -> str:
    llm = AzureChatOpenAI(
        api_key=AZURE_OPENAI_API_KEY,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_version=API_VERSION,
        azure_deployment=AZURE_DEPLOYMENT_NAME,
    )

    tools_for_agent= [
        Tool(
            name= "product web search",
            func= get_product_links,
            description= "useful when you get a product description and you need URLs to buy the product with the best prices",
        ),
        Tool(
            name= "product web search by image",
            func= search_product_by_image,
            description= "useful when you get an image and you need URLs to buy the product in the image with the best prices",
        )
    ]
    react_prompt= hub.pull("hwchase17/react")
    agent= create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor= AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    return agent_executor
