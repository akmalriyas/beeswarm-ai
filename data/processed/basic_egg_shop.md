# Basic Egg Shop

![Egg Shop](https://static.wikia.nocookie.net/bee-swarm-simulator/images/9/9b/Egg_Shop.png/revision/latest/scale-to-width-down/267?cb=20180604172559) The Basic Egg Shop

The **Basic Egg Shop** is a shop located next to the Sunflower Field and behind an Instant Converter. It sells Basic Eggs, which are used for obtaining Hive Slots.

## Usage & Requirements

*   **Obtains:** Hive Slots
*   **Input Item:** Basic Eggs
*   **Requirement(s):** Honey (Cost varies based on egg number)
*   **Cooldown:** None
*   **Location:** Between the Sunflower Field and the Dandelion Field

The shop sells Basic Eggs for increasing amounts of honey. The cost starts at 1,000 honey and increases exponentially, eventually capping off at 10,000,000 honey for the 22nd egg and beyond.

## Pricing Table (Honey Cost)

| Egg Number | Honey Cost |
| :---: | :---: |
| 1 | 1,000 |
| 2 | 2,500 |
| 3 | 4,250 |
| 4 | 6,708 |
| 5 | 10,313 |
| 6 | 15,669 |
| 7 | 23,670 |
| 8 | 35,648 |
| 9 | 53,596 |
| 10 | 80,506 |
| 11 | 120,858 |
| 12 | 181,378 |
| 13 | 272,151 |
| 14 | 408,304 |
| 15 | 612,527 |
| 16 | 918,857 |
| 17 | 1,378,348 |
| 18 | 2,067,580 |
| 19 | 3,101,426 |
| 20 | 4,652,191 |
| 21 | 6,978,337 |
| 22+ | 10,000,000 |

## Cost Formula Mechanics

The cost of egg number N is calculated using the following iterative formula:

*   **Base:** 1000
*   **Initial State:** `cost = base`, `i = 0`
*   **Iteration:** While $i < N-1$:
    $$ \text{cost} = (1.5 \times \text{cost}) + (\text{base} / (i+1)) $$
    $$ i = i + 1 $$

*(Note: The price progression is roughly exponential, but does not follow a simple closed-form equation.)*

## Trivia

*   The Basic Egg Shop and stacking the Round Basic Bee sticker are the only ways to obtain a Basic Egg, besides the one given to the player at the start of the game.
*   Like other machine lookalikes in the game, the model of this shop is a modified version of the Gumball Machine model by @wonderful72pike.