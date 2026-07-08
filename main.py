from src.load.database_loader import create_database
from src.extract.extractor import (read_customer_csv,
                                read_product_csv, 
                                read_sales_csv, 
                                read_stores_csv
                                )
from src.utils.helpers import (CUSTOMERS,
                               PRODUCTS,
                               SALES,
                               STORES
                               )
from src.validate.customer_validator import validate_customer


def main():
    create_database()
    print("Created The Database + Tables")
    
    # Extract

    df_customer = read_customer_csv(CUSTOMERS)

    validate_customer(df_customer)

    

    

if __name__ == "__main__":
    main()