#importing required modules
import random, string

#variables for password
UPPER = string.ascii_uppercase
LOWER = string.ascii_lowercase
NUMBER = string.digits
PUNCTUATIONS = string.punctuation

#function to generate random password
def password_generator(length, strength):
    password = ""

    #if length provided is 0
    if length == 0:
        print("Don't come crying to me when you're hacked.")
        return

    #else generate a password based on the given strength and length
    else:
        #strength - low
        if(strength == 'L'):
            for i in range (0, length):
                password = password + random.choice(LOWER + UPPER)
            print('Password for you: ', password)

        #strength - medium
        elif(strength == 'M'):
            for i in range (0, length):
                password = password + random.choice(LOWER + UPPER + NUMBER)
            print('Password for you: ', password)

        #strength - high
        elif(strength == 'H'):
            for i in range (0, length):
                password = password + random.choice(LOWER + UPPER + NUMBER + PUNCTUATIONS)
            print('Password for you: ', password)

        #to be displayed if details provided are not correct
        else:
            print('Incorrect details provided')


#driver code
print('!------Random Password Generator------!\n')
print('Please provide the below fields: \n')
print('1. Length \n2. Strength:\n a. L\n b. M\n c. H\n')

try:
    length = int(input('Enter length of the password you wish to have: '))
    strength = input('Enter strength of the password you wish to have: ')
    #calling the function to generate a random password of given length and strength
    password_generator(length, strength)
except:
    print('Please provide the required details')
