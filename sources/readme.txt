List of current congress members:
https://github.com/unitedstates/congress-legislators
Filtering CSV to source list:
cat congress/legislators-current.csv | awk -F, '{ print tolower($1$2$3) }' | sed -e 's/\.//g;s/\x20//g;s/\x27//g' | tail -n +2 > congress.txt

Oscars from wikipedia, numbers and symbols removed
