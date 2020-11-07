#!/bin/bash

echo 1. Current member of Congress → Academy Award-winning film
./findevmatches.py -s sources/quiz01/legislators-current.txt -d sources/quiz01/oscars.txt
echo ""

echo 2. Political slogan used by any U.S. candidate → Periodic table element
./findevmatches.py -s sources/quiz02/politicalslogans.txt -d sources/quiz02/elements.txt
echo ""

echo 3. Democratic nominee for president _winner or loser_ → Beatles song title
./findevmatches.py -s sources/quiz03/democrats.txt -d sources/quiz03/beatlessongs.txt
echo ""

echo 4. Republican nominee for president _winner or loser_ → Religious figure _living or dead, any religion_
./findevmatches.py -s sources/quiz04/republicans.txt -d sources/quiz04/somereligiousfigures.txt
echo ""

echo 5. President who died in office → Disease
./findevmatches.py -s sources/quiz05/presidents-who-died-in-office.txt -d sources/quiz05/diseases.txt
echo ""

echo 6. U.S. political party _any, and including the word 'party'_ → "Star Wars" planet, character, or race
./findevmatches.py -s sources/quiz06/parties.txt -d sources/quiz06/starwars.txt
echo ""

echo 7. Politician who played college sports → Professional sports team _city and mascot, or just mascot_
./findevmatches.py -s sources/quiz07/spotspoliticians.txt -d sources/quiz07/professionalsports.txt
echo ""

echo 8. Person who served as Secretary of the Treasury → World currency _current or past_
./findevmatches.py -s sources/quiz08/treasurysecretaries.txt -d sources/quiz08/currencies.txt
echo ""

echo 9. Any living politician → Palindrome
./findevmatches.py -s sources/quiz09/longnamesalive.txt -d sources/quiz09/palindromes.txt
echo ""

echo 10. Any dead politician → Shakespeare character
./findevmatches.py -s sources/quiz10/legislators-historical.txt -d sources/quiz10/shakespeare.txt
