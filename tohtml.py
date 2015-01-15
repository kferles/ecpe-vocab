import sys

wordClass = "<div class=\"word\">"
defClass = "<div class=\"def\">"
endDiv = "</div>"
br = "</br>"

for line in sys.stdin:
    word, defs = line.rstrip('\n').split(';', 1)
    defs = defs.split('|')

    print wordClass, word, endDiv,";",

    for df in defs:
        print defClass, df, endDiv, br,
    print
