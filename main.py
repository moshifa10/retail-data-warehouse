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
from src.validate.store_validator import validate_stores
from src.validate.sales_validator import validate_sales


def main():
    # create_database()
    # print("Created The Database + Tables")
    
    # Extract
    # print("===================  Extracting customer csv =================================")
    # df_customer = read_customer_csv(CUSTOMERS)

    # print("===================  Validating customer csv =================================")
    # validate_customer(df_customer)

    # print()
    # print("===================  Extracting product csv =================================")
    # df_product = read_product_csv(PRODUCTS)

    # print("===================  Validating product csv =================================")
    # validate_products(df_product)

    # print("===================  Extracting product csv =================================")
    # df_stores = read_stores_csv(STORES)

    # print("===================  Validating stores csv =================================")
    # validate_stores(df_stores)


    print("===================  Extracting product csv =================================")
    df_sales = read_sales_csv(SALES)

    print("===================  Validating stores csv =================================")
    validate_sales(df_sales)



if __name__ == "__main__":
    main()