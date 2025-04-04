import csv
def main ():
    ID_INDEX = 0
    students_dict = read_dictionary("students.csv", ID_INDEX)

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

#Get input from the user
def get_inumber(ID_INDEX) 
print(input("Enter the sudent I-Number: "))

        
# Call main to start this program.
if __name__ == "__main__":
    main()




