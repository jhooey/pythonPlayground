from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("Copying from {} to {}".format(from_file, to_file))

indata = open(from_file).read()

print ("The input file is {} bytes long".format(len(indata)))

print ("Does the output file exist? {}".format(exists(to_file)))
print ("Ready, hit RETURN to continue, CTR-C to abort.")
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done"

out_file.close()
