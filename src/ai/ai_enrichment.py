from groq import Groq
from src.utils.config import GROK
import os

groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def get_product_category(product_name: str) -> str:
    """Classifies a product into one of the predefined dataset categories."""
    categories = ["Drinks", "Food", "Dairy", "Snacks", "Household"]

    system_instruction = (
        "You are a strict data classification assistant. "
        "Your task is to look at a product name and return ONLY its category. "
        f"You must pick exactly one category from this list: {', '.join(categories)}. "
        "Do not write full sentences. Do not add punctuation. Return only the category name."
    )

    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.0,
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": f"Product: {product_name}"}
        ]
    )
    
    return response.choices[0].message.content.strip()

def get_product_supplier(product_name: str) -> str:
    """Identifies the primary supplier or parent company of a product."""
    
    system_instruction = (
        "You are a strict data classification assistant. "
        "Your task is to identify the primary manufacturer, supplier, or parent company of a given product. "
        "Return ONLY the company name. Do not write full sentences, explanations, or add punctuation. "
        "Example: If the product is 'Sprite', return 'Coca-Cola'."
    )

    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.0,
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": f"Product: {product_name}"}
        ]
    )
    
    return response.choices[0].message.content.strip()
