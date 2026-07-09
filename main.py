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
from src.validate.product_validator import validate_products

def main():
    create_database()
    print("Created The Database + Tables")
    
    # Extract
    print("===================  Extracting customer csv =================================")
    df_customer = read_customer_csv(CUSTOMERS)

    print("===================  Validating customer csv =================================")
    validate_customer(df_customer)

    print()
    print("===================  Extracting product csv =================================")
    df_product = read_product_csv(PRODUCTS)

    print("===================  Validating product csv =================================")
    validate_products(df_product)
    

    

if __name__ == "__main__":
    main()