import datetime

now = datetime.datetime.now()

#Using the strftime() method for formatting, for more, visit strftime.org
Date = now.strftime("%Y-%M")

#create empty file
def create_file():
    """This function writes to an empty file"""
    with open(Date+".txt","w+") as file:
        file.write("Ashish")

create_file()
