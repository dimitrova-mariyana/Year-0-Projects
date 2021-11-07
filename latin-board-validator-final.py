puzzle = [] # a list to store the values of the puzzle in a 2D array
error = [] # a list to store the number of errors occuring in the validation process. A value of 1 will be appended each time a function returns False.

def load_file(filename):
    try:
        #for every line in the puzzle file, append every character separated by a blank string to the puzzle list.
        infile = open(filename, "r")
        for line in infile:
            if line != "":
                puzzle.append(line.split())
        print(puzzle)   #-> used only for testing
        return True
        
    except FileNotFoundError:
        print("ERROR: This file does not exist in the directory.")
        error.append(1) 
    except: # a catch-all exception for any other potential errors.
        print("ERROR: A file I/O error has occurred.")
        error.append(1)
    return False

filename = input("Please enter a filename: ") # only required input from the user - the name of the file they wish to validate

if load_file(filename) is True: 
    def grid_size(puzzle):
        count = 0 # a counter is implemented to take note of the occurrence of the possible unequal sizes of the rows and columns being iterated.
        for row in range(0, len(puzzle)):
            if len(puzzle[row])!= len(puzzle):
                count += 1 
        if count > 0: 
            print("ERROR: The puzzle is NOT a valid NxN grid. There are ", count,"surplus characters.")
            error.append(1)
            return False
        else: 
            print("PASS: The puzzle is a valid NxN grid.")
            return True
    grid_size(puzzle)

    def distinct_chars(puzzle):
        #the puzzle list is "flattened", meaning the nested lists will become a one-dimentional list, allowing for the use of the set function.
        flat_list = [item for sublist in puzzle for item in sublist]
        if len(puzzle) != len(set(flat_list)):
            print("ERROR: There are too many different N characters in the grid.")
            error.append(1)
            return False
        else:
            print("PASS: The puzzle contains N distinct characters.")
            return True
    distinct_chars(puzzle)

    #Both following functionsa have the same structure, again allowing the set function to determine the presence of duplicate characters due to it removing them by default.

    def duplicate_char_rows(puzzle): 
        count = 0 
        for line in puzzle:
            if len(line) != len(set(line)):
                count += 1
        if count > 0:
            print("ERROR: There are", count, "duplicate items in the puzzle rows.")
            error.append(1) 
            return False
        else:
            print("PASS: There are NO duplicate items in the puzzle rows.") 
            return True 
    duplicate_char_rows(puzzle)


    def duplicate_char_columns(puzzle):
        count = 0
        switched_rows = zip(*puzzle) #the zip function swtiches the rows and the columns around, allowing us to perform the same check to the flipped data.
        for line in switched_rows:
            if len(line) != len(set(line)):
                count += 1
        if count > 0:
            print("ERROR: There are", count, "duplicate items in the puzzle columns.")
            error.append(1)
            return False
        else:
            print("PASS: There are NO duplicate items in the puzzle columns.")
            return True
    duplicate_char_columns(puzzle)

    def validate_puzzle(puzzle, filename):
        if len(error) == 0: # whenever no errors have occured (all functions returned True), the puzzle is validated. 
            outfile = open("VALIDATED_" + filename, "w")
            for row in range(0, len(puzzle)):
                for col in range(0, len(puzzle[row])):
                    outfile.write(puzzle[row][col] + " ")
                outfile.write("\n")
            print("Puzzle has been validated and saved.")
        else: #if errors have occured, the puzzle is not validated. Number of errors is displayed to the user.
            print("Puzzle has NOT been validated as it contains", len(error), "errors.")
            return
    validate_puzzle(puzzle, filename)
