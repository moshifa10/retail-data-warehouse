import pandas as pd
from pathlib import Path
from groq import g


# In each file it should return this:
    # Valid rows
    # Invalid rows

    # - Then save them to data/proccessed or data/rejected

def validate_products(df: pd.DataFrame):

    # Check missing customers ids, customer name, city
    ids = []
    for index, row in df.iterrows():
        valid_id = check_id(row)
        valid_product_name = check_product_name(row)
        valid_category = check_category(row)
        valid_price = check_price(row)
        valid_supplier = check_supplier(row)
        valid_price_int = check_price_interger(row)

        if all([valid_id, valid_product_name, valid_category, valid_price, valid_supplier, valid_price_int]):
            if (row["product_id"]) in ids:
                # Exists
                invalid_customer_csv(row, "Product Exists Already")
                continue
            ids.append(row["product_id"])
            # Just add to proccessed csv
            valid_products_csv(row)
        else:
            if not valid_category:
                # Prompt AI
                pass

            if not valid_supplier:
                pass

            invalid_id = "Product id is invalid"
            name = "Product name is invalid"
            price = "Invalid price"
            product_name = "Missing product name"

            reasons = [
                (invalid_id, valid_id),
                (name, valid_product_name),
                (price ,valid_price_int if valid_price_int == False else valid_price)
                (product_name, valid_product_name)
                ] 
            
            
            message = []
            for i in range(len(reasons)):
                if reasons[i][-1] == False:
                    message.append(reasons[i][0])
            invalid_customer_csv(row, ", ".join(message))



def check_id(row : pd.Series) -> bool:
    return not (pd.isna(row["product_id"]) or row["product_id"] is None)

def check_product_name(row : pd.Series) -> bool:
    return not (pd.isna(row["product_name"]) or row["product_name"] is None)

def check_category(row : pd.Series) -> bool:
    return not (pd.isna(row["category"]) or row["category"] is None)

def check_price(row : pd.Series) -> bool:
    return not (pd.isna(row["price"]) or row["price"] is None)

def check_price_interger(row: pd.Series) -> bool: 
    try:
        x = int(row["price"])
        return True
    except (TypeError, ValueError):
        return False

def check_supplier(row : pd.Series) -> bool:
    return not (pd.isna(row["supplier"]) or row["supplier"] is None)

#     return pd.read_csv(file_path)


def valid_products_csv(data: pd.Series) -> None:
    file_path = Path("data/processed/valid_products.csv")
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if file_path.is_file():
        df = pd.read_csv(file_path)
        df.loc[len(df)] = data
        df.to_csv(file_path, index=False)
    
    else:
        # Create columns for that
        new_row = {
            "product_id": [data["product_id"]],
            "product_name":[ data["product_name"]],
            "category": [data["category"]],
            "price": [data["price"]],
            "supplier": [data["supplier"]]
        }

        df = pd.DataFrame(new_row)
        df.to_csv(file_path, index=False)

def invalid_customer_csv(data: pd.Series, reason: str) -> None:
    file_path = Path("data/rejected/rejected_products.csv")
    file_path.parent.mkdir(parents=True, exist_ok=True)

    data["reason"] = reason
    # print(data)
    if file_path.is_file():

        df = pd.read_csv(file_path)
        df.loc[len(df)] = data
        df.to_csv(file_path, index=False)
    
    else:
        # Create columns for that
        new_row = {
            "product_id": [data["product_id"]],
            "product_name":[ data["product_name"]],
            "category": [data["category"]],
            "price": [data["price"]],
            "supplier": [data["supplier"]],
            "reason": [reason]
        }

        df = pd.DataFrame(new_row)
        df.to_csv(file_path, index=False)