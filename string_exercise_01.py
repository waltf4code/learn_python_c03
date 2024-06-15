# Python 101: String Exercise 01

# 1. From the string "Welcome to python 101 Strings", extract text and create/print a new string that says
# * "Welcome Ring To Tyler"
# * Every first letter in a word should be capitalized(title format)

msg = "Welcome to python 101 Strings"
print(msg)

print("-"*20)
# Print the same string backwards
msg = "Welcome Ring to Tyler"
print(msg.title())

newmsg = "Hint: Google is your friend..."
print(newmsg[::-1])

