"""
This script creates an empty file
"""


filename = "sample1.txt"

#create empty file
def create_file():
    """This function writes to an empty file"""
    with open(filename,"w") as file:
        file.write("Ashish")

create_file()