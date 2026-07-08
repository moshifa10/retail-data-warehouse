import pandas as pd
from pathlib import Path


# In each file it should return this:
    # Valid rows
    # Invalid rows

    # - Then save them to data/proccessed or data/rejected

def validate_customer(df: pd.DataFrame):

    # Check missing customers ids, customer name, city

    for index, row in df.iterrows():
        valid_id = check_id(row)
        valid_customer_name = check_customer_name(row)
        valid_city = check_city(row)

        if all([valid_id, valid_city, valid_customer_name]):
            # Just add to proccessed csv
            valid_customer_csv(row)
            break



def check_id(row : pd.Series) -> bool:
    return not (pd.isna(row["customer_id"]) or row["customer_id"] is None)

def check_customer_name(row : pd.Series) -> bool:
    return not (pd.isna(row["customer_name"]) or row["customer_name"] is None)

def check_city(row : pd.Series) -> bool:
    return not (pd.isna(row["city"]) or row["city"] is None)

#     return pd.read_csv(file_path)


def valid_customer_csv(data: pd.Series) -> pd.DataFrame:
    file_path = Path("data/processed/valid_customer.csv")
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if file_path.is_file():
        df = pd.read_csv(file_path)
        df.loc[len(df)] = data
    
    else:
        # Create columns for that
        new_row = {
            "customer_id": [data["customer_id"]],
            "customer_name":[ data["customer_name"]],
            "email": [data["email"]],
            "city": [data["city"]]
        }

        df = pd.DataFrame(new_row)
        df.to_csv(file_path, index=False)



# VALID Ones

# def valid_customers_csv() -> pd.DataFrame:
#     file_path = Path("data/processed/valid_customers.csv")
#     file_path.parent.mkdir(parents=True, exist_ok=True)
#     file_path.touch(exist_ok=True)
#     return pd.read_csv(file_path)

    
# def valid_products_csv() -> pd.DataFrame:
#     file_path = Path("data/processed/valid_products.csv")
#     file_path.parent.mkdir(parents=True, exist_ok=True)
#     file_path.touch(exist_ok=True)


# INVALID ONES

# def invalid_customers_csv() -> pd.DataFrame:
#     file_path = Path("data/rejected/invalid_customers.csv")
#     file_path.parent.mkdir(parents=True, exist_ok=True)
#     file_path.touch(exist_ok=True)
#     return pd.read_csv(file_path)


# def create_rejected_csv() -> pd.DataFrame:
#     file_path = Path("data/rejected/invalid_stores.csv")
#     file_path.parent.mkdir(parents=True, exist_ok=True)
#     file_path.touch(exist_ok=True)
#     return pd.read_csv(file_path)

# def create_rejected_csv() -> pd.DataFrame:
#     file_path = Path("data/processed/invalid_products.csv")
#     file_path.parent.mkdir(parents=True, exist_ok=True)
#     file_path.touch(exist_ok=True)
#     return pd.read_csv(file_path)