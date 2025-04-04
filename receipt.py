import csv

def read_dictionary(filename, key_column_index):
    dictionary = {}
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
    # Return the dictionary.
    return dictionary



def main():
    #Calls the read_dictionary function and stores the compound dictionary in a variable named products_dict.
    products_dict = read_dictionary("products.csv", 0)
    PRODUCT_NAME_INDEX = 1
    PRODUCT_PRICE_INDEX = 2
    print(products_dict)
    
    with open("request.csv", "rt") as csv_file:
        reader = csv.reader (csv_file)
        #skip the first row/heading of the CSV file.
        next(reader)
        #Uses a loop that reads and processes each row from the request.csv file. 
        print("Requested items: ")
        for row_list in reader:
            if len(row_list) != 0:
        # From the current row, retrieve the data
        # from the column that contains the key.
                product_id = row_list[0]
                # For the current row, retrieve the
            # values in columns 1. 
            quantity = int(row_list[1]) 
            print(f"{products_dict[product_id][1]}: {row_list[1]} @ {products_dict[product_id][2]}")
if __name__ == "__main__":
    main()                

