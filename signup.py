
import vigenerecipher as vc

def check():

    f = open('password.txt', 'r')
    s =  f.read()
    f.close()

    if s == '':
        return False
    else:
        return True

def signup(password):

    f = open('password.txt', 'w')
    f.write(vc.cipher(password, password))
    f.close()

    
