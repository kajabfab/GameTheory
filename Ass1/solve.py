from sys import argv

if len(argv) == 2:
    FN = str(argv[1])
else:
    FN = str(raw_input("Enter Input File: "))

def validate(file):
    pass

F = open(FN, 'r')
headers = F.readline().strip()
header = headers.split()
if header[0] != "NFG" or header[1] != "1" or header[2] != "R":
    print "Invalid Input Format Given"
else:
    Title = ""
    for t in header[3:]:
        Title += t + " "
    Title = Title.strip()
    # print Title

    info = F.readline().strip().split('} {')

    players = info[0].strip('{ }').split()
    player = []
    for p in players:
        player.append(p.strip('"'))

    # print player

    strategies = info[1].strip('{ }').split()
    strategy = []
    for s in strategies:
        strategy.append(int(s))

    # print strategy

    F.readline()
    body = F.readline().strip().split()

    payoff = []
    for p in body:
        payoff.append(int(p))

    # print payoff

    utility = []