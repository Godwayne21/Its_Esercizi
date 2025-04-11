import string

def validate_password(password):
    count_uppercase = 0
    count_specialChar = 0

    alfabeto_maiuscolo = list(string.ascii_uppercase)
    special = ['+', '*', '#', '@', '!', '?', '&', '%']

    for i in password:

        if i in special:

            count_specialChar += 1
        
        if i in alfabeto_maiuscolo:

            count_uppercase += 1
        
    print (count_uppercase)
    print (count_specialChar)

validate_password('ADsddadS')
validate_password('*+sss')