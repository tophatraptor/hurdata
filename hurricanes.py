#!/usr/bin/python2.7
#Python 2.7.9
import sys
import os

class Storm:
    def __init__(self,name,year):
        self.windentries = []
        self.year = year
        self.name = name
    def saffir_simpson_day(self):
        return ssday(self.windentries)
    def addwind(self,windspeed):
        self.windentries.append(windspeed)

def generator(inputfile):
    #Gets all data into list of lists
    #Later for loop can be extended
    #to add/work with additional data
    for line in inputfile:
        yield [x.strip() for x in line.split(',')]

def rank(w):
    if w<64:
        return 0
    elif w>=64 and w<83:
        return 1
    elif w<96:
        return 2
    elif w<113:
        return 3
    elif w<137:
        return 4
    else:
        return 5

def ssday(input):
    a=0
    for x in input:
        a+=rank(x)
    return a/4.0

def main():
    if not os.path.isfile(sys.argv[1]):
        print("Error: file not found")
        sys.exit(1)

    f = open(sys.argv[1],'rt')
    out = open("output.txt",'w')

    times=("0000","0600","1200","1800")

    stormlist = []
    lines = generator(f)

    #Use the generator to add wind data to storm list
    for x in lines:
        if len(x)==4:
            stormlist.append(Storm(x[0],int(x[0][4:8])))
        else:
            if x[1] in times:
                stormlist[len(stormlist)-1].addwind(int(x[6]))

    simpsondata = {}
    #Generate dictionary of saffir simpson totals
    for storm in stormlist:
        if storm.year in simpsondata:
            simpsondata[storm.year]+=storm.saffir_simpson_day()
            print(storm.year,simpsondata[storm.year])
        else:
            simpsondata[storm.year]=storm.saffir_simpson_day()
            print(storm.year,simpsondata[storm.year])

    for k,v in simpsondata.items():
        out.write("{}\t{}\n".format(k,v))

if __name__=='__main__':
    main()
