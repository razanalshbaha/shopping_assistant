from langchain.prompts import PromptTemplate

prompt= """
Given a product description, find the links to buy this product at the best prices.

-Product Description: {product_description}
"""

prompt_template = PromptTemplate(
    template=prompt,
    input_variables=["product_description"],
)

def get_agent_prompt_template() -> PromptTemplate:
    return prompt_template
