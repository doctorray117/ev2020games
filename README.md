# ev2020games
Anagram comparison from two word lists, based on the game directive at https://www.electoral-vote.com/evp2020/Pres/Maps/Nov03.html#item-7

## How it works

To determine if a letters from a word in the source can be found in the dictionary, mark off the first letter in the dictionary word that appears when testing each of the letters in the source word.  If you've marked off all the letters in the dictionary word, you have a match.

This python script does exactly that.

The code isn't written to be super pretty, probably imports stuff it doesn't need, etc.

## Inputs

Create a sourcefile and a dictionaryfile that contain all lowercase versions of the words to compare, without spaces or special characters.  Doing this is beyond the scope of the readme, but really contains a little find and replace in notepad, and some tolower() in awk, with some sed sprinkled in here and there.

## Usage

./findevmatches.py -s source/congress.txt -d source/oscars.txt

## sources gathered so far:

1. Current member of Congress → Academy Award-winning film
https://github.com/unitedstates/congress-legislators
https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films

2. Political slogan used by any U.S. candidate → Periodic table element
https://en.wikipedia.org/wiki/List_of_U.S._presidential_campaign_slogans
https://gist.githubusercontent.com/GoodmanSciences/c2dd862cd38f21b0ad36b8f96b4bf1ee/raw/1d92663004489a5b6926e944c1b3d9ec5c40900e/Periodic%2520Table%2520of%2520Elements.csv

3. Democratic nominee for president (winner or loser) → Beatles song title
http://beatlesbible.com/songs/
https://en.wikipedia.org/wiki/List_of_United_States_Democratic_Party_presidential_tickets

