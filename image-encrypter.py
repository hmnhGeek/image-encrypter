#!/usr/bin/env python
import argparse as ap
import imgencrypt as icr
import vigenerecipher as vc
from getpass import getpass
import imagefinder
import signup

p = ap.ArgumentParser()
p.add_argument('-c', action = 'store_true', help = 'To encrypt!!')
p.add_argument('-d', action = 'store_true', help = 'To decrypt!!')
p.add_argument('--findall', action = 'store_true', help = 'To operate on all images in a folder.!!')
p.add_argument('--format', action = 'store', dest = 'format', type = str, help = 'To specify the format.')
p.add_argument('--show', action = 'store_true', help = 'To show the image.')
p.add_argument('--save', action = 'store_true', help = 'To save the image.')
p.add_argument('address', type = str, help = 'Pass image address.')

args = p.parse_args()

if signup.check():
    f = open('password.txt', 'r')
    correct = f.read()
    f.close()

    password = getpass()
    try:
        correctpassword = vc.decipher(correct, password)
    except RuntimeError:
        correctpassword = ''

    if password.upper() == correctpassword:

        if args.findall:
            if args.c and not args.d:
                images = imagefinder.findallimages(args.address)

                if args.address[-1] != '/':
                    args.address += '/'

                for image in images:
                    icr.get_array(args.address+image, password)
            else:
                dats = imagefinder.findallbinaries(args.address)

                if args.address[-1] != '/':
                    args.address += '/'

                for dat in dats:
                    icr.image(args.address+dat, password, args.format, args.save, args.show)
            
        else:

            if args.c and not args.d:
                icr.get_array(args.address, password)
            else:
                icr.image(args.address, password, args.format, args.save, args.show)

    else:
        print "Wrong password!!"

else:
    print "Please signup first by entering a password below."

    try:
        while 1:
            print
            passw = getpass("Password: ")
            cpassw = getpass("Confirm Password: ")

            if passw == cpassw:
                signup.signup(passw)
                print "Signed Up."
                break
            else:
                print "Passwords did not match. CTRL-C to quit."
    except KeyboardInterrupt:
        pass
