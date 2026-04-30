# Basic Egg Shop

![Egg Shop](https://static.wikia.nocookie.net/bee-swarm-simulator/images/9/9b/Egg_Shop.png/revision/latest/scale-to-width-down/267?cb=20180604172559) The Basic Egg Shop

The Basic Egg Shop is a shop located next to the Sunflower Field and behind an Instant Converter. It sells Basic Eggs, which are used for obtaining Hive Slots.

## Information

### Location
The shop is situated between the Sunflower Field and the Dandelion Field.

### Requirements & Mechanics
*   **Item Sold:** Basic Eggs (used to obtain Hive Slots).
*   **Cost:** Honey (varies based on quantity).
*   **Cooldown:** None.

The cost of Basic Eggs begins at 1,000 honey and increases exponentially. This price increase eventually caps out at 10,000,000 honey for the 22nd egg and beyond.

### Price Chart (Honey Cost)

| Quantity | Honey Cost |
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

## Pricing Formula

The cost of egg number N is calculated using the following iterative formula:

*   **Base Cost:** 1,000 honey.
*   **Formula:**
    ```
    base = 1000
    cost = base
    i = 0
    while i < N-1 do
        cost = 1.5 * cost + base / (i+1)
        i = i + 1
    end
    ```

*Note: While the formula results in an exponential growth pattern, it does not follow a simple mathematical exponential function.*

## Trivia

*   The Basic Egg Shop and stacking Round Basic Bee stickers are currently the only ways to obtain a Basic Egg (aside from the one given to the player at the start of the game).
*   The model used for the machine is a modified version of the Gumball Machine model by @wonderful72pike.