# Sticker Seeker Quest Machine

![Digital Bee](https://static.wikia.nocookie.net/bee-swarm-simulator/images/2/27/Digital_Bee.png/revision/latest/scale-to-width-down/100?cb=20230415203844) | *Note: This content contains information obtained through datamining, and details may be inaccurate or outdated.*

> _This article describes the quest giver. For information on the tool, see [Sticker-Seeker]._

[![The Sticker Quest Giver and the Sticker-Seeker leaderboard.](https://static.wikia.nocookie.net/bee-swarm-simulator/images/d/df/StickerQuest_Giver.png/revision/latest/scale-to-width-down/209?cb=20240114231934)](https://static.wikia.nocookie.net/bee-swarm-simulator/images/d/df/StickerQuest_Giver.png/revision/latest?cb=20240114231934) [](/wiki/File:StickerQuest_Giver.png)

The **Sticker-Seeker Quest Machine** is a quest giver located in the Hive Hub. To interact with it, the player must own and have the Sticker-Seeker equipped, and they must possess at least 15 hatched bees.

Similar to Brown Bear, Polar Bear, Honey Bee (NPC), Gifted Riley Bee, and Gifted Bucko Bee, this machine provides infinite quests, offering extra rewards at specific milestones up to the 1000th quest.

## Ranks
A player's rank is determined by the total number of Sticker-Seeker Quest Machine quests they have completed. This rank dictates their position on the Top Sticker-Seekers leaderboard and increases with every quest completion. Higher ranks yield better rewards, such as a greater likelihood of receiving Sticker Planters compared to players at lower ranks (e.g., Rank 5). Quest requirements also scale based on the player's current rank.

## Quests
To obtain or turn in quests from this giver, the player must have the Sticker-Seeker equipped. The only quest available is **🔎 Sticker-Seeker: Rank X**, where *X* represents the player's current rank.

Every quest always includes two primary requirements:
1. Finding a specified number of [Seeker Stickers] hidden around the map.
2. Collecting pollen using the [Sticker-Seeker].

### Seeker Stickers Requirement
The requirement states: "_Find a number of Seeker Stickers Hidden in any number of bee zones, which can also include shops or HQ's._"

The game always generates two more Seeker Stickers than required to complete the quest. Furthermore, uncollected Seeker Sticker locations change every 2 days.

**Predetermined Locations (Ranks 1-26):**

| Rank | Requirements |
| :---: | :--- |
| **1** | Find 2 Seeker Stickers Hidden in the 5 Bee Zone. |
| **2** | Find 2 Seeker Stickers Hidden in the 10 Bee Zone. |
| **3** | Find 2 Seeker Stickers Hidden in the Starter Zone. |
| **4** | Find 2 Seeker Stickers Hidden in the 20 Bee Zone or the 5 Bee Zone. |
| **5** | Find 3 Seeker Stickers Hidden in the 10 Bee Zone or the Starter Zone. |
| **6** | Find 3 Seeker Stickers Hidden in the 5 Bee Zone or the 10 Bee Zone. |
| **7** | Find 3 Seeker Stickers Hidden in HQs. |
| **8** | Find 3 Seeker Stickers Hidden in the 5 Bee Zone or the 20 Bee Zone. |
| **9** | Find 3 Seeker Stickers Hidden in the Starter Zone or 10 Bee Zone. |
| **10** | Find 3 Seeker Stickers Hidden in Zones that require 10 Bees or less (Starter, 5 Bee Zone, 10 Bee Zone). |
| **11** | Find 4 Seeker Stickers Hidden in the 25 Bee Zone. |
| **12** | Find 4 Seeker Stickers Hidden in the 10 Bee Zone or the 15 Bee Zone. |
| **13** | Find 4 Seeker Stickers Hidden in Shops. |
| **14** | Find 4 Seeker Stickers Hidden in the 15 Bee Zone or the 20 Bee Zone. |
| **15** | Find 4 Seeker Stickers Hidden in Zones that require 15 Bees or less (Starter, 5 Bee Zone, 10 Bee Zone, 15 Bee Zone). |
| **16** | Find 4 Seeker Stickers Hidden in the Starter Zone or the 25 Bee Zone. |
| **17** | Find 4 Seeker Stickers Hidden in the 15 Bee Zone or HQs. |
| **18** | Find 4 Seeker Stickers Hidden in the 5 Bee Zone, the 10 Bee Zone, or the 25 Bee Zone. |
| **19** | Find 4 Seeker Stickers Hidden in the Starter Zone or the 20 Bee Zone. |
| **20** | Find 4 Seeker Stickers Hidden in Zones that require up to 20 Bees (Starter, 5 Bee Zone, 10 Bee Zone, 15 Bee Zone, 20 Bee Zone). |
| **21** | Find 5 Seeker Stickers Hidden in the 25 Bee Zone or the 30 Bee Zone. |
| **22** | Find 4 Seeker Stickers Hidden in Zones that require 15 Bees or less (Starter, 5 Bee Zone, 10 Bee Zone, 15 Bee Zone). |
| **23** | Find 4 Seeker Stickers Hidden in the 20 Bee Zone, the 25 Bee Zone, or HQs. |
| **24** | Find 5 Seeker Stickers Hidden in the Starter Zone. |
| **25** | Find 5 Seeker Stickers Hidden in the 5 Bee Zone or the 10 Bee Zone. |
| **26** | Find 5 Seeker Stickers Hidden in Zones that require up to 30 Bees (Starter, 5 Bee Zone, 10 Bee Zone, 15 Bee Zone, 20 Bee Zone, 25 Bee Zone, 30 Bee Zone). |

Past the 26th quest, requirements are randomly generated:
*   Find 5 Seeker Stickers (or 6 if the rank is $\ge 500$) hidden in [pick 3 zones from the following pool]: Starter Zone, 5 Bee Zone, 10 Bee Zone, 15 Bee Zone, 20 Bee Zone, 25 Bee Zone, Shops, HQs, 30 Bee Zone (Rank 40+), or 35 Bee Zone (Rank 80+).

### Pollen Requirement
The amount of pollen required is calculated using the formula:
$$P(X) = 100,000 + 99,900,000 \times \left(\frac{X-1}{499}\right)^{2.25} + 25,000 \times (X-1) + \Delta(X)$$
The final requirement is the value $P(X)$ floored to the nearest $S(P(X))$.

*   $X$: The quest's rank, or the player's rank plus 1.
*   $\frac{X-1}{499}$: Clamped between 0 and 1.
*   $\Delta(X)$:
    *   $0$ if $X \le 500$.
    *   $1,000,000 \times (X - 500)$ otherwise.
*   $S(P(X))$: The required amount of pollen based on the calculated value $P(X)$:
    *   $50,000$ if $P(X) \ge 1,000,000$.
    *   $25,000$ if $500,000 \le P(X) < 1,000,000$.
    *   $10,000$ if $100,000 \le P(X) < 500,000$.
    *   $5,000$ if $25,000 \le P(X) < 100,000$.
    *   $1,000$ if $P(X) < 25,000$.

### Other Requirements
The remaining requirements are randomly selected from a pool. The number of extra requirements starts at 1, increases to 2 at quest 100, and finally to 3 at quest 250. A requirement cannot appear in two consecutive quests.

Requirements are chosen by weighting: all possible requirements that meet the minimum rank and have not appeared recently are added to a pool. Each is given a weight, and selection probability equals its weight divided by the sum of all weights in the pool. The selected requirement is then removed from the pool until the required limit is reached.

**Possible Requirements Pool:**
| Requirement | Minimum Rank | Weight (Ranks 1-149) | Weight (Ranks 150+) |
| :--- | :---: | :---: | :---: |
| Collect 6 or 20 Stickers (without Trading). | 0 | 7 | 7 |
| Donate 1 or 7 Stickers to the Public Sticker Board. | 0 | 10 | 10 |
| Collect 3 or 12 Rainbow [Sticker Tokens]. | 0 | 6 | 6 |
| Collect 1 or 3 Stickers from Sprouts. | 8 | 3 | 3 |
| Find 7 or 8 Hidden Stickers on Surfaces around the Map. | 10 | 8 | 8 |
| Collect 1 or 5 Stickers spawned by your Tool while Gathering. | 10 | 6 | 6 |
| Collect a Sticker from Leaves. | 15 | 6 | 6 |
| Collect 1 or 3 Stickers found by your Bees while Gathering. | 20 | 5 | 5 |
| Print 1 or 3 Stickers with the Sticker Printer. | 25 | 7 | 7 |
| Collect 1 or 2 Stickers from Puffshrooms. | 30 | 4 | 4 |
| Collect a Sticker from Wild Windy Bee. | 35 | 4 | 4 |
| Discard 5 or 25 Stickers. | 40 | 10 | 10 |
| Collect 1 or 3 Stickers from Planters. | 45 | 3 | 3 |
| Collect a Sticker from Fireflies. | 50 | 4 | 4 |
| Collect a Sticker from the Public Sticker Board. | 100 | 4 | 4 |

**Bonus Requirement:** Every 10th quest includes an extra requirement: Add $\lfloor \frac{X+1}{2} \rfloor$ Stickers to the Sticker Stack.

## Rewards
Every quest reward always includes (assuming $X$ is the quest's rank, clamped between 1 and 100,000):

*   $\left\lfloor \frac{P(X) \times 2}{50,000} \right\rfloor \times 50,000$ [Honey], where $P(X)$ is the amount of pollen collected to finish the quest.
*   $\min\left(1+\left\lfloor \frac{X}{100}\right\rfloor, 5\right)$ [Tickets].
*   $\max\left(\left\lfloor \frac{X}{4}\right\rfloor, 1\right)$ [Royal Jellies].
*   One of: Soft Wax, Neonberry, Micro-Converter, Field Dice, or Whirligigs.
*   A random Sticker.

**Sticker Planter Probability:**
In addition to guaranteed rewards from milestones, there is a chance to receive a Sticker Planter from the quest. This probability increases quadratically from rank 1 to 500, maxing out at 5%. The formula for this probability is:
$$2\% + 3\% \times \left(\frac{X-1}{499}\right)^2$$

### Sticker Reward Calculation
The sticker reward is determined by a weighted random selection process. All attainable stickers are added to a pool, but they are removed if:
*   The player has not met the sticker's minimum quest rank requirement.
*   The sticker is guaranteed via a milestone.
*   The sticker cannot be obtained due to the player's spread ID restrictions.

Each remaining sticker is assigned a true weight using the formula:
$$\text{weight} = \text{leftBound} + (\text{rightBound} - \text{leftBound}) \times \min\left(\frac{X-1}{499}, 1\right)$$
The probability of receiving any sticker is its true weight divided by the sum of all true weights in the pool.

**Sticker Weight Bounds:**
| Sticker | Minimum Rank | Lower Bound | Upper Bound |
| :--- | :---: | :---: | :---: |
| Yellow Umbrella | 0 | 1 | 0.25 |
| Green Check Mark | 0 | 0.6 | 0.3 |
| Green Plus Sign | 0 | 0.6 | 0.3 |
| Yellow Left/Right Arrow | 0 | 1.5 | 1 |
| Thumbs Up/Peace Sign Hand | 5 | 1.5 | 1 |
| Simple Cloud | 10 | 1 | 0.5 |
| Tough Potato | 10 | 0.4 | 0.4 |
| Standing Bean Bug | 10 | 0.02 | 0.02 |
| Coiled Snake | 15 | 0.2 | 0.2 |
| Pink Chair | 15 | 0.1 | 0.1 |
| Nessie | 18 | 0.001 | 0.001 |
| Lightning | 20 | 1 | 0.5 |
| Grey Diamond Logo | 20 | 0.2 | 0.2 |
| Basic Red Hive Skin | 20 | 0.03 | 0.03 |
| Basic Blue Hive Skin | 20 | 0.03 | 0.03 |
| Blue/Orange/Yellow Marble | 25 | 0.1 | 0.2 |
| Doodle S | 30 | 0.4 | 0.4 |
| 4-Pronged Vector Bee | 30 | 0.02 | 0.02 |
| Taunting Doodle Person | 35 | 0.02 | 0.02 |
| Orange/Green Tri Deco | 40 | 0.1 | 0.2 |
| Squashed Head Bear | 40 | 0.02 | 0.02 |
| Stretched Head Bear | 40 | 0.02 | 0.02 |
| Shining Halo | 50 | 0.1 | 0.1 |
| Wall Crack | 50 | 0.02 | 0.02 |
| Auryn | 50 | 0.005 | 0.005 |
| Black Star | 70 | 0.02 | 0.02 |
| Prism/Banana Painting | 75 | 0.1 | 0.1 |
| Prehistoric Hand/Boar | 80 | 0.02 | 0.02 |
| Basic Pink Hive Skin | 80 | 0.015 | 0.015 |
| Basic Green Hive Skin | 80 | 0.015 | 0.015 |
| Abstract Color Painting | 90 | 0.02 | 0.02 |
| Ionic Column Middle | 100 | 0.3 | 0.3 |
| Ionic Column Top/Base | 100 | 0.2 | 0.2 |
| Dapper From Above | 100 | 0.005 | 0.005 |
| Pearl Girl | 150 | 0.02 | 0.02 |
| Royal Bear | 160 | 0.02 | 0.02 |
| Basic White Hive Skin | 200 | 0.007 | 0.007 |
| Basic Black Hive Skin | 200 | 0.007 | 0.007 |

**Milestones:**
Quest milestones provide extra rewards:

| Rank | Reward |
| :---: | :--- |
| 10 | Pink Balloon |
| 25 | Silver Egg |
| 50 | Gold Egg |
| 75 | Diamond Egg |
| 100 | Gifted Silver Egg |
| 110 | Red Balloon |
| 150 | Gifted Gold Egg |
| 200 | Gifted Diamond Egg |
| 210 | White Balloon |
| 300 | Mythic Egg |
| 310 | Black Balloon |
| 400 | Star Egg |
| 410 | 3 Pink Balloons |
| 500 | Gifted Mythic Egg |
| 510 | 3 White Balloons |
| 600 | 3 Gifted Silver Eggs |
| 610 | 3 White Balloons |
| 700 | 3 Gifted Gold Eggs |
| 800 | 3 Gifted Diamond Eggs |
| 900 | 3 Mythic Eggs |
| 1000 | 3 Gifted Mythic Eggs |

**Sticker Planter Milestones:**
| Rank | Amount |
| :---: | :---: |
| 11, 33, 55, 77, 99, 111, 133, 144, 155, 166, 199, 244, 255, 266, 277 | 1 Sticker Planter |
| 222, 422 | 2 Sticker Planters |
| 333 | 3 Sticker Planters |
| 444 | 4 Sticker Planters |
| 555 | 5 Sticker Planters |

**Specific Rank Rewards:**
*   Rank 20: Doodle S Sticker OR Tough Potato Sticker
*   Rank 40: Orange Swirled Marble Sticker, Yellow Swirled Marble Sticker OR Blue And Green Marble Sticker
*   Rank 60: Coiled Snake Sticker OR Grey Diamond Logo Sticker
*   Rank 90: Orange Step Array Sticker OR Orange Green Tri Deco Sticker
*   Rank 120: Ionic Column Top Sticker OR Ionic Column Base Sticker
*   Rank 140: Prism Painting Sticker OR Banana Painting Sticker
*   Rank 180: Prehistoric Hand Sticker OR Prehistoric Boar Sticker
*   Rank 220: Ionic Column Middle Sticker
*   Rank 250: Ticket Voucher
*   Rank 350: Basic Green Hive Skin OR Basic Pink Hive Skin
*   Rank 450: Basic White Hive Skin OR Basic Black Hive Skin

## Trivia
*   It is the only Quest Giver that lacks dialogue and does not send a notification to talk to the machine again after quest completion.
*   The Sticker Quest Giver is the fourth randomized Quest Giver to grant eggs at certain milestones, alongside Gifted Riley Bee, Gifted Bucko Bee, and Brown Bear.
*   All quests given by this giver always include the requirements: "Collect {amount} of Pollen using [Sticker-Seeker]," and "Find 2-7 Seeker-Stickers hidden in {zones}."
*   The difficulty of the quests was originally intended to scale linearly with player rank up to Rank 150, but due to an oversight, the difficulty remained constant until Rank 150 before increasing sharply.