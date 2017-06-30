#!/usr/bin/env python
from PIL import Image
import numpy as np
import os, pickle
from scipy.misc import imshow, imsave
import comprssr
import vigenerecipher as vc

def spl(addr):
    reverse = addr[-1:-len(addr)-1:-1]
    imgname = ''
    imgcounter = False

    while 1:
        popped = reverse[0]
        reverse = reverse[1::]

        if popped == '.' or ('.' in imgname and '/' not in imgname):
            imgname += popped
        elif '.' in imgname and '/' in imgname:
            break

    imgname = imgname[1::]
    imgname = imgname.rstrip(imgname[-1])

    return reverse[-1:-len(reverse)-1:-1]+popped+'/',imgname[-1:-len(imgname)-1:-1]
            
def get_array(addr, password):

    directory, filename = spl(addr)

    if len(filename) >= len(password):
        filename = vc.cipher(filename, password)

        print "Opening Image..."
        img = Image.open(addr)
        d = np.asarray(img, dtype = 'int32')

        print "Encrypting..."
        f = open(directory+filename+'.dat', 'wb')
        pickle.dump(d, f)
        f.close()

        print "Compressing..."
        comprssr.comprss(directory+filename+'.dat', directory+filename+'.gz')

        os.remove(directory+filename+'.dat')

        print "Removing original image..."
        os.remove(addr)

        print "Done"
    else:
        print "The filename must be larger or equal to the length of your password."
        print "File that caused error: "+filename
        os.system('exit')

def image(image_bin, password, image_extension = '.jpg',save = False, show = False):

    d, f = spl(image_bin)
    
    print "Decompressing..."
    comprssr.decomprss(d+f+'.gz', d+f+'.dat')
    
    print "Ananlysing file..."
    array = np.load(d+f+'.dat')

    print "Removing binary file..."
    os.remove(d+f+'.dat')


    if show:
        imshow(array)

    if save:
        imsave(d+vc.decipher(f, password)+image_extension, array)
        
    print "Done"
