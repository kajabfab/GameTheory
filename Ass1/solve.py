from sys import argv

WDSE_FL = 0  # weakly dominant strategy equilibrium

def FBRS(player, strategy_profiles):  # Find best response strategy
    global WDSE_FL
    best_response = []

    MS = 0
    for s in range(0, len(strategy_profiles)):
        if strategy_profiles[s][player] > strategy_profiles[MS][player]:
            MS = s
            best_response = [MS]
        elif strategy_profiles[s][player] == strategy_profiles[MS][player]:
            WDSE_FL = 1
            best_response.append(s)
    print player+1, best_response, strategy_profiles
    return best_response


def FCS(br1, br2):  # Find commmon strategies
    return list(set(br1) & set(br2))


def FBS(player, player_strategy):  # Find best strategy
    global WDSE_FL
    best_strategy = []
    for sp in range(0, len(player_strategy)):
        if sp == 0:
            best_strategy = FBRS(player, player_strategy[sp])
        else:
            tmp_best_strategy = FBRS(player, player_strategy[sp])
            if len(tmp_best_strategy) > 1:
                WDSE_FL = 1
            best_strategy = FCS(best_strategy, tmp_best_strategy)

        if not best_strategy:
            break
    return best_strategy

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

    ES = []  # equilibrium strategy

    for i in range(0, NP):
        NPS = strategy[i]  # number of player strategies

        player_strategy = []
        INC = 1
        for j in range(0, i):
            INC *= strategy[j]

        for j in range(0, NSP):
            player_strategy.append(strategy_profiles[j:j+(INC*NPS):INC])

        # if i == 0:  # P1
        #     for j in range(0, NSP/NPS):
        #         player_strategy.append(strategy_profiles[j*NPS:(j+1)*NPS])
        # else:
        #     for j in range(0, NSP/NPS):
        #         player_strategy.append(strategy_profiles[j:j+(INC*NPS):INC])
                
        print i+1, INC, player_strategy

        BSP = FBS(i, player_strategy)  # best strategy for player
        if not BSP:
            WDSE_FL = -1
            break
            #print "No dominant equilibrium strategy exists"
            #raise SystemExit
        else:
            ES.append(BSP[0]+1)

    if WDSE_FL == 0:
        print "The strongly dominant strategy is", ES
    elif WDSE_FL == 1:
        print "The weakly dominant strategy is", ES
    elif WDSE_FL == -1:
        print "No dominant equilibrium strategy exists"

        
