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
    """Identifies the primary supplier or parent company of a product, guessing if generic."""
    
    system_instruction = (
        "You are a strict data classification assistant. "
        "Your task is to identify the primary manufacturer, supplier, or parent company of a given product. "
        "CRITICAL RULES: "
        "1. If the product is generic (e.g., 'Bread', 'Water', 'Soap'), you MUST pick exactly ONE of the most famous brands or manufacturers for that item. "
        "2. NEVER say 'Various', NEVER ask for clarification, and NEVER provide explanations. "
        "3. Return ONLY a single company name. Do not write full sentences or add punctuation. "
        "Example 1 (Specific): If Product is 'Sprite', return 'Coca-Cola'. "
        "Example 2 (Generic): If Product is 'Bread', return 'Sasko'."
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