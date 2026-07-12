import pandas as pd
from pathlib import Path

def validate_stores(df: pd.DataFrame):

    ids = []
    for index, row in df.iterrows():
        valid_id = check_id(row)
        valid_store_name = check_store_name(row)
        valid_province = check_province(row)
        valid_manager = check_manager(row)

        if all([valid_id, valid_store_name, valid_province, valid_manager]):
            if (row["store_id"]) in ids:
                invalid_stores_csv(row, "Store ID Exists Already")
                continue
            ids.append(row["store_id"])
            valid_stores_csv(row)
        else:
            invalid_id = "storeId is invalid"
            store_name = "Store name is invalid"
            province = "Provinve is invalid"
            manager = "Manager is not existing"

            reasons = [
                (invalid_id, valid_id),
                (store_name, valid_store_name),
                (province ,valid_province),
                (manager, valid_manager)
                ] 
            
            message = []
            for i in range(len(reasons)):
                if reasons[i][-1] == False:
                    message.append(reasons[i][0])
            invalid_stores_csv(row, ", ".join(message))

def check_manager(row: pd.Series) -> bool:
    return not (pd.isna(row["manager"]) or row["manager"] is None)

def check_id(row : pd.Series) -> bool:
    return not (pd.isna(row["store_id"]) or row["store_id"] is None)

def check_store_name(row : pd.Series) -> bool:
    return not (pd.isna(row["store_name"]) or row["store_name"] is None)

def check_province(row : pd.Series) -> bool:
    return not (pd.isna(row["province"]) or row["province"] is None)


def valid_stores_csv(data: pd.Series) -> None:
    file_path = Path("data/processed/valid_stores.csv")
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if file_path.is_file():
        df = pd.read_csv(file_path)
        df.loc[len(df)] = data
        df.to_csv(file_path, index=False)
    
    else:
        new_row = {
            "store_id": [data["store_id"]],
            "store_name":[ data["store_name"]],
            "province": [data["province"]],
            "manager": [data["manager"]]
        }
        df = pd.DataFrame(new_row)
        df.to_csv(file_path, index=False)

def invalid_stores_csv(data: pd.Series, reason) -> None:
    file_path = Path("data/rejected/rejected_stores.csv")
    file_path.parent.mkdir(parents=True, exist_ok=True)

    data["reason"] = reason
    if file_path.is_file():
        df = pd.read_csv(file_path)
        df.loc[len(df)] = data
        df.to_csv(file_path, index=False)
    
    else:
        new_row = {
            "store_id": [data["store_id"]],
            "store_name":[ data["store_name"]],
            "province": [data["province"]],
            "manager": [data["manager"]],
            "reason": [reason]
        }
        df = pd.DataFrame(new_row)
        df.to_csv(file_path, index=False)
