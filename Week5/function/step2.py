numlist = []
str_input = input("Please enter a statement: ")
 
def count_letters(str):
    print("# of Upper Case Letters: ", sum(1 for x in str if x.isupper()))
    print("# of Lower Case Letters: ", sum(1 for x in str if x.islower()))

count_letters(str_input)