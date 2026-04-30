# Whistle

The **Whistle** is a Level 8 Beequip with an equip limit of one and no color requirement. It can be equipped by Brave Bee, Commander Bee, Rascal Bee, Demo Bee, Cool Bee, and Rage Bee. The item description states: "Bees can blow into this to startle everyone around them."

## Stats and Potential

The Whistle provides the following base stats and abilities:
*   **General:** +Movespeed%, +Critical Power%, -Energy%
*   **Abilities:** Haste, Melody
*   **Hive Bonus:** xPlayer Movespeed, +Bee Movespeed%, +Super-Crit Power%

### Base Stat Generation (Non-Caustic)

| Stat | Caustic Req. | Base Chance | Upgrades Chance | Range/Value | Limit | Notes |
| :--- | :---: | :---: | :---: | :--- | :---: | :--- |
| **+Movespeed%** | 100% | Random (+5% to +10%) | Random (+1% to +2%) | Intervals of +1%; Bias scales linearly | 15 | Average Base: +6.22%; Average Upgrade: +1.25% |
| **+Critical Power%** | 100% | Random (+15% to +25%) | Random (+2% to +3%) | Intervals of +1%; Bias scales linearly | 20 | Average Base: +17.48%; Average Upgrade: +2.15% |
| **-Energy%** | 100% | Random (-55% to -45%) | N/A | Intervals of +1%; Biased near -55% | N/A | Average Base: -52.52% |

### Caustic Stat Generation (Examples)

The following tables show examples of stat generation based on different levels of Caustic Wax investment, demonstrating how the probabilities shift with upgrades.

**Example 1:**
| Stat | Caustic Req. | Base Chance | Upgrades Chance | Range/Value | Limit | Notes |
| :--- | :---: | :---: | :---: | :--- | :---: | :--- |
| **+Movespeed%** | 100% | Random (+5% to +10%) | Random (+1% to +2%) | Intervals of +1%; Biased near +5% | 15 | Average Base: +6.22%; Average Upgrade: +1.25% |
| **+Critical Power%** | 100% | Random (+15% to +25%) | Random (+2% to +3%) | Intervals of +1%; Biased near +15% | 20 | Average Base: +17.48%; Average Upgrade: +2.15% |
| **-Energy%** | 100% | Random (-55% to -45%) | N/A | Intervals of +1%; Biased near -55% | N/A | Average Base: -52.52% |

**Example 2 (Higher Caustic):**
| Stat | Caustic Req. | Base Chance | Upgrades Chance | Range/Value | Limit | Notes |
| :--- | :---: | :---: | :---: | :--- | :---: | :--- |
| **+Movespeed%** | 100% | Random (+5% to +10%) | Random (+1% to +2%) | Intervals of +1%; Biased near +6% | 15 | Average Base: +6.74%; Average Upgrade: +1.35% |
| **+Critical Power%** | 100% | Random (+15% to +25%) | Random (+2% to +3%) | Intervals of +1%; Biased near +17% | 20 | Average Base: +18.49%; Average Upgrade: +2.21% |
| **-Energy%** | 100% | Random (-55% to -45%) | N/A | Intervals of +1%; Biased near -53% | N/A | Average Base: -52.01% |

*(Note: The original wiki contained multiple tables showing varying Caustic investment results; these examples illustrate the data structure.)*

## Probabilities (Potential)

The following tables detail the probability of a Whistle's stats falling within specific ranges based on its potential rating (★).

### Movespeed Potential
| Potential | +5% Range | +6% Range | +7% Range | +8% Range | +9% Range | +10% Range | Average |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0 ★** | 33.026% | 33.093% | 18.538% | 10.31% | 4.515% | 0.518% | +6.2% |
| **1 ★** | 3.069% | 47.726% | 28.63% | 14.075% | 5.847% | 0.653% | +6.7% |
| **3 ★** | 0.884% | 8.322% | 22.877% | 51.781% | 14.768% | 1.37% | +7.8% |

### Critical Power Potential
| Potential | +15%-+16% Range | +17%-+18% Range | +19%-+20% Range | +21%-+22% Range | +23%-+24% Range | +25% Range | Average |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0 ★** | 43.457% | 28.287% | 16.137% | 8.695% | 3.297% | 0.127% | +17.5% |
| **1 ★** | 8.069% | 52.041% | 23.824% | 11.674% | 4.232% | 0.16% | +18.5% |
| **3 ★** | 2.054% | 11.059% | 29.462% | 47.137% | 9.961% | 0.326% | +20.5% |

### Energy Potential
| Potential | -55%--54% Range | -53%--52% Range | -51%--50% Range | -49%--48% Range | -47%--46% Range | -45% Range | Average |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0 ★** | 43.457% | 28.287% | 16.137% | 8.695% | 3.297% | 0.127% | -52.5% |
| **1 ★** | 8.069% | 52.041% | 23.824% | 11.674% | 4.232% | 0.16% | -51.5% |
| **3 ★** | 2.054% | 11.059% | 29.462% | 47.137% | 9.961% | 0.326% | -49.5% |

### Bee Stats Potential (Hive Bonuses)
| Potential | +1%-+1.2% Range | +1.2%-+1.4% Range | +1.4%-+1.6% Range | +1.6%-+1.8% Range | +1.8%-+2% Range | Average |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0 ★** | 52.189% | 24.463% | 13.998% | 7.202% | 2.149% | +1.2% |
| **1 ★** | 20% | 47.726% | 20% | 9.535% | 2.739% | +1.3% |
| **3 ★** | 3.781% | 14.246% | 41.972% | 33.863% | 6.137% | +1.6% |

### Super-Crit Power Potential
| Potential | +1% Range | +2% Range | Average |
| :---: | :---: | :---: | :---: |
| **0 ★** | 84.657% | 15.343% | +1.2% |
| **1 ★** | 79.425% | 20.575% | +1.2% |
| **3 ★** | 32.082% | 67.918% | +1.7% |

## Acquisition Methods

The Whistle can be obtained in several ways:
*   Purchased in Dapper Bear's Shop.
*   As an exceptionally rare drop from harvesting the Plastic Planter.
*   As a very rare drop from harvesting the Pesticide Planter.
*   As a very rare drop from harvesting The Planter Of Plenty.
*   As a reward from the Robo Bear Challenge.

## Trivia

The Whistle is one of eight Beequips designed to provide a negative stat. The other seven are: Kazoo, Beesmas Top, Toy Horn, Toy Drum, Pink Eraser, Demon Talisman, and Lump Of Coal.