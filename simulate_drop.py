##### ADD AS PRIVATE METHOD IN BOSS BASE CLASS

from collections import Counter
from dataclasses import dataclass
from boss import boss_factory
from drop_rate import DropRates


def simulate_once(boss_name: str, n_kills: int) -> None:
    boss = boss_factory(boss_name)

    for _ in range(n_kills):
        boss.roll()

    drops = boss.drop_history

    drop_summary = Counter(drops)

    print(drop_summary)


def simulate_many(boss_name: str, n_trials: int, n_kills_per_trial: int) -> None:
    print(f"Simulating {boss_name} for {n_trials} trials of {n_kills_per_trial} kills")
    for _ in range(n_trials):
        simulate_once(boss_name, n_kills_per_trial)


if __name__ == "__main__":
    simulate_many("Leviathan", 10, 1000)
