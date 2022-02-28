import sqlite3, sys

################## Text Based User Interface ####################
def show_menu():
    print("\nProduct Table Menu")
    print("1. (Re)Create Product Table")
    print("2. Add new product")
    print("3. Update existing product")
    print("4. Delete existing product")
    print("5. Find products")
    print("6. List products")
    print("0. To exit")

def handleChoice():
    choice = input("Please select an option: \n")
    if '0' == choice:
        print("Bye!")
        sys.exit()
        quit()
    elif "1" == choice:
        print("\nRe)Create Product Table selected")
        create_product_table_UI()
    elif "2" == choice:
        print("\nAdd product")
        insert_UI()
    elif "3" == choice:
        print("\nUpdate product")
        update_UI()
    elif "4" == choice:
        print("\nDelete product")
        delete_UI()
    elif "5" == choice:
        print("\nFind products")
        select_products_UI()
    elif "6" == choice:
        list_products_UI()
    else:
        print("\nPlease select again.")




################## DB SQL Functionality ####################

# CREATE DB AND TABLE #
def create_product_table_UI():
    print("Make sure you read the instructions here.")
    create_table()


def create_table():
    db_name = "coffee_shop.db"
    sql = """create table Product
            (ProductID integer,
            Name text,
            Price real,
            primary key(ProductID))"""
    table_name = "Product"
    
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to recreate it? (y/n): ".format(table_name))
            if response == 'y':
                keep_table = False
                print("The {0} table will be recreated - all existing data will be lost.".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The existing table was kept.")
        else:
            keep_table = False
            print("A new table was created.")

        # create the table if required (not keeping old one)
        if not keep_table:
            cursor.execute(sql)
            db.commit()


# ADD #
# Add to definition for insert_data here!
def insert_data(values):
    print("\nadd DB SQL code here to insert new data")
    # use Python SQL function to insert the data in the DB


def insert_UI():
    # user input is requested
    product_name = input("Please enter name of new product.\n")
    print("Please enter price of %s: " % product_name)
    product_price = input()
    product = (product_name, product_price)
    insert_data(product)


# UPDATE #
# Add to definition for update_product here!
def update_product(data):
    print("\nadd DB SQL code here to update product data")
    # use Python SQL function to update the data in the DB



def update_UI():
    # user input is requested
    product_ID = input("Please enter product ID to edit.\n")
    product_name = input("Please enter the new name: \n")
    print("Please enter price of %s: " % product_name)
    product_price = input()
    data = (product_name, product_price, product_ID)
    update_product(data)    



# FIND #
# Add definition for select_all_products here!
def select_all_products():
    print("\nadd DB SQL code here to select all products")
    # use Python SQL function to select/find the data in the DB

    


# Add definition for select_product here!
def select_product(id):
    print("\nadd DB SQL code here to select product with specific ID")
    # use Python SQL function to select/find the data in the DB
   


def select_products_UI():
    # user input is requested
    choice = input("Enter \'one' for a specific product ID and \'all' for all products in the DB.\n")
    choice = choice.lower()
    choice = choice.strip()
    if choice == 'one':
        product_ID = int(input("Please enter product ID to find.\n"))

        print(select_product(product_ID))
    elif choice == 'all':

        print(select_all_products())
    else:
        print("Please select again.\n")



# DELETE #
# Add definition for delete_product here!
def delete_product(data):
    print("\nadd DB SQL code here to delete product with specific ID")
    # use Python SQL function to delete the data in the DB
    

def delete_UI():
    # user input is requested
    product_ID = int(input("Please enter product ID to delete.\n"))
    data = (product_ID,)
    delete_product(data)
    print("Deleted product ID number %s" % product_ID)


# LIST sort/order products
def list_products_UI():
    print("\nAdd DB SQL code here to list and sort products by name or price.")
    input("\nPress enter to continue.")

# Add list_products() function here; call it in function above





################## MAIN LOOP #########################
if __name__ == "__main__":
    ## main loop
    while True:
        show_menu()
        handleChoice()

          
        
            
    
