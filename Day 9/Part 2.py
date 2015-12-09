import itertools
from collections import defaultdict
input = """Tristram to AlphaCentauri = 34
Tristram to Snowdin = 100
Tristram to Tambi = 63
Tristram to Faerun = 108
Tristram to Norrath = 111
Tristram to Straylight = 89
Tristram to Arbre = 132
AlphaCentauri to Snowdin = 4
AlphaCentauri to Tambi = 79
AlphaCentauri to Faerun = 44
AlphaCentauri to Norrath = 147
AlphaCentauri to Straylight = 133
AlphaCentauri to Arbre = 74
Snowdin to Tambi = 105
Snowdin to Faerun = 95
Snowdin to Norrath = 48
Snowdin to Straylight = 88
Snowdin to Arbre = 7
Tambi to Faerun = 68
Tambi to Norrath = 134
Tambi to Straylight = 107
Tambi to Arbre = 40
Faerun to Norrath = 11
Faerun to Straylight = 66
Faerun to Arbre = 144
Norrath to Straylight = 115
Norrath to Arbre = 135
Straylight to Arbre = 127"""
input = input.split("\n")
distances = defaultdict(dict)
for line in input:
    line = line.split()
    distances[line[0]][line[2]] = int(line[4])
    distances[line[2]][line[0]] = int(line[4])

longestPath = 0
longestLength = 0

for path in itertools.permutations(distances.keys()):
    current = 0
    for source, destination in zip(path, path[1:]):
        current += distances[source][destination]
    if not longestLength or current > longestLength:
        longestPath = path
        longestLength = current

print longestLength
