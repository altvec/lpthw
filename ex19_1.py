def top_gear_episodes(season, episodes):
    print "There are %d episodes in %d season of Top Gear\n" % (
        episodes, season)

# 1
print ">>> 1"
top_gear_episodes(2, 10)

# 2 some 'math'
print ">>> 2"
top_gear_episodes(6 + 2, 5 + 5)

# 3 using vars
print ">>> 3"
season = 9
episodes = 8
top_gear_episodes(season, episodes)

# 4 vars + some 'math'
print ">>> 4"
top_gear_episodes(season - 2, episodes)

# 5
print ">>> 5"
season = int(raw_input("Enter season: "))
episodes = int(raw_input("Enter number of episodes: "))
top_gear_episodes(season, episodes)

# 6
print ">>> 6"
season = int(raw_input("Enter season: "))
episodes = int(raw_input("Enter number of episodes: "))
top_gear_episodes(season + 4, episodes + 1)

# 7
print ">>> 7"
top_gear_episodes(int(raw_input("Enter season: ")),
    int(raw_input("Number of episodes: ")))

# 8
print ">>> 8"
def prompt():
    season = int(raw_input("Enter season: "))
    episodes = int(raw_input("Enter number of episodes: "))
    top_gear_episodes(season, episodes)

prompt()

# 9
print ">>> 9"
def p_season(s):
    return s

def p_episode(e):
    return e

top_gear_episodes(p_season(7), p_episode(9))

# 10
# we can use argv from sys module and pass variables to function as arguments