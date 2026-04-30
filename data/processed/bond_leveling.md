# Bee Leveling and Bond

**Bond** is a core mechanic equivalent to leveling systems found in many other games. When bees develop a high enough bond with the player, they level up, granting the following stat boosts per level above 1:

*   +5% Gather Amount
*   +10% Production Amount (Conversion)
*   +5% Energy
*   +3% Movespeed

### Bond Mechanics

Bond can be checked at any time by clicking on a bee's hive slot, which displays the bee's current bond and stats.

**Gaining Bond:**

1.  **Pollen Collection:** Bees automatically gain bond when collecting pollen in fields. Each bee type has an opinion (like, neutral, or dislike) of each field.
    *   If a bee has a sad emoticon over its head, it dislikes the field and gains only minimal bond.
    *   A happy emoticon indicates the bee likes the field and will gain extra bond.
    *   No emoticon means the bee is neutral and gains the usual amount.
2.  **Treats:** Bees can be fed treats to increase their bond by 10, 25, 50, 100, 250, 500, or 1000, depending on the treat type. If a player feeds a bee its favorite treat, it gains double the normal amount of bond and has a low chance to become Gifted or Mutated.
3.  **Combat & Tokens:** Bond is also rewarded from defeating mobs and collecting a Puppy Love token from a Puppy Bee.

**Bond Multipliers (Maximum 133%):**

The base bond gain can be increased through various buffs:

*   **Gifted Puppy Bee Ability:** Provides a 20% boost to all bond gained from treats.
*   **Moon Amulet Ability:** Increases bond by 10% when fed treats.
*   **Reindeer Antlers Beequip:** Grants a 3% boost to all bond when equipped on the Puppy Bee.

These buffs can be combined for a maximum total bonus of 33% (20% + 10% + 3%) to treat-based bond gain.

### Leveling Details

*   **Bond Persistence:** A bee's bond does not reset after leveling up. However, the information window only displays the bond required for the *next* level, which can make it appear as if the bond has dropped to zero (this is why server messages show a different number than the info window when feeding treats).
*   **Rarity:** A bee's rarity does not affect how much bond it needs to level up. Both Common and Mythic bees require 10 bonds to reach Level 2 from Level 1.
*   **Maximum Level:** The maximum level a bee can achieve is 25. Even if a bee reaches the maximum level, it will continue to gain bond.

### Combat Scaling (Mob Levels)

Mobs also have levels, which determines attack accuracy:

*   If the bee's level is the same or higher than the mob's level, the attack is guaranteed to hit.
*   If the bee is one level lower than the mob, it has a 50% chance to hit.
*   If the bee is two levels lower than the mob, it has a 25% chance to hit, and so on.

The formula for calculating the chance of hitting a mob is:
$$ \frac{1}{2^{(monsterlevel-beelevel)}} $$

### Leveling Costs (Honey)

The following table shows the required bond cost per level and the corresponding Honey cost to achieve that level for 50 bees, based on different bonus multipliers. (Assumes each treat costs 10K honey).

| Level | Base Bond Required | With Moon Amulet Max (+10% BFT) | With Gifted Puppy Bee (+20% BFT) | Both (+30% BFT) | Base Cost for 50 Bees | Cost with Gifted Puppy Bee (+20% BFT) | Cost with Both (+30% BFT) |
| :---: | :----------------: | :------------------------------: | :-------------------------------: | :------------: | :--------------------: | :----------------------------------: | :--------------------------: |
| 1     | 0                  | 0                                | 0                                 | 0              | 0                      | 0                                    | 0                            |
| 2     | 10                 | 10K                              | 7.69K                             | 500K           | 8.33K                  | 416.7K                               | 384.6K                       |
| 3     | 40                 | 36.4K                            | 30.8K                             | 1.538M         | 33.3K                  | 1.667M                               | 2M                           |
| 4     | 200                | 182K                             | 154K                              | 7.692M         | 167K                   | 8.333M                               | 10M                          |
| 5     | 750                | 682K                             | 577K                              | 28.846M        | 577K                   | 31.25M                               | 37.5M                        |
| 6     | 4,000              | 3.64M                            | 3.08M                             | 153.846M       | 3.33M                  | 166.667M                             | 200M                         |
| 7     | 15,000             | 13.6M                            | 11.5M                             | 576.923M       | 12.5M                  | 625M                                 | 750M                         |
| 8     | 60,000             | 54.5M                            | 46.2M                              | 2.308B         | 50M                    | 2.5B                                 | 3B                           |
| 9     | 270,000            | 245M                             | 208M                              | 10.385B        | 225M                   | 11.25B                               | 13.5B                        |
| 10    | 450,000            | 409M                             | 346M                              | 17.308B        | 375M                   | 18.75B                               | 22.5B                        |
| 11    | 1,200,000          | 1.09B                            | 923M                              | 46.154B        | 1B                     | 50B                                  | 60B                          |
| 12    | 2,000,000          | 1.82B                            | 1.54B                              | 76.923B        | 1.67B                  | 83.333B                              | 100B                         |
| 13    | 4,000,000          | 3.64B                            | 3.08B                              | 153.846B       | 3.33B                  | 166.667B                             | 200B                         |
| 14    | 7,000,000          | 6.36B                            | 5.38B                              | 269.231B       | 5.83B                  | 291.667B                             | 350B                         |
| 15    | 15,000,000         | 13.6B                            | 11.5B                              | 576.923B       | 12.5B                  | 625B                                 | 750B                         |
| 16    | 120,000,000        | 109B                             | 92.3B                              | 4.615T         | 100B                   | 5T                                   | 6T                           |
| 17    | 450,000,000        | 409B                             | 346B                               | 17.308T        | 375B                   | 18.75T                               | 22.5T                        |
| 18    | 1,900,000,000      | 1.72T                            | 1.46T                              | 73.077T        | 1.58T                  | 79.167T                              | 95T                          |
| 19    | 7,500,000,000      | 6.82T                            | 5.77T                              | 288.462T       | 6.25T                  | 312.5T                               | 375T                         |
| 20    | 15,000,000,000     | 13.6T                            | 11.5T                              | 576.923T       | 12.5T                  | 625T                                 | 750T                         |
| 21    | 475,000,000,000    | 432T                             | 365T                               | 18.27Qd        | 396T                   | 19.792Qd                             | 23.75Qd                       |
| 22    | 4,500,000,000,000  | 4.09Qd                           | 3.46Qd                             | 173.1Qd        | 3.75Qd                 | 187.5Qd                              | 225Qd                         |
| 23    | 95,000,000,000,000 | 86.4Qd                           | 73.1Qd                             | 3.654Qn        | 79.2Qd                 | 3.958Qn                              | 4.75Qn                        |
| 24    | 900,000,000,000,000 | 818Qd                            | 692Qd                              | 34.62Qn        | 750Qd                  | 37.5Qn                               | 45Qn                          |
| 25    | 9,000,000,000,000,000 | 8.18Qn                           | 6.92Qn                             | 346.2Qn        | 7.5Qn                  | 375Qn                                | 450Qn                         |

**Alternative Cost Formula:**
The cost to level up can also be determined using this formula:
$$ \left(\frac{10(BondForNextLevel)(NumberOfBees)}{BondFromTreats}-TreatsInInventory\right) \times 10000 $$

### Bee Wings
Bee wings are cosmetic items that change based on the bee's level. Level 1 bees do not have visible wings, as they lack a decal. The available wing types range from Wing2 to Wing25.

### Trivia
*   The maximum possible bond gain from treats is currently 133%: 100% base + 20% (Gifted Puppy Bee Hive Bonus) + 10% (Moon Amulet) + 3% (Reindeer Antlers Beequip).
*   Temporary bees can still be leveled up.
*   Prior to the 2018-11-25 update, the bee information page always displayed the total bond, not the current bond required for the next level.
*   Leveling a full hive of 50 bees from Level 0 to Level 25 would cost approximately 500 Quintillion Honey in treats. With the maximum achievable treat bonus (133%), this cost can be reduced to about 376 Quintillion Honey.