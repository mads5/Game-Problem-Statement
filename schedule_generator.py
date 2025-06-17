from itertools import cycle

GROUP_A = [f"A{i+1}" for i in range(10)]
GROUP_B = [f"B{i+1}" for i in range(10)]


def generate_schedule():
    rounds = []
    # first half
    for r in range(10):
        matches = []
        for i in range(10):
            a = GROUP_A[i]
            b = GROUP_B[(i + r) % 10]
            if (i + ((i + r) % 10)) % 2 == 0:
                home, away = a, b
            else:
                home, away = b, a
            matches.append((home, away))
        rounds.append(matches)
    # second half - reverse fixtures
    for r in range(10):
        matches = []
        for i in range(10):
            a = GROUP_A[i]
            b = GROUP_B[(i + r) % 10]
            if (i + ((i + r) % 10)) % 2 == 0:
                home, away = b, a
            else:
                home, away = a, b
            matches.append((home, away))
        rounds.append(matches)
    return rounds


def check_balance(rounds):
    """Ensure no team exceeds home/away difference >2 at any time."""
    home_count = {t: 0 for t in GROUP_A + GROUP_B}
    away_count = {t: 0 for t in GROUP_A + GROUP_B}
    for rnd, matches in enumerate(rounds, 1):
        for home, away in matches:
            home_count[home] += 1
            away_count[away] += 1
        for team in home_count:
            diff = abs(home_count[team] - away_count[team])
            if diff > 2:
                raise ValueError(f"Balance violated for {team} after round {rnd}")


def save_csv(rounds, path="schedule.csv"):
    import csv
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Round", "HomeTeam", "AwayTeam"])
        for rnd, matches in enumerate(rounds, 1):
            for home, away in matches:
                writer.writerow([rnd, home, away])


def main():
    rounds = generate_schedule()
    check_balance(rounds)
    save_csv(rounds)
    print(f"Generated schedule with {len(rounds)} rounds. Saved to schedule.csv")


if __name__ == "__main__":
    main()
