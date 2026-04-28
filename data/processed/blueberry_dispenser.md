# Blueberry Dispenser

The Blueberry Dispenser is a specialized dispenser found within the Blue HQ area of Bee Swarm Simulator. It is one of several dispensers that provide various treats to players, including the Honey Dispenser and Strawberry Dispenser.

## Information

### Location & Usage
*   **Location:** First floor of the Blue HQ, located next to the Blue Teleporter.
*   **Requirement:** Access to the Blue HQ and membership in the Bee Swarm Simulator Club.
*   **Cooldown:** 4 hours.

When activated, the dispenser grants the player a set amount of Honey, Haste Tokens, Blue Boost Tokens, and Blueberries based on the number of Blue bees currently in the player's hive. If the player has no blue bees in their hive, it will not grant any blueberries.

**Standard Grants:**
*   Haste: x5
*   Blue Boost Tokens: x10
*   Blueberries: Equal to the count of Blue bees in the hive.

### Reward Calculation (Honey and Blueberries)

The amount of honey received is calculated based on the number of Blue bees ($\text{cnt}$) in the player's hive using the following formula:

$$\text{Honey} = \max\left(500, \left\lfloor {\text{cnt}}^{1.5}+0.5\right\rfloor \times 200\right)$$

The amount of blueberries received is simply equal to the number of Blue bees ($\text{cnt}$).

**Reward Table (Honey per Bee Count):**

| Bees ($\text{cnt}$) | Honey Received | Bees ($\text{cnt}$) | Honey Received |
| :---: | :---: | :---: | :---: |
| 0-1 | 500 | 26 | 26,600 |
| 2 | 600 | 27 | 28,000 |
| 3 | 1,000 | 28 | 29,600 |
| 4 | 1,600 | 29 | 31,200 |
| 5 | 2,200 | 30 | 32,800 |
| 6 | 3,000 | 31 | 34,600 |
| 7 | 3,800 | 32 | 36,200 |
| 8 | 4,600 | 33 | 38,000 |
| 9 | 5,400 | 34 | 39,600 |
| 10 | 6,400 | 35 | 41,400 |
| 11 | 7,200 | 36 | 43,200 |
| 12 | 8,400 | 37 | 45,000 |
| 13 | 9,400 | 38 | 46,800 |
| 14 | 10,400 | 39 | 48,800 |
| 15 | 11,600 | 40 | 50,600 |
| 16 | 12,800 | 41 | 52,600 |
| 17 | 14,000 | 42 | 54,400 |
| 18 | 15,200 | 43 | 56,400 |
| 19 | 16,600 | 44 | 58,400 |
| 20 | 17,800 | 45 | 60,400 |
| 21 | 19,200 | 46 | 62,400 |
| 22 | 20,600 | 47 | 64,400 |
| 23 | 22,000 | 48 | 66,600 |
| 24 | 23,600 | 49 | 68,600 |
| 25 | 25,000 | 50 | 70,800 |

## Trivia
*   Prior to the November 25, 2018 update, the Blueberry Dispenser was located where the Gifted Bucko Bee used to be. It was subsequently moved to accommodate the NPC.
*   This dispenser appears in a quest only within Science Bear's "The Power of Information."
*   It provides the same amount of honey per bee as the Strawberry Dispenser.
*   Along with the Treat Dispenser and Strawberry Dispenser, this is one of three dispensers that grant treats in the game.
*   This dispenser is part of a group of four machines that require players to be members of the Bee Swarm Simulator Club (alongside the Honey Dispenser, Treat Dispenser, and Strawberry Dispenser).