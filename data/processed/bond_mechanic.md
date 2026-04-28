# Bond Mechanic

**Bond** is a core mechanic equivalent to the leveling system found in many other games. When bees achieve a high enough bond with the player, they level up and gain the following stat boosts per level above 1:

*   +5% Gather Amount
*   +10% Production Amount (Conversion)
*   +5% Energy
*   +3% Movespeed

### Tracking Bond
Bond can be checked at any time by clicking on a bee's hive slot, which displays the bee's current bond and stats.

### How to Gain Bond
Bees automatically gain bond when collecting pollen in fields. Each bee type has an opinion of every field (likes, neutral, or dislikes).

*   **Dislike:** If a bee has a sad emoticon over its head, it dislikes the field and gains only minimal bond while collecting pollen there.
*   **Like:** If a bee has a happy emoticon, it likes the field and gains extra bond.
*   **Neutral:** If no emoticon is present, the bee is neutral and gains the usual amount of bond.

Bond can also be increased through other actions:

1.  **Treats:** Bees can be fed treats to increase their bond by 10, 25, 50, 100, 250, 500, or 1000, depending on the treat type. If the player feeds a bee its favorite treat, it gains double the usual amount of bond and has a low chance to become Gifted or Mutated.
2.  **Combat:** Bond is rewarded from defeating mobs.
3.  **Tokens:** Bond is also gained by collecting a Puppy Love token from a Puppy Bee.

### Bond Buffs and Multipliers
The maximum bond gain from treats can be boosted:

*   **Gifted Puppy Bee's Ability:** Provides a 20% boost to all bond.
*   **Moon Amulet Ability:** Increases bond by 10% when fed treats.
*   **Reindeer Antlers Beequip:** Grants a 3% boost to all bond when equipped on the Puppy Bee.

Combining these buffs results in a total maximum of 33% increased bond gain from treats for the player.

### Leveling Mechanics and Limitations
A bee's bond does not reset after leveling up; however, the information window only displays the required bond for the next level, which can make it appear as if the bond has dropped to zero. (This is why server messages regarding treat feeding may show a different number than the in-game info window.)

*   **Rarity:** A bee's rarity does not affect how much bond it needs to level up. Both Common and Mythic bees require 10 bonds to reach Level 2 from Level 1.
*   **Bond Persistence:** Bond does not diminish when using Royal Jellies or replacing a bee with an egg.
*   **Maximum Level:** The maximum level a bee can achieve is 25. While difficult, bees will continue gaining bond even after reaching the maximum level.

### Combat and Mob Levels
Mobs also have levels, which determines hit chance during combat:

*   If the bee has the same or higher level than the mob, it guarantees a hit.
*   If the bee is one level lower than the mob, it has a 50% chance to hit.
*   If the bee is two levels lower than the mob, it has a 25% chance to hit, and so on.

The formula for calculating the chance of hitting a mob is:
$$\frac{1}{2^{(monsterlevel-beelevel)}}$$

### Bee Level Costs (Honey Equivalent)
The following table details the bond required for each level and the associated honey cost for 50 bees, based on different available buffs. (Assuming one Treat costs 10K Honey).

| Level | Base Bond Required | With Moon Amulet Max (+10% BFT) | With Gifted Puppy Bee (+20% BFT) | Both Buffs (+30% BFT) | Base Cost for 50 Bees | Cost with Gifted Puppy Bee (+20% BFT) | Cost with Both Buffs (+30% BFT) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 0 | **0** | 0 | 0 | 0 | 0 | **0** |
| 2 | 10 | **10K** | 9.09K | 8.33K | 8.33K | 7.69K | **500K** |
| 3 | 40 | **40K** | 36.4K | 33.3K | 30.8K | 2M | **1.667M** |
| 4 | 200 | **200K** | 182K | 167K | 154K | 10M | **8.333M** |
| 5 | 750 | **750K** | 682K | 625K | 577K | 37.5M | **31.25M** |
| 6 | 4,000 | **4M** | 3.64M | 3.33M | 3.08M | 200M | **166.667M** |
| 7 | 15,000 | **15M** | 13.6M | 12.5M | 11.5M | 750M | **625M** |
| 8 | 60,000 | **60M** | 54.5M | 50M | 46.2M | 3B | **2.5B** |
| 9 | 270,000 | **270M** | 245M | 225M | 208M | 13.5B | **11.25B** |
| 10 | 450,000 | **450M** | 409M | 375M | 346M | 22.5B | **18.75B** |
| 11 | 1,200,000 | **1.2B** | 1.09B | 1B | 923M | 60B | **50B** |
| 12 | 2,000,000 | **2B** | 1.82B | 1.67B | 1.54B | 100B | **83.333B** |
| 13 | 4,000,000 | **4B** | 3.64B | 3.33B | 3.08B | 200B | **166.667B** |
| 14 | 7,000,000 | **7B** | 6.36B | 5.83B | 5.38B | 350B | **291.667B** |
| 15 | 15,000,000 | **15B** | 13.6B | 12.5B | 11.5B | 750B | **625B** |
| 16 | 120,000,000 | **120B** | 109B | 100B | 92.3B | 6T | **5T** |
| 17 | 450,000,000 | **450B** | 409B | 375B | 346B | 22.5T | **18.75T** |
| 18 | 1,900,000,000 | **1.9T** | 1.72T | 1.58T | 1.46T | 95T | **79.167T** |
| 19 | 7,500,000,000 | **7.5T** | 6.82T | 6.25T | 5.77T | 375T | **312.5T** |
| 20 | 15,000,000,000 | **15T** | 13.6T | 12.5T | 11.5T | 750T | **625T** |
| 21 | 475,000,000,000 | **475T** | 432T | 396T | 365T | 23.75Qd | **19.792Qd** |
| 22 | 4,500,000,000,000 | **4.5Qd** | 4.09Qd | 3.75Qd | 3.46Qd | 225Qd | **187.5Qd** |
| 23 | 95,000,000,000,000 | **95Qd** | 86.4Qd | 79.2Qd | 73.1Qd | 4.75Qn | **3.958Qn** |
| 24 | 900,000,000,000,000 | **900Qd** | 818Qd | 750Qd | 692Qd | 45Qn | **37.5Qn** |
| 25 | 9,000,000,000,000,000 | **9Qn** | 8.18Qn | 7.5Qn | 6.92Qn | 450Qn | **346.2Qn** |

Alternatively, the cost to level up can be calculated using this formula:
$$\frac{10(BondForNextLevel)(NumberOfBees)}{BondFromTreats}-TreatsInInventory) \times 10000$$

### Audio Cue
The following audio file plays when a bee levels up: [Levellllup.ogg](http://bee-swarm-simulator.fandom.com/wiki/File:Levellllup.ogg). (Note that the sound is slightly faster in-game.)

## Gallery
*(Image gallery content retained for completeness, though not strictly part of core mechanic data)*

### Bee Wings
*Level 1 bees do not have wings as there is no decal.*

## Trivia
*   The maximum possible Bond from Treats is 133%: 100% base + 20% from Gifted Puppy Bee's Hive Bonus + 10% from Moon Amulet + 3% from Reindeer Antlers Beequip.
*   Temporary bees can still be leveled up.
*   Prior to the 2018-11-25 update, the bee information page always displayed the bee's total bond, not the current bond required for the next level.
*   Leveling a full hive of 50 bees from Level 0 to Level 25 would cost 500Qn Honey in treats. With the maximum possible Bond from Treats (133%), this cost could be reduced to approximately 376Qn Honey in treats.