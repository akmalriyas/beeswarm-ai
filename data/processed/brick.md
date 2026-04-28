# Brick

![Digital Bee](https://static.wikia.nocookie.net/bee-swarm-simulator/images/2/27/Digital_Bee.png/revision/latest/scale-to-width-down/100?cb=20230415203844) | *Note: This content contains information obtained through datamining, and details may be inaccurate or outdated.*

Brick is the primary currency used within the Retro Swarm Challenge. It is required to purchase various utilities necessary for surviving waves of slimes and zombies during this challenge.

**Cooldown:** N/A

## Acquisition Methods

Bricks can be acquired through several methods:

*   Farming in the Red, Blue, White, and Mixed Brick Fields.
*   Destroying Brick Blooms (the amount obtained depends on the current level).
*   Slaying Slimes and Zombies (the amount obtained depends on the current level).
*   Purchasing from Honey Stalls:
    *   10 Bricks can be purchased for honey near the hives.
    *   100 Bricks can be purchased for honey on the left side of the monster's spawn area.

## Cost of Buying Bricks

The cost of purchasing a Brick increases based on how many bricks ($n$) have already been bought, following a complex formula:

$$\text{Cost}(n) = \left\lfloor n^{x(n+1)} \cdot y(n+1) \right\rfloor$$

Where $x(n)$ and $y(n)$ are defined by the following piecewise functions:

**$x(n)$ (Exponent Multiplier):**
$$x(n)=
\begin{cases}
1.2 & \text{if } n < 50 \\
1.5 & \text{if } 50 \leq n < 100 \\
1.75 & \text{if } 100 \leq n < 250 \\
2 & \text{if } n \geq 250
\end{cases}$$

**$y(n)$ (Base Multiplier):**
$$y(n)=
\begin{cases}
10 & \text{if } n < 1000 \\
20 & \text{if } 1000 \leq n < 2000 \\
30 & \text{if } 2000 \leq n < 5000 \\
40 & \text{if } n \geq 5000
\end{cases}$$

**Example Calculation:** If a player has already bought 110 bricks ($n=110$), the cost of the next brick is calculated as:
$$\text{Cost}(110) = \left\lfloor 111^{1.75} \cdot 10 \right\rfloor \approx 37,363 \text{ Honey}$$

### Deprecated Acquisition Methods

The following methods for obtaining Bricks are no longer possible:

*   Completing Bubble Bee Man's Naughty List during Summer Beesmas 2024 and Winter Beesmas 2024 rewarded 1 Brick.
*   Giving Bubble Bee Man a present during Summer Beesmas 2024 and Winter Beesmas 2024 rewarded 2 Bricks.

## Uses

Bricks serve as the main currency in the Retro Swarm Challenge, allowing players to purchase various items:

### Utilities (Boost Items)

| Item | Cost | Notes |
| :--- | :--- | :--- |
| Unlock A Bee | 5 Bricks | +10 after first purchase, +15 thereafter. |
| Level Up Rental Bees | 10 Bricks | +10 after first and third purchase, +20 otherwise. |
| Bloxiade | 100 Bricks | |
| Bloxy Cola | 200 Bricks | |
| Cheezburger | 300 Bricks | |
| Pizza | 500 Bricks | |

### Weapons

| Item | Cost |
| :--- | :--- |
| Classic Sword | 10 Bricks |
| Trowel | 25 Bricks |
| Slingshot | 150 Bricks |
| Firebrand | 300 Bricks |
| Rocket Launcher | 750 Bricks |
| Illumina | 1,500 Bricks |

## Trivia

*   Bricks can still be obtained outside of the Retro Swarm Challenge by giving Bubble Bee Man a present or by completing his Beesmas 2024 quest.
*   Some quests, such as Brown Bear's Stockings or BBM's Naughty List in Beesmas 2024, required players to collect these items.