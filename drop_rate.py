from collections import Counter
from dataclasses import dataclass
import random

@dataclass
class DropRate:
    item: str
    prob: float


class DropRates:
    def __init__(self, drop_rates: list[DropRate]) -> None:
        self._drop_rates = drop_rates
        self._total_prob = sum(drop.prob for drop in self._drop_rates)
        self._unique_chance = self._calculate_unique_chance()
        
    def _calculate_unique_chance(self) -> float:
        return self._total_prob
    
    def roll_unique(self) -> str:
        normalized_probabilities = [
            DropRate(drop.item, drop.prob / self._total_prob) for drop in self._drop_rates
            ]
            
        cdf = [sum(item.prob for item in normalized_probabilities[:i+1]) for i in range(len(self._drop_rates))]
        random_number = random.random()

        for i, item in enumerate(self._drop_rates):
            if random_number < cdf[i]:
                return item.item
            
    @property
    def drop_rates(self) -> list[DropRate]:
        return self._drop_rates
    
    @property
    def unique_chance(self) -> float:
        return self._unique_chance
    