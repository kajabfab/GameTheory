from sys import argv

if len(argv) == 2:
    FN = str(argv[1])
else:
    FN = str(raw_input("Enter Input File: "))

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

    players_str = info[0].strip('{ }').split()
    player = []  # player names
    for p in players_str:
        player.append(p.strip('"'))

    NP = len(player)  # no of players

    # print player

    strategy_str = info[1].strip('{ }').split()
    strategy = []  # no of strategies of player i
    for s in strategy_str:
        strategy.append(int(s))

    # print strategy

    F.readline()
    body = F.readline().strip().split()

    payoff = []
    for p in body:
        payoff.append(int(p))

    # print payoff

    strategy_profiles = []

    NSP = 1  # no of strategy profiles
    for n in strategy:
        NSP *= n

    # print NSP

    for i in range(0, NSP):
        strategy_profiles.append(tuple(payoff[i*NP:(i+1)*NP]))

    # print strategy_profiles
    
    for i in range(0, NP):
        NPS = strategy[i]  # number of player strategies

        player_strategy = []
        INC = 1
        for j in range(0, i):
            INC *= strategy[j]

        if i == 0:  # P1
            for j in range(0, NSP/NPS):
                player_strategy.append(strategy_profiles[j*NPS:(j+1)*NPS])
        else:
            for j in range(0, NSP/NPS):
                player_strategy.append(strategy_profiles[j:j+(INC*NPS):INC])

        # print i+1, INC, player_strategy
