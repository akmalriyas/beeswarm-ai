# Sweatband

The **Sweatband** is a Level 5 Beequip with an equip limit of three and no color requirement. It provides the following base bonuses:

*   +Energy%
*   +Red Gather Amount%
*   +White Gather Amount%
*   +Blue Gather Amount%
*   +Red Pollen%
*   +White Pollen%
*   +Blue Pollen%
*   +Max Bee Energy%
*   +Pollen%

> "This absorbant strap keeps sweat out of your eyes while looking vaguely patriotic."

## Stats and Potential

The Sweatband's stats are generated randomly, depending on whether it is a Base (Non-Caustic) or Caustic version. The tables below detail the potential ranges for various stat combinations.

### Base/Non-Caustic Potential
| Stat | Caustic Req. | Base Chance | Base Value | Upgrades Chance | Upgrade Value | Limit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **+Energy%** | 100% | A random value between +15% - +20% (Intervals of +1%) | 0.5 | A random value between +1% - +3% (Intervals of +1%) | 20 | +15% - +80% |
| **+Red Gather Amount%** | N/A | An exact value between 40% - 60% (Linear scaling by a factor of 1) | 0.15 | A random value between +1% - +2% (Intervals of +1%) | 20 | 0% - +60% |
| **+White Gather Amount%** | N/A | An exact value between 40% - 60% (Linear scaling by a factor of 1) | 0.15 | A random value between +1% - +2% (Intervals of +1%) | 20 | 0% - +60% |
| **+Blue Gather Amount%** | N/A | An exact value between 40% - 60% (Linear scaling by a factor of 1) | 0.15 | A random value between +1% - +2% (Intervals of +1%) | 20 | 0% - +60% |
| **+Red Pollen%** | Hive Bonus | An exact value between 5% - 25% (Linear scaling by a factor of 1) | +1% | An exact value between 0.0002 - 0.01 (Linear scaling by a factor of 1, Scaling power: 1.5) | +1% | 0% - +2% |
| **+White Pollen%** | Hive Bonus | An exact value between 5% - 25% (Linear scaling by a factor of 1) | +1% | An exact value between 0.0001 - 0.01 (Linear scaling by a factor of 1, Scaling power: 1.5) | +1% | 0% - +2% |
| **+Blue Pollen%** | Hive Bonus | An exact value between 5% - 25% (Linear scaling by a factor of 1) | +1% | An exact value between 0.0001 - 0.01 (Linear scaling by a factor of 1, Scaling power: 1.5) | +1% | 0% - +2% |
| **+Max Bee Energy%** | N/A | — | — | An exact value between 0.0001 - 0.02 (Linear scaling by a factor of 1) | +1% | 0% - +5% |
| **+Pollen% / Caustic Points Only** | N/A | — | — | An exact value between 0.0001 - 0.001 (Linear scaling by a factor of 1, Scaling power: 1.5) | +1% | 0% - +1% |

### Caustic Potential
| Stat | Caustic Req. | Base Chance | Base Value | Upgrades Chance | Upgrade Value | Limit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **+Energy%** | 100% | A random value between +15% - +20% (Intervals of +1%) | Biased to values near +15% (Average: +16.22%) | A random value between +1% - +3% (Intervals of +1%) | Biased to values near +1% (Average: +1.5%) | 20 |
| **+Red Gather Amount%** | N/A | **40%** | A random value between +15% - +20% (Intervals of +1%) | Biased to values near +15% (Average: +16.22%) | A random value between +1% - +2% (Intervals of +1%) | 20 |
| **+White Gather Amount%** | N/A | **40%** | A random value between +15% - +20% (Intervals of +1%) | Biased to values near +15% (Average: +16.22%) | A random value between +1% - +2% (Intervals of +1%) | 20 |
| **+Blue Gather Amount%** | N/A | **40%** | A random value between +15% - +20% (Intervals of +1%) | Biased to values near +15% (Average: +16.22%) | A random value between +1% - +2% (Intervals of +1%) | 20 |
| **+Red Pollen%** | Hive Bonus | **5%** | **+1%** | **0.021%** | **+1%** | **1** |
| **+White Pollen%** | Hive Bonus | **5%** | **+1%** | **0.0105%** | **+1%** | **1** |
| **+Blue Pollen%** | Hive Bonus | **5%** | **+1%** | **0.0105%** | **+1%** | **1** |
| **+Max Bee Energy%** | N/A | — | — | **0.0105%** | **+1%** | **5** |

*(Note: Multiple tables exist in the source data showing different RNG averages for various potential tiers (e.g., 0★, 2★, 5★). These represent specific statistical models and are retained as separate blocks of data.)*

### Probability Tables
The following tables show the probability of a stat falling within a given range or being upgraded within a given range by a wax point.

**Potential | Stat Ranges (Base) | Average Energy%**
| 0 ★ | 33.026% (+15%) | 33.093% (+16%) | 18.538% (+17%) | 10.31% (+18%) | 4.515% (+19%) | 0.518% (+20%) | +16.2% |
| 0.5 ★ | 10% (+15%) | 50.082% (+16%) | 22.356% (+17%) | 11.891% (+18%) | 5.095% (+19%) | 0.577% (+20%) | +16.5% |
| 1 ★ | 3.069% (+15%) | 47.726% (+16%) | 28.63% (+17%) | 14.075% (+18%) | 5.847% (+19%) | 0.653% (+20%) | +16.7% |
| 1.5 ★ | 1.891% (+15%) | 28.109% (+16%) | 45.055% (+17%) | 17.329% (+18%) | 6.864% (+19%) | 0.751% (+20%) | +17% |
| 2 ★ | 1.37% (+15%) | 14.768% (+16%) | 51.781% (+17%) | 22.877% (+18%) | 8.322% (+19%) | 0.884% (+20%) | +17.2% |
| 2.5 ★ | 1.074% (+15%) | 10.6% (+16%) | 38.326% (+17%) | 38.326% (+18%) | 10.6% (+19%) | 1.074% (+20%) | +17.5% |
| 3 ★ | 0.884% (+15%) | 8.322% (+16%) | 22.877% (+17%) | 51.781% (+18%) | 14.768% (+19%) | 1.37% (+20%) | +17.8% |
| 3.5 ★ | 0.751% (+15%) | 6.864% (+16%) | 17.329% (+17%) | 45.055% (+18%) | 28.109% (+19%) | 1.891% (+20%) | +18% |
| 4 ★ | 0.653% (+15%) | 5.847% (+16%) | 14.075% (+17%) | 28.63% (+18%) | 47.726% (+19%) | 3.069% (+20%) | +18.3% |
| 4.5 ★ | 0.577% (+15%) | 5.095% (+16%) | 11.891% (+17%) | 22.356% (+18%) | 50.082% (+19%) | 10% (+20%) | +18.5% |
| 5 ★ | 0.518% (+15%) | 4.515% (+16%) | 10.31% (+17%) | 18.538% (+18%) | 33.093% (+19%) | 33.026% (+20%) | +18.8% |

**Potential | Stat Ranges (Upgrade) | Average Energy%**
| 0 ★ | 59.657% (+1%-+1.5%) | 25% (+1.5%-+2%) | 11.919% (+2%-+2.5%) | 3.424% (+2.5%-+3%) | +1.5% |
| 0.5 ★ | 51.876% (+1%-+1.5%) | 30.561% (+1.5%-+2%) | 13.715% (+2%-+2.5%) | 3.848% (+2.5%-+3%) | +1.6% |
| 1 ★ | 38.863% (+1%-+1.5%) | 40.562% (+1.5%-+2%) | 16.183% (+2%-+2.5%) | 4.392% (+2.5%-+3%) | +1.7% |
| 1.5 ★ | 16.041% (+1%-+1.5%) | 59.014% (+1.5%-+2%) | 19.827% (+2%-+2.5%) | 5.118% (+2.5%-+3%) | +1.8% |
| 2 ★ | 10.288% (+1%-+1.5%) | 57.63% (+1.5%-+2%) | 25.947% (+2%-+2.5%) | 6.135% (+2.5%-+3%) | +1.9% |
| 2.5 ★ | 7.671% (+1%-+1.5%) | 42.329% (+1.5%-+2%) | 42.329% (+2%-+2.5%) | 7.671% (+2.5%-+3%) | +2% |
| 3 ★ | 6.135% (+1%-+1.5%) | 25.947% (+1.5%-+2%) | 57.63% (+2%-+2.5%) | 10.288% (+2.5%-+3%) | +2.1% |
| 3.5 ★ | 5.118% (+1%-+1.5%) | 19.827% (+1.5%-+2%) | 59.014% (+2%-+2.5%) | 16.041% (+2.5%-+3%) | +2.2% |
| 4 ★ | 4.392% (+1%-+1.5%) | 16.183% (+1.5%-+2%) | 40.562% (+2%-+2.5%) | 38.863% (+2.5%-+3%) | +2.3% |
| 4.5 ★ | 3.848% (+1%-+1.5%) | 13.715% (+1.5%-+2%) | 30.561% (+2%-+2.5%) | 51.876% (+2.5%-+3%) | +2.4% |
| 5 ★ | 3.424% (+1%-+1.5%) | 11.919% (+1.5%-+2%) | 25% (+2%-+2.5%) | 59.657% (+2.5%-+3%) | +2.5% |

## Ways to Obtain
The Sweatband can be acquired through several methods:

*   **Harvesting:** It is a very rare drop from harvesting the Tacky Planter, Candy Planter, and Petal Planter. (Tacky Planter and Petal Planter have a higher chance of dropping it in Clover Field.)
*   **Purchase:** Buying it from Dapper Bear's Shop.
*   **Quest Reward:** Completing Robo Bear's Winter 2025 Beesmas quest grants one Sweatband, along with other items.

## Gallery
![A Sweatband in Dapper Bear's Shop next to a Bandage and a Paperclip.](https://static.wikia.nocookie.net/bee-swarm-simulator/images/7/76/Sweatband1.png/revision/latest/scale-to-width-down/185?cb=20230516233746)
*A Sweatband in Dapper Bear's Shop next to a Bandage and a Paperclip.*

![A Sweatband equipped to a Shy Bee.](https://static.wikia.nocookie.net/bee-swarm-simulator/images/9/93/Sweatband2.png/revision/latest/scale-to-width-down/185?cb=20230516233747)
*A Sweatband equipped to a Shy Bee.*

![A glitched Sweatband.](https://static.wikia.nocookie.net/bee-swarm-simulator/images/7/75/GlitchedSweatband.png/revision/latest/scale-to-width-down/93?cb=20241229184726)
*A glitched Sweatband.*

## Trivia
*   It was one of the first beequips added that could be obtained outside of Beesmas events.
*   This Beequip was released during the 2022-04-01 update.
*   Currently, it is one of the few non-event Beequips whose stats do not provide an extra ability token.