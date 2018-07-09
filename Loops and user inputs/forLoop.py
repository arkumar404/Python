# emails = ['me@gmail.com','you@hotmail.com','they@gmail.com']

# for item in emails:
#     if 'gmail' in item:
#         print(item)


# For Loop with Multiple Lists
names = ['James','John','Jack']
email_domain = ['gmail','hotmail','yahoo']

for i,j in zip(names,email_domain):
    print(i,j)
