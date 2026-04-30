# Nectar

![Digital Bee](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D) | **Disclaimer:** This content contains information obtained through datamining. Due to the nature of the data, details may be inaccurate or outdated. Datamined information includes the scaling mechanics of all Nectars' buffs. (Data file date: December 19th, 2024).

## Overview and Acquisition
Nectar is a set of powerful buffs added in the 2021-12-26 update. It can be acquired through several methods:

*   **Planters:** Harvesting nectar from various planters.
*   **Sipping:** Bees sipping from planters.
*   **Events/Items:** Using Dapper Bear's Samovar during Beesmas, or using a nectar vial item.
*   **Quests:** Certain quests require specific amounts and types of nectar to be collected.

All sources contribute to quest requirements (except collecting Nectar directly from the Nectar Pot).

### Locations and Storage
*   The **Nectar Pot**, located in the 30 Bee Zone, allows for storage.
*   The **Nectar Condenser**, located in the 35 Bee Zone, is used to convert nectar into vials.

**Storage Mechanics:**
*   Nectar can be stored inside the Nectar Pot for up to 5 Tickets.
*   All five types of Nectar are storable.
*   To deposit new Nectar, any existing stored Nectar must first be withdrawn.
*   If nectar is not stored, it will continue to deplete even when the player is offline.

## Nectar Mechanics and Types
There are five distinct types of Nectar: Invigorating, Satisfying, Motivating, Comforting, and Refreshing.

Nectar buffs can last for up to 24 hours. The strength of the boost granted scales based on the amount of time remaining on the buff.

**Condensation:** 12 hours of nectar can be converted into a Nectar Vial using the Nectar Condenser. Any excess nectar beyond the 12-hour limit cannot be condensed.

### Types and Bonuses
The following table details the five types of Nectar, their associated buffs, where they are found, and how various planters modify their yield.

| Nectar Type | Buffs (Min - Max) | Fields Found In | Planter Multipliers |
| :---: | :--- | :--- | :--- |
| **Comforting** | x1.2 - x2 Colorless Bee [Convert Rate] <br> x1.1 - x1.5 [Blue Pollen] <br> x1.1 - x2 [Convert Rate At Hive] | Dandelion Field, Bamboo Field, Pine Tree Forest | x1.2 from Blue Clay Planter <br> x1.25 from Tacky Planter <br> x1.4 from Hydroponic Planter <br> x1.5 from Petal Planter |
| **Motivating** | x1.1 - x1.5 [Convert Rate] <br> x1.1 - x1.5 [Blue Pollen] <br> +1% - +5% [Bee Ability Rate] | Mushroom Field, Spider Field, Stump Field, Rose Field | x1.2 from Candy Planter <br> x1.3 from Pesticide Planter <br> x1.4 from Heat-Treated Planter |
| **Satisfying** | x1.2 - x2 Red [Convert Rate] <br> x1.2 - x2 [White Pollen] <br> x1.05 - x1.5 [Honey at Hive] | Sunflower Field, Pineapple Patch, Pumpkin Patch | x1.2 from Red Clay Planter <br> x1.25 from Tacky Planter <br> x1.3 from Pesticide Planter <br> x1.5 from Petal Planter |
| **Refreshing** | x1.2 - x2 Blue [Convert Rate] <br> x1.1 - x1.5 [Red Pollen] <br> +5% - +20% [Unique Instant Conversion] | Blue Flower Field, Strawberry Field, Coconut Field | x1.2 from Blue Clay Planter <br> x1.4 from Hydroponic Planter |
| **Invigorating** | x1.1 - x1.5 [Convert Rate] <br> x1.1 - x1.5 [Red Pollen] <br> x1.02 - x1.10 [Bee Attack] | Clover Field, Cactus Field, Mountain Top Field, Pepper Patch | x1.2 from Red Clay Planter <br> x1.4 from Heat-Treated Planter |

*Note: In addition to the primary buffs listed above, every type of nectar grants an additional bonus of x1.01 - x1.05 [Honey Per Pollen].*

**General Planter Bonuses:**
All nectar types receive a base multiplier based on the planter used:
*   Paper Planter: x0.75
*   The Planter Of Plenty: x1.5
*   Ticket Planters / Sticker Planters: x2
*   Festive Planters: x3

## Buff Scaling Formula
The amount of a buff received from nectar is not constant; it scales based on the time remaining on the effect.

**Formula:**
$$\text{Buff Amount} = \min + (\max - \min) \times \left(\frac{t}{86400}\right)^{0.7}$$

Where:
*   $t$: The number of seconds left on the buff (Maximum duration is 24 hours, or 86400 seconds).
*   $\min$: The minimum possible value of the given buff.
*   $\max$: The maximum possible value of the given buff.

The final result must be rounded to the nearest 0.001.

**Example Calculation (Comforting Nectar):**
To calculate Blue Pollen from 18 hours of Comforting Nectar:
1.  Convert time: $t = 18 \text{ hours} \times 3600 \text{ seconds/hour} = 64800$ seconds.
2.  Identify min/max: $\min = 1.1$, $\max = 1.5$.
3.  Apply formula: $1.1 + (1.5 - 1.1) \times \left(\frac{64800}{86400}\right)^{0.7} \approx 1.42704$
4.  Result: The player receives x1.427 Blue Pollen.

## Gallery and Trivia

### Icon Stickers
The game features several nectar icon stickers, each representing a type of Nectar:
*   **Satisfying:** Features the letter 'S' resembling a lightning bolt in its decal.
*   **Motivating:** Features the letter 'M' within the lightbulb filament.
*   **Invigorating:** Displays the lower part of an 'I' or a small capital 'I' at the bottom of the fire graphic.
*   **Comforting:** Bears the letter 'C', which resembles a crescent moon shape.
*   **Refreshing:** Is unique as it has no visible letter, though it is presumed to contain the gaps forming the letter 'R'.

### Advanced Mechanics and Lore
*   **Shy Bee Passive:** The Shy Bee possesses the passive ability "Nectar Lover," making it twice as likely to sip nectar and gather twice as much. It also contributes double to a planter's growth rate.
*   **Field Restrictions:** Nectar cannot be collected from the Ant Field or the Hub Field. Although Onett announced that the Ant Field contains Invigorating Nectar, collection is currently restricted. (Note: A past glitch allowed planters in the Hub Field, which would grant Comforting Nectar, but abusing this method risks account flagging.)