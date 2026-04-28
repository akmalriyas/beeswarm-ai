# Candy Ring

![Candy Ring](https://static.wikia.nocookie.net/bee-swarm-simulator/images/1/1a/Candy_Ring.png/revision/latest?cb=20240528162800)

**Level:** 14
**Color:** Any
**Limit:** 1
*"Keeps some sugar on hand to satisfy on demand."*
🎄Beesmas

| Stat | Value | Notes |
| :--- | :--- | :--- |
| **+Energy** | (Variable) | Random value between +60 and +80. |
| **+Convert Amount%** | (Variable) | Random value between +20% and +30%. |
| **+Ability Rate%** | (Variable) | Variable, depends on Caustic/Non-Caustic status. |
| **+Honey At Hive%** | (Variable) | Random value between +2% and +5%. |
| **+Honey Per Goo%** | (Variable) | Base is +1%; variable range applies to Upgrades. |
| **xHoney From Tokens** | (Variable) | Variable, depends on Caustic/Non-Caustic status. |

The **Candy Ring** is a Level 14 Beequip with an equip limit of one. It has no color requirement and can be equipped by Stubborn, Bumble, Honey, Diamond, Festive, and Gummy bees.

## Stats Breakdown

### Base Stats (Random Generation)
| Stat | Caustic Req. | Base Value | Upgrades Chance/Value | Range / Notes |
| :--- | :--- | :--- | :--- | :--- |
| **+Energy** | 100% | Random value between +60 and +80 (Intervals of +0.01) | N/A | Bias scales linearly. |
| **+Convert Amount%** | 100% | Random value between +20% and +30% (Intervals of +1%) | N/A | Bias scales linearly. |
| **+Ability Rate%** | Caustic Points Only | Random value between +1% and +2% (Intervals of +1%) | N/A | Linear scaling by a factor of 1, Scaling power: 1.5. |
| **+Honey At Hive%** | 100% | Random value between +2% and +5% (Intervals of +1%) | N/A | Linear scaling by a factor of 1, Scaling power: 1.5. |
| **+Honey Per Goo%** | 100% | +1% | N/A | Linear scaling by a factor of 1, Scaling power: 1.5. |
| **xHoney From Tokens** | Caustic Points Only | N/A | Random value between 5e-05 and 0.0002 (Intervals of +0.01) | Linear scaling by a factor of 1, Scaling power: 1.5. |

### Upgraded Stats (Average Values from Data Samples)
*Note: The specific values vary based on the generation method (Caustic/Non-Caustic), but average trends are provided below.*

**Non-Caustic Average Trends:**
| Stat | Base Avg. | Upgrade Chance/Avg. | Limit |
| :--- | :--- | :--- | :--- |
| **+Energy** | ~67 | Random value between +6 and +8 (Avg: ~6.4) | 20 |
| **+Convert Amount%** | ~23% | N/A | 10 |
| **+Ability Rate%** | ~1.15% | N/A | - |
| **+Honey At Hive%** | ~2.7% | Random value between +1% and +2% (Avg: ~1.15%) | 10 |
| **+Honey Per Goo%** | ~1% | Average upgrade value varies significantly based on sample data (e.g., 0.4926%, 0.8787%). | 6 |

**Caustic Average Trends:**
| Stat | Base Avg. | Upgrade Chance/Avg. | Limit |
| :--- | :--- | :--- | :--- |
| **+Energy** | ~67 | Random value between +6 and +8 (Avg: ~6.4) | 20 |
| **+Convert Amount%** | ~23% | N/A | 10 |
| **+Ability Rate%** | ~1.15% | Average upgrade value varies significantly based on sample data (e.g., 8.9682%, 10.6679%). | 3 |
| **+Honey At Hive%** | ~2.7% | Random value between +1% and +2% (Avg: ~1.15%) | 10 |
| **+Honey Per Goo%** | ~1% | Average upgrade value varies significantly based on sample data (e.g., 0.6302%, 1.5617%). | 6 |

***Note:** The values shown may differ greatly from the real in-game potential, as players can only see a beequip's potential rounded to the nearest 1 ★ (or 0.5 ★ in Dapper Bear's Shop).*

## Probabilities
The following tables show the probability of a stat falling within a given range based on its star rating (Potential).

### +Energy Potential Probability
| Potential | +60–+64.99 | +65–+69.99 | +70–+74.99 | +75–+79.99 | +80 | Average Value |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **0 ★** | 59.623% | 25.017% | 11.929% | 3.431% | 0% | +65 |
| **0.5 ★** | 51.832% | 30.585% | 13.727% | 3.856% | 0% | +66 |
| **1 ★** | 38.794% | 40.607% | 16.198% | 4.401% | 0% | +67 |
| **1.5 ★** | 15.996% | 59.027% | 19.847% | 5.129% | 0% | +68 |
| **2 ★** | 10.263% | 57.61% | 25.979% | 6.149% | 1e-05% | +69 |
| **2.5 ★** | 7.654% | 42.131% | 42.526% | 7.689% | 1e-05% | +70 |
| **3 ★** | 6.122% | 25.916% | 57.65% | 10.312% | 1e-05% | +71 |
| **3.5 ★** | 5.106% | 19.807% | 59.0005% | 16.086% | 1e-05% | +72 |
| **4 ★** | 4.382% | 16.168% | 40.517% | 38.932% | 2e-05% | +73 |
| **4.5 ★** | 3.839% | 13.703% | 30.536% | 51.921% | 3e-05% | +74 |
| **5 ★** | 3.417% | 11.909% | 24.983% | 59.46% | 0.232% | +75 |

### +Convert Amount% Potential Probability
| Potential | +20%–+21% | +22%–+23% | +24%–+25% | +26%–+27% | +28%–+29% | +30% | Average Value |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **0 ★** | 43.457% | 28.287% | 16.137% | 8.695% | 3.297% | 0.127% | +22.5% |
| **0.5 ★** | 29.452% | 37.571% | 19.168% | 9.961% | 3.706% | 0.142% | +23% |
| **1 ★** | 8.069% | 52.041% | 23.824% | 11.674% | 4.232% | 0.16% | +23.5% |
| **1.5 ★** | 4.603% | 43.592% | 32.545% | 14.142% | 4.935% | 0.183% | +24% |
| **2 ★** | 3.25% | 21.353% | 51.192% | 18.07% | 5.921% | 0.214% | +24.5% |
| **2.5 ★** | 2.516% | 14.424% | 49.573% | 25.816% | 7.413% | 0.259% | +25% |
| **3 ★** | 2.054% | 11.059% | 29.462% | 47.137% | 9.961% | 0.326% | +25.5% |
| **3.5 ★** | 1.736% | 9.0038% | 21.153% | 52.065% | 15.599% | 0.442% | +26% |
| **4 ★** | 1.503% | 7.605% | 16.813% | 35.216% | 38.178% | 0.685% | +26.5% |
| **4.5 ★** | 1.326% | 6.588% | 14.03% | 26.18% | 50.342% | 1.534% | +27% |
| **5 ★** | 1.186% | 5.813% | 12.068% | 21.275% | 39.679% | 19.979% | +27.5% |

### +Ability Rate% Potential Probability
| Potential | +1% | +2% | Average Value |
| :--- | :--- | :--- | :--- |
| **0 ★** | 84.657% | 15.343% | +1.2% |
| **0.5 ★** | 82.437% | 17.563% | +1.2% |
| **1 ★** | 79.425% | 20.575% | +1.2% |
| **1.5 ★** | 75.055% | 24.945% | +1.2% |
| **2 ★** | 67.918% | 32.082% | +1.3% |
| **2.5 ★** | 50% | 50% | +1.5% |
| **3 ★** | 32.082% | 67.918% | +1.7% |
| **3.5 ★** | 24.945% | 75.055% | +1.8% |
| **4 ★** | 20.575% | 79.425% | +1.8% |
| **4.5 ★** | 17.563% | 82.437% | +1.8% |
| **5 ★** | 15.343% | 84.657% | +1.8% |

### +Honey At Hive% Potential Probability
| Potential | +2% | +3% | +4% | +5% | Average Value |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0 ★** | 46.529% | 38.128% | 13.869% | 1.473% | +2.7% |
| **0.5 ★** | 34.018% | 48.419% | 15.914% | 1.648% | +2.9% |
| **1 ★** | 10.694% | 68.731% | 18.704% | 1.871% | +3.1% |
| **1.5 ★** | 5.854% | 69.201% | 22.781% | 2.164% | +3.2% |
| **2 ★** | 4.09% | 63.828% | 29.517% | 2.565% | +3.3% |
| **2.5 ★** | 3.151% | 46.849% | 46.849% | 3.151% | +3.5% |
| **3 ★** | 2.565% | 29.517% | 63.828% | 4.09% | +3.7% |
| **3.5 ★** | 2.164% | 22.781% | 69.201% | 5.854% | +3.8% |
| **4 ★** | 1.871% | 18.704% | 68.731% | 10.694% | +3.9% |
| **4.5 ★** | 1.648% | 15.914% | 48.419% | 34.018% | +4.1% |
| **5 ★** | 1.473% | 13.869% | 38.128% | 46.529% | +4.3% |

## Acquisition Methods

The Candy Ring can be obtained through several methods:

*   Purchased from Dapper Bear's Beequip Shop.
*   Awarded as a reward from the Ant Challenge.
*   Awarded as a reward from the Robo Bear Challenge.
*   Dropped by Hydroponic Planters in various fields (Stump Field, Blue Flower Field, Sunflower Field, and Pine Tree Forest).
*   Dropped by Petal Planters.

### Outdated Methods
The Candy Ring was previously available as a reward for completing Gummy Bear's Beesmas Summer or Winter 2024 quests.