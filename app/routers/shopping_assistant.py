from fastapi.routing import APIRouter
from app.schemas.user_input import Text
#from app.services.llm_response import get_llm_response
from app.agent.web_search_agent import web_search_agent
from app.prompts.agent_prompt import get_agent_prompt_template
from app.tools.azure_bing_search import search_product_by_image
import asyncio
from fastapi import File, UploadFile
from starlette.responses import JSONResponse
import tempfile
import os



router = APIRouter()


@router.post("/get_products")
async def get_products(text: Text):
    agent = await web_search_agent()
    formatted_prompt = get_agent_prompt_template().format_prompt(product_description=text)
    task = asyncio.create_task(
                agent.ainvoke(
                    {"input": formatted_prompt}
                )
        )
    
    response = await task
    return response
    


@router.post("/get_products_by_image")
async def get_product_by_image(image: UploadFile = File(...)):
    image_path = "temp_image.jpg"
    with open(image_path, "wb") as buffer:
        buffer.write(await image.read())
    
    host_page_urls = search_product_by_image(image_path)
    print(host_page_urls)
    
    return {"host_page_urls": host_page_urls}

