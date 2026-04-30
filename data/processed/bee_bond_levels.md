# Bee Bond and Leveling System

The **Bond** mechanic is equivalent to the leveling system found in many other games. When bees achieve a high enough bond with the player, they level up, gaining the following boosts per level above 1:

*   +5% Gather Amount
*   +10% Conversion Amount (Production)
*   +5% Energy
*   +3% Movespeed

## Bond Mechanics

Bond can be checked at any time by clicking on a bee's hive slot, which displays the bee's current bond and stats.

**Gaining Bond:**

A bee automatically gains bond when collecting pollen in a field. Each bee type has an opinion of each field (likes, neutral, or dislikes).
*   If a bee has a sad emoticon over its head, it dislikes the field and gains only minimal bond.
*   If it has a happy emoticon, it likes the field and gains extra bond.
*   If there is no emoticon, it is neutral and gains the usual amount of bond.

Bond can also be increased by feeding treats:
*   Treats provide 10, 25, 50, 100, 250, 500, or 1000 bond depending on the type.
*   If a bee is fed its favorite treat, it gains double the normal amount of bond and has a low chance to become Gifted or Mutated.

Bond is also rewarded from defeating mobs and collecting a Puppy Love token from a Puppy Bee.

**Bond Modifiers:**

The total amount of bond gained from treats can be increased by several buffs:
*   The gifted Puppy Bee's ability provides a 20% boost to all bond.
*   One Moon Amulet ability increases bond by 10% from treats.
*   Equipping the Reindeer Antlers on the Puppy Bee grants a 3% boost to all bond.

These buffs can combine for a maximum total of 33% bonus bond gain in the game.

**Leveling Details:**

A bee's bond does not reset after leveling up; however, the information window only displays the bond required for the next level, which may make it appear as if the bond has dropped to zero. (This is why server messages regarding treat bonuses may show a different number than the in-game info window.)

*   A bee's rarity does not affect its bond requirements. A Common and a Mythic bee at Level 1 both require 10 bonds to level up.
*   Bond does not diminish when using Royal Jellies or replacing a bee with an egg.

**Mob Combat Levels:**

Mobs also have levels, which determine attack success:
*   If the bee's level is equal to or higher than the mob's level, the attack is guaranteed to hit.
*   If the bee is one level lower, it has a 50% chance to hit.
*   If the bee is two levels lower, it has a 25% chance to hit, and so on.

The formula for calculating the chance of hitting a mob is:
$$ \frac{1}{2^{(monsterlevel-beelevel)}} $$

The maximum level a bee can achieve is 25. While reaching levels above 20 is difficult, bees will continue to gain bond even at maximum level.

## Bee Leveling Costs (Honey)

The table below shows the required bond and the corresponding honey cost for leveling up a hive of 50 bees. Honey costs are calculated assuming each treat is priced at 10K honey.

| Level | Bond Required for Level | Base Cost (50 Bees) | With Gifted Puppy Bee (+20% BFT) | With Both Buffs (+30% BFT) |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 0 | 0 | 0 | 0 |
| 2 | 10 | 8.33K | 7.69K | 500K |
| 3 | 40 | 30.8K | 33.3K | 1.538M |
| 4 | 200 | 154K | 167K | 7.692M |
| 5 | 750 | 577K | 625K | 28.846M |
| 6 | 4,000 | 3.08M | 3.33M | 153.846M |
| 7 | 15,000 | 11.5M | 12.5M | 576.923M |
| 8 | 60,000 | 46.2M | 50M | 2.308B |
| 9 | 270,000 | 208M | 225M | 10.385B |
| 10 | 450,000 | 346M | 375M | 17.308B |
| 11 | 1,200,000 | 923M | 1B | 46.154B |
| 12 | 2,000,000 | 1.54B | 1.67B | 76.923B |
| 13 | 4,000,000 | 3.08B | 3.33B | 153.846B |
| 14 | 7,000,000 | 5.38B | 5.83B | 269.231B |
| 15 | 15,000,000 | 11.5B | 12.5B | 576.923B |
| 16 | 120,000,000 | 92.3B | 100B | 4.615T |
| 17 | 450,000,000 | 346B | 375B | 17.308T |
| 18 | 1,900,000,000 | 1.46T | 1.58T | 73.077T |
| 19 | 7,500,000,000 | 5.77T | 6.25T | 288.462T |
| 20 | 15,000,000,000 | 11.5T | 12.5T | 576.923T |
| 21 | 475,000,000,000 | 365T | 396T | 18.27Qd |
| 22 | 4,500,000,000,000 | 3.46Qd | 3.75Qd | 173.1Qd |
| 23 | 95,000,000,000,000 | 73.1Qd | 79.2Qd | 3.654Qn |
| 24 | 900,000,000,000,000 | 692Qd | 750Qd | 34.62Qn |
| 25 | 9,000,000,000,000,000 | 6.92Qn | 7.5Qn | 346.2Qn |

**Alternative Cost Formula:**

You can determine the cost to level up your bees using this formula:
$$ \left(\frac{10(BondForNextLevel)(NumberOfBees)}{BondFromTreats}-TreatsInInventory\right) \times 10000 $$

## Bee Wings

*   Note that Level 1 bees do not have wings, as they will lack a decal.
*   The various wing images (Wing2 through Wing25) are available for use in bee customization.

## Trivia

*   **Maximum Bond:** The maximum possible bond bonus from treats is currently 133% (100% base + 20% Gifted Puppy Bee Hive Bonus + 10% Moon Amulet + 3% Reindeer Antlers Beequip).
*   Temporary bees can still be leveled up.
*   Prior to the November 25, 2018 update, the bee information page displayed the total bond instead of the current bond required for the next level.
*   Leveling a full hive of 50 bees from Level 0 to Level 25 would cost approximately 500 Quintillion Honey in treats. With the maximum possible treat bonus (133%), this cost can be reduced to about 376 Quintillion Honey.