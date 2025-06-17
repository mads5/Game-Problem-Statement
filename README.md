# Game Problem Statement

This repository contains a small Python script for generating a balanced 20
round schedule for two groups of ten teams.

The `schedule_generator.py` script implements the following requirements:

- Each team in group A plays every team in group B twice (home and away).
- Each of the 20 rounds has exactly ten matches with five home teams from each
  group.
- No pair of teams meets twice before all cross‑group combinations have been
  played.
- At no point does any team have more than two additional home or away matches
  compared to the opposite.

Running the script creates `schedule.csv` containing the full schedule. The
script also performs a balance check to ensure the constraints are met.

```bash
python3 schedule_generator.py
```

After running, `schedule.csv` contains three columns: `Round`, `HomeTeam` and
`AwayTeam`.
