import csv
def main ():
    
    #Get input from the user
    ID_INDEX = 0
    student_index = input("Enter the sudent I-Number: ")
    students_dict = read_dictionary("students.csv", ID_INDEX)

    if student_index in students_dict.keys():
        print(students_dict[student_index][1])
    
    else:
        print("No such student")


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


        
# Call main to start this program.
if __name__ == "__main__":
    main()




