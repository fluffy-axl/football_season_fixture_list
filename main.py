import random

teams = ["Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton & Hove Albion", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Leicester City",
         "Leeds United", "Liverpool", "Manchester City", "Manchester United", "Newcastle United", "Nottingham Forest", "Southampton", "Tottenham Hotspur",
         "West Ham United", "Wolverhampton Wanderers"
         ]

i = 0
n = len(teams)

fixtures = []

while i < n:
    pop = teams.pop(random.randrange(len(teams)))
    i += 1
    pop = str(pop)
    fixtures.append(pop)

it = iter(fixtures)
for x in it:
    print(f'{x} vs {next(it)}')
