import textwrap

# Font B: 42 wide?
# printer.writeBytes(27, 33, 1)

# arr = ["octopi", "bunnies",  "Catan crochet things", "Toshi (green turtle)", "mini Lego sets", "owl", "longhorn plush", "armadillo ornament", "Whataburger tents"]

arr = ["Catan", "Carcassonne", "playing cards", "Hanabi", "Dominion", "Bananagrams", "101 Games", "Simpsons trivia", "Pandemic", "The Resistance", "Space Alert", "Blokus", "Trivial Pursuit 2000s", "Pikachu case", "various movies/games", "1st hat trick puck", "Cornell puck", "chia pet skull", "Emily mouse", "old TV remote", "old laptop HDD", "mouse/keyboard", "anniversary card+holder"]

lines = [textwrap.wrap(("-" + item), 20) for item in arr]
lines = [item for sublist in lines for item in sublist]
# if len(lines)/2 != 0:
#   lines.append([""])
left = lines[:len(lines)/2]
right = lines[len(lines)/2:]
if "-" not in right[0][0]:
  left.append("  " + right[0])
  right.remove(right[0])

if len(left) < len(right):
  for x in range(len(right)-len(left)):
    left.append("")
elif len(right) < len(left):
  for x in range(len(left)-len(right)):
    right.append("")

left = [item.ljust(21) for item in left]
for i in range(len(right)):
  if right[i] == "" or right[i][0] != "-":
    right[i] = "  " + right[i]
# print(left)
# print(right)

#####TODO: Pad left[x] to push right[x] side to middle


columns = []
for i in range(len(left)):
  columns.append(left[i] + " " + right[i])

# print(columns)