# ev2020games
Anagram comparison from two word lists, based on the game directive at https://www.electoral-vote.com/evp2020/Pres/Maps/Nov03.html#item-7

## How it works

To determine if a letters from a word in the source can be found in the dictionary, mark off the first letter in the dictionary word that appears when testing each of the letters in the source word.  If you've marked off all the letters in the dictionary word, you have a match.

This python script does exactly that.

The code isn't written to be super pretty, probably imports stuff it doesn't need, etc.

## Inputs

Create a sourcefile and a dictionaryfile that contain all the words or phrases to compare.  The program will remove any special characters, though you may consider replacing any non-English letters to their English equivalents as those would otherwise be removed.

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

4. Republican nominee for president (winner or loser) → Religious figure (living or dead, any religion)

https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States_who_died_in_office
https://www.wikidata.org/wiki/Wikidata:Lists/List_of_biblical_characters
https://en.wikipedia.org/wiki/List_of_Catholic_saints
https://en.wikipedia.org/wiki/List_of_founders_of_religious_traditions

5. President who died in office → Disease

https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States_who_died_in_office
https://en.wikipedia.org/wiki/Lists_of_diseases

6. U.S. political party (any, and including the word 'party') → "Star Wars" planet, character, or race

https://en.wikipedia.org/wiki/List_of_political_parties_in_the_United_States
https://starwars.fandom.com/wiki/List_of_planets
https://en.wikipedia.org/wiki/List_of_Star_Wars_characters

7. Politician who played college sports → Professional sports team (city and mascot, or just mascot)

8. Person who served as Secretary of the Treasury → World currency (current or past)

https://home.treasury.gov/about/history/prior-secretaries -- site was down on election day... isitdns.com
https://en.wikipedia.org/wiki/List_of_currencies

9. Any living politician → Palindrome

There's a lot of politicians out there, so this should be filled out more.

https://github.com/unitedstates/congress-legislators -- current legislators
https://en.wiktionary.org/wiki/Appendix:English_palindromes

10. Any dead politician → Shakespeare character

https://github.com/unitedstates/congress-legislators -- historical legislators
https://www.opensourceshakespeare.org/views/plays/characters/chardisplay.php
