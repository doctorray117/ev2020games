#!/usr/bin/python3

## findevmatches.py
##
## Notes:
## re.sub(r'[^a-zA-Z]','' appears a bunch, this is simply removing anything non-alpha from the string.
## When needed, .lower is added to make the comparisons all lower case.

import argparse, logging, re
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

parser = argparse.ArgumentParser(description='Anagram solver for ElectoralVote2020.')
parser.add_argument("--sourcefile", "-s", type=str, help="Source file for searching dictionary (Category 1)")
parser.add_argument("--dictionary", "-d", type=str, help="Dictionary file (Category 2)")
args = parser.parse_args()

## open text files for reading
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

## determine if the sourceword component letters can be made into an anagram of dictionaryword
def anagram(sourceword, dictionaryword):
  sourcearray = tuple(re.sub(r'[^a-zA-Z]','',sourceword.lower()));
  dictarray = list(re.sub(r'[^a-zA-Z]','',dictionaryword.lower()));
  for letter in sourcearray:
    for i in range(len(dictarray)):
      if dictarray[i] == letter:
        dictarray.remove(dictarray[i])
        break
  if len(dictarray) == 0:
    return True
  return False

## main
## for each phrase in the source list, check it against every phrase in the dictionary list
## store the anagrams in the results list
results = []
for sourceword in source:
  for dictionaryword in dictionary:
    if anagram(sourceword, dictionaryword):
      results.append([sourceword, dictionaryword])

## log all results if in debug
logging.debug(results)

## find the length of the longest dictionary word (in cases of multiple matches)
maxlength = 0
for i in range(0,len(results)):
  if len(re.sub(r'[^a-zA-Z]','',results[i][1])) > maxlength:
    maxlength = len(re.sub(r'[^a-zA-Z]','',results[i][1]))

## now print all items that match this length with their point values
for i in range(0,len(results)):
  if len(re.sub(r'[^a-zA-Z]','',results[i][1])) == maxlength:
    print (str(results[i]) + " " + str(getpoints(len(re.sub(r'[^a-zA-Z]','',results[i][1])))) + " points")
