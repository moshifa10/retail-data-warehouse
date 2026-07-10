                invalid_customer_csv(row, "Product Exists Already")
                continue

            invalid_id = "Product id is invalid"
            name = "Product name is invalid"
            price = "Invalid price"
            product_name = "Missing product name"

            reasons = [
                (invalid_id, valid_id),
                (name, valid_product_name),
                (price ,valid_price_int if valid_price_int == False else valid_price),
                (product_name, valid_product_name)
                ]
            
            message = []
            for i in range(len(reasons)):
                if reasons[i][-1] == False:
                    message.append(reasons[i][0])

            if message:
                invalid_customer_csv(row, ", ".join(message))

            else:
                ids.append(row["product_id"])
                valid_products_csv(row)



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
        if int(row["price"]) < 1:
            return False
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
