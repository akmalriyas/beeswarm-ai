# Bee Leveling System

Bond is the core leveling mechanic in Bee Swarm Simulator, similar to progression systems found in other games. When bees achieve a high bond with the player, they level up and gain significant statistical boosts per level above 1:

*   **+5% Gather Amount:** Increases pollen collection efficiency.
*   **+10% Conversion Amount:** Improves production rates (e.g., honey/pollen conversion).
*   **+5% Energy:** Boosts bee energy reserves.
*   **+3% Movespeed:** Increases the speed at which bees travel.

### Bond Mechanics and Progression

Bond can be checked anytime by clicking on a bee's hive slot, where its current bond level and stats are displayed.

**Gaining Bond:**
1.  **Pollen Collection:** Bees automatically gain bond when collecting pollen in fields. Each bee type has an opinion of every field (likes, neutral, or dislikes).
    *   If a bee displays a happy emoticon over its head, it likes the field and gains extra bond.
    *   If it displays a sad emoticon, it dislikes the field and gains only minimal bond.
    *   If there is no emoticon, the bee is neutral and gains the standard amount of bond.
2.  **Treats:** Bees can be fed treats to increase their bond by specific amounts (10, 25, 50, 100, 250, 500, or 1000), depending on the treat type. If a bee is given its favorite treat, it gains double the usual bond amount and has a low chance to become Gifted or Mutated.
3.  **Combat/Tokens:** Bond is also rewarded from defeating mobs and collecting Puppy Love tokens dropped by Puppy Bees.

**Bond Modifiers (Maximum Boost):**
The total bond gained can be increased through various buffs:
*   Gifted Puppy Bee's ability provides a 20% boost to all bond.
*   Moon Amulet abilities can increase bond from treats by 10%.
*   Equipping Reindeer Antlers on the Puppy Bee grants a 3% boost to all bond.

These buffs, when combined, allow players to achieve a maximum total bond boost of 33%.

**Leveling Details:**
*   A bee's bond level does not reset after leveling up; however, the in-game information window only displays the required bond for the *next* level, which can make it appear as if the bond has dropped to zero. (This is why server messages show a different number than the info window when feeding treats.)
*   A bee's rarity does not affect its bond requirements. Both Common and Mythic bees require 10 bonds to reach Level 2 from Level 1.
*   Bond does not diminish when using Royal Jellies or replacing a bee with an egg.

**Mob Combat Levels:**
Mobs also have levels, which determines the success rate of a bee's attack:
*   If the bee's level is equal to or higher than the mob's level, the hit is guaranteed (100%).
*   The chance of hitting decreases by 25% for every level difference.

**Hit Chance Formula:**
The probability of a bee hitting a mob is calculated as:
$$\frac{1}{2^{(\text{monster\_level} - \text{bee\_level})}}$$

**Level Cap:**
The maximum level a bee can achieve is 25. While it is generally difficult to reach levels above 20, bees will continue to gain bond even after reaching the maximum level.

### Leveling Costs (Honey/Treats)

The table below details the required bond and the corresponding honey cost for leveling up a hive of 50 bees. The costs vary based on active bond modifiers:
*   **Base:** Standard cost without buffs.
*   **With Moon Amulet Max (+10% BFT):** Cost with only the Moon Amulet bonus applied.
*   **With Gifted Puppy Bee (+20% BFT):** Cost with only the Gifted Puppy Bee bonus applied.
*   **Both (+30% BFT):** Cost with both buffs applied (maximum achievable boost).

| Level | Bond Required for Next Level | Honey Cost for 50 Bees (Base) | Honey Cost for 50 Bees (+20% BFT) | Honey Cost for 50 Bees (+30% BFT) |
| :---: | :---------------------------: | :----------------------------: | :-------------------------------: | :-------------------------------: |
| **1** | 0                             | 0                              | 0                                 | 0                                 |
| **2** | 10                            | 8.33K                          | 7.69K                             | 500K                              |
| **3** | 40                            | 30.8K                          | 33.3K                             | 1.538M                            |
| **4** | 200                           | 154K                           | 167K                              | 7.692M                            |
| **5** | 750                           | 577K                           | 625K                              | 28.846M                           |
| **6** | 4,000                         | 3.08M                          | 3.33M                             | 153.846M                          |
| **7** | 15,000                        | 11.5M                          | 12.5M                             | 576.923M                          |
| **8** | 60,000                        | 46.2M                          | 50M                               | 2.308B                            |
| **9** | 270,000                       | 208M                           | 225M                              | 10.385B                           |
| **10** | 450,000                      | 346M                           | 375M                              | 17.308B                           |
| **11** | 1,200,000                    | 923M                           | 1B                                | 46.154B                           |
| **12** | 2,000,000                    | 1.54B                          | 1.67B                             | 76.923B                           |
| **13** | 4,000,000                    | 3.08B                          | 3.33B                             | 153.846B                          |
| **14** | 7,000,000                    | 5.38B                          | 5.83B                             | 269.231B                          |
| **15** | 15,000,000                   | 11.5B                          | 12.5B                             | 576.923B                          |
| **16** | 120,000,000                  | 92.3B                          | 100B                              | 4.615T                            |
| **17** | 450,000,000                  | 346B                           | 375B                              | 17.308T                           |
| **18** | 1,900,000,000                | 1.46T                          | 1.58T                             | 73.077T                           |
| **19** | 7,500,000,000                | 5.77T                          | 6.25T                             | 288.462T                          |
| **20** | 15,000,000,000               | 11.5T                          | 12.5T                             | 576.923T                          |
| **21** | 475,000,000,000              | 365T                           | 396T                              | 18.27Qd                           |
| **22** | 4,500,000,000,000            | 3.46Qd                         | 3.75Qd                            | 173.1Qd                           |
| **23** | 95,000,000,000,000           | 73.1Qd                         | 79.2Qd                            | 3.654Qn                           |
| **24** | 900,000,000,000,000          | 692Qd                          | 750Qd                             | 34.62Qn                           |
| **25** | 9,000,000,000,000,000        | 6.92Qn                         | 7.5Qn                             | 346.2Qn                           |

*Note: Costs are calculated assuming each Treat is priced at 10K honey.*

**Alternative Cost Formula:**
The cost to level up can also be determined using the following formula:
$$\left(\frac{10 \times (\text{Bond For Next Level}) \times (\text{Number Of Bees})}{\text{Bond From Treats}} - \text{Treats In Inventory}\right) \times 10,000$$

### Trivia

*   The maximum possible bond boost from treats is 133%: 100% base + 20% (Gifted Puppy Bee Hive Bonus) + 10% (Moon Amulet) + 3% (Reindeer Antlers Beequip).
*   Temporary bees can still be leveled up.
*   Before the November 25, 2018 update, the bee information page displayed the total bond instead of the current bond required for the next level.
*   Leveling a full hive of 50 bees from Level 0 to Level 25 would cost approximately 500 Quintillion honey in treats (Base Cost). With the maximum achievable bond boost (133%), this cost is reduced to about 376 Quintillion honey.

### Bee Wings
*   Level 1 bees do not have wings, as there is no decal applied at that level.