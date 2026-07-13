import pandas as pd
from pathlib import Path
import datetime

def validate_sales(df: pd.DataFrame):

    ids = []
    for index, row in df.iterrows():
        valid_transaction_id = check_id(row)
        valid_customer_id = check_customer_id(row)
        valid_product_id = check_product_id(row)
        valid_store_id = check_store_id(row)
        valid_quantity =  check_quantity(row)
        valid_sale_date = check_date(row)

        if all([valid_transaction_id, 
                valid_customer_id, 
                valid_product_id, 
                valid_store_id,
                valid_quantity,
                valid_sale_date
                ]):
            if (row["transaction_id"]) in ids:
                invalid_sales_csv(row, "transaction Id Exists Already")
                continue
            ids.append(row["transaction_id"])
            valid_sales_csv(row)
        else:
            invalid_transaction_id = "Tranaction Id is Invalid"
            invalid_customer_id = "Customer Id is Invalid"
            invalid_product_id = "Product id is Invalid"
            invalid_store_id = "Store id is Invalid"
            invalid_quantity =  "Quantity is Invalid"
            invalid_sale_date = "Invalid sale-date"

            reasons = [
                (invalid_transaction_id, valid_transaction_id),
                (invalid_customer_id, valid_customer_id),
                (invalid_product_id ,valid_product_id),
                (invalid_store_id, valid_store_id),
                (invalid_quantity, valid_quantity),
                (invalid_sale_date, valid_sale_date)
                ] 
            
            message = []
            for i in range(len(reasons)):
                if reasons[i][-1] == False:
                    message.append(reasons[i][0])
            invalid_sales_csv(row, ", ".join(message))

def check_customer_id(row: pd.Series) -> bool:
    return not (pd.isna(row["customer_id"]) or row["customer_id"] is None)

def check_store_id(row: pd.Series) -> bool:
    return not (pd.isna(row["store_id"]) or row["store_id"] is None)

def check_quantity(row: pd.Series) -> bool:
    missing = not (pd.isna(row["store_id"]) or row["store_id"] is None)
    if not missing:
        return False
    
    try:
        quantity = int(row["quantity"])
        if quantity < 1:
            return False
    except (ValueError, TypeError):
        return False

def check_date(row: pd.Series) -> bool:
    missing = not (pd.isna(row["sale_date"]) or  row["sale_date"] is None)
    if not missing:
        return False
    try:
        valid_date = datetime.datetime.strptime("2026-07-04", "%Y-%m-%d").date()
        return True
    except (ValueError):
        return False

def check_product_id(row: pd.DataFrame) -> bool:
    return not (pd.isna(row["product_id"]) or row["product_id"] is None)

def check_manager(row: pd.Series) -> bool:
    return not (pd.isna(row["manager"]) or row["manager"] is None)

def check_id(row : pd.Series) -> bool:
    return not (pd.isna(row["store_id"]) or row["store_id"] is None)


def valid_sales_csv(data: pd.Series) -> None:
    file_path = Path("data/processed/valid_sales.csv")
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if file_path.is_file():
        df = pd.read_csv(file_path)
        df.loc[len(df)] = data
        df.to_csv(file_path, index=False)
    
    else:
        new_row = {
            "transaction_id": [data["transaction_id"]],
            "customer_id":[ data["customer_id"]],
            "product_id": [data["product_id"]],
            "store_id": [data["store_id"]],
            "quantity": [data["quantity"]],
            "sale_date": [data["sale_date"]]
        }
        df = pd.DataFrame(new_row)
        df.to_csv(file_path, index=False)

def invalid_sales_csv(data: pd.Series, reason) -> None:
    file_path = Path("data/rejected/rejected_sales.csv")
    file_path.parent.mkdir(parents=True, exist_ok=True)

    data["reason"] = reason
    if file_path.is_file():
        df = pd.read_csv(file_path)
        df.loc[len(df)] = data
        df.to_csv(file_path, index=False)
    
    else:
        new_row = {
            "transaction_id": [data["transaction_id"]],
            "customer_id":[ data["customer_id"]],
            "product_id": [data["product_id"]],
            "store_id": [data["store_id"]],
            "quantity": [data["quantity"]],
            "sale_date": [data["sale_date"]],
            "reason" : [reason]
        }
        df = pd.DataFrame(new_row)
        df.to_csv(file_path, index=False)
