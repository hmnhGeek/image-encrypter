import shutil
import gzip

def comprss(infile, outfile):
    with open(infile, 'rb') as orig_file:
        with gzip.open(outfile, 'wb') as zipped_file:
            zipped_file.writelines(orig_file)


def decomprss(gzfile, outfile):

    inF = gzip.open(gzfile, 'rb')
    outF = open(outfile, 'wb')
    outF.write( inF.read() )
    inF.close()
    outF.close()
