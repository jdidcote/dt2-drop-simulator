import random

from drop_rate import DropRate, DropRates

class Base:
    def __init__(self, time_to_kill: float, drop_rates: DropRates) -> None:
        super().__init__()
        self.kills = 0
        self.time_spent = 0
        self._time_to_kill = time_to_kill
        self._drop_rates = drop_rates
        self.drop_history = []
    
    def roll(self):
        rand_val = random.uniform(0, 1)

        if rand_val <= self._drop_rates.unique_chance:
            drop = self._drop_rates.roll_unique()
        else:
            drop = "Nothing"

        self.drop_history.append(drop)



class Leviathan(Base):
    def __init__(self) -> None:
        time_to_kill = 120
        drop_rates = self._get_drop_rates()
        super().__init__(time_to_kill, drop_rates)

    @staticmethod
    def _get_drop_rates() -> DropRates:
        drops=  [
            DropRate("Awakener's orb", 1 / 53),
            DropRate("Smoke quartz", 1 / 180),
            DropRate("Chromium ingot", 1 / 320),
            DropRate("Venator vestige (roll)", 1 / 960 * 3),
            DropRate("Leviathan's lure", 1 / 960),
            DropRate("Virtus mask", 1 / 2880),
            DropRate("Virtus robe top", 1 / 2880),
            DropRate("Virtus robe bottom", 1 / 2880) 
            ]
        return DropRates(drops)


def boss_factory(boss_name: str) -> Base:
    bosses = {
        "Leviathan": Leviathan
        }

    if boss_name not in bosses:
        raise ValueError(f"Invalid boss name: {boss_name}")
    
    return bosses[boss_name]()
    

if __name__ == "__main__":
    boss = boss_factory("Leviathan")

    for _ in range(100):
        boss.roll()
    print(boss.drop_history)