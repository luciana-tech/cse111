from datetime import datetime
from datetime import date
import csv

#Exceeding requirements: print a reminder of how many days until the New Years Sale begins (Jan 1) at the bottom of the receipt.
current_date_and_time = datetime.now()


def read_dictionary(filename, key_column_index):
    dictionary = {}
    try:
        with open(filename, "rt") as csv_file:
            reader = csv.reader(csv_file)
            #skip the first row/heading of the CSV file.
            next(reader)
            #Reads the rows in the CSV file one row at a time.
            #The reader object returns each row as a list.
            for row_list in reader:
                if len(row_list) != 0:
            # From the current row, retrieve the data
            # from the column that contains the key.
                    key = row_list[key_column_index]
                    # Store the data from the current
                    # row into the dictionary.
                    dictionary[key] = row_list
    except FileNotFoundError:
        print("Error: Missing file 'products.csv' was not found.")
                    
# Return the dictionary.
    return dictionary


def main():
    #Calls the read_dictionary function and stores the compound dictionary in a variable named products_dict.
    products_dict = read_dictionary("products.csv", 0)
    PRODUCT_NAME_INDEX = 1
    PRODUCT_PRICE_INDEX = 2

     # Print days until New Year's Sale
    today = date.today()
    next_year = today.year + 1
    new_years_day = date(next_year, 1, 1)
    days_until_sale = (new_years_day - today).days
        

    try:
        with open("request.csv", "rt") as csv_file:
            reader = csv.reader (csv_file)
            #skip the first row/heading of the CSV file.
            next(reader)
            #Uses a loop that reads and processes each row from the request.csv file. 
            print("Inkom Emporium")
            item_total = 0
            subtotal = 0
            for row_list in reader:
                if len(row_list) != 0:
            # From the current row, retrieve the data
            # from the column that contains the key.
                    product_id = row_list[0]
                    # For the current row, retrieve the
                # values in columns 1. 
                product_name = products_dict[product_id][1]
                quantity = int(row_list[1])
                price = float(products_dict[product_id][2]) 

                print(f"{product_name}: {quantity} @ {price}")
                #Sum items total quantity
                item_total += quantity
                subtotal += (quantity*price)
                sales_tax = subtotal*0.06
                total = subtotal + sales_tax
        print(f"Number of items: {item_total}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        print("Thank you for shopping at the Inkom Emporium.")
        print(f"{current_date_and_time:%A %I:%M %p}")

    except FileNotFoundError:
        print("Error: The file 'request.csv' was not found.")

    except KeyError as e:
        print(f"Error: Product ID {e} not found in request.csv was not found in products dicionary")

    print(f"\n🎉 Only {days_until_sale} day(s) until our New Year's Sale on January 1st!")
if __name__ == "__main__":
    main()                

