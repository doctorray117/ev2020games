#!/usr/bin/python3

import random, argparse, logging, sys
sysrand = random.SystemRandom()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

parser = argparse.ArgumentParser(description='Anagram solver for ElectoralVote2020.')
parser.add_argument("--sourcefile", "-s", type=str, help="Source file for searching dictionary (Category 1)")
parser.add_argument("--dictionary", "-d", type=str, help="Dictionary file (Category 2)")
args = parser.parse_args()

sourcefile = open(args.sourcefile,'r')
source = sourcefile.read().splitlines()
dictionaryfile = open(args.dictionary,'r')
dictionary = dictionaryfile.read().splitlines()

## set the point value array by modified fibbonachi sequence
def getpoints(length):
  count = 1
  points = []
  n1, n2 = 0, 1
  while count <= (length):
    points.append(n1)
    if (count % 2) == 0:
      nth = n1 + n2
      n1 = n2
      n2 = nth
    count += 1
  return sum(points)

def anagram(sourceword, dictionaryword):
  sourcearray = tuple(sourceword);
  dictarray = list(dictionaryword);
  for letter in sourcearray:
    for i in range(len(dictarray)):
      if dictarray[i] == letter:
        dictarray.remove(dictarray[i])
        break
  if len(dictarray) == 0:
    return True
  return False

## iterate through dictionary
results = []
for sourceword in source:
  for dictionaryword in dictionary:
    if anagram(sourceword, dictionaryword):
      results.append([sourceword, dictionaryword])

#print (results)

## find the length of the longest dictionary word (in cases of multiple matches)
maxlength = 0
for i in range(0,len(results)):
  if len(results[i][1]) > maxlength:
    maxlength = len(results[i][1])

## now print all items that match this length
for i in range(0,len(results)):
  if len(results[i][1]) == maxlength:
    print (str(results[i]) + " " + str(getpoints(len(results[i][1]))) + " points")
