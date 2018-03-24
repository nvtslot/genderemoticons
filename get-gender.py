import sys

female=[name.strip() for name in open("/home/s3212386/iwo/names/nl-female.txt").readlines()]
male=[name.strip() for name in open("/home/s3212386/iwo/names/nl-male.txt").readlines()]

for line in sys.stdin:
    name = line.strip().split("\t")[0].lower() # assumes name is first in tab-separated input
    f=0
    m=0
    for n in female:
        if n in name:
            f+=1
    for n in male:
        if n in name:
            m+=1

    if f > m:
        print("female\t{}".format(line.strip()))
    elif m > f:
        print("male\t{}".format(line.strip()))
    else:
        pass #not found
