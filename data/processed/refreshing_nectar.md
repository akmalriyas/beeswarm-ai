# Refreshing Nectar

***Disclaimer:** This piece of content contains information obtained through datamining. Due to the nature of the information, details may be inaccurate or outdated.*

**Datamined Information:** The scaling mechanics for all Nectars' buffs.
**Date of Datamine:** December 19th, 2024

## Overview

Nectar is a set of powerful buffs introduced in the 2021-12-26 update. These buffs are granted through several methods: harvesting planters, having bees sip from planters, using Dapper Bear's Samovar during Beesmas, or consuming nectar vial items. Certain quests require specific amounts and types of nectar; all sources (except the Nectar Pot) contribute to these quests.

There are five distinct types of Nectar: Invigorating, Satisfying, Motivating, Comforting, and Refreshing.

### Mechanics

Nectar buffs can last for up to 24 hours, and the boosts granted scale based on the amount of time remaining.

*   **Condensing:** 12 hours of nectar can be converted into a Nectar Vial using the Nectar Condenser. Any excess nectar beyond the 12-hour limit will not be condensed.
*   **Storage:** Nectar can be stored in the Nectar Pot (located in the 30 Bee Zone) for up to 5 Tickets. All types of nectar are storable, but any existing stored nectar must be withdrawn before depositing new nectar. If nectar is not stored, it will continue to deplete even when the player is offline.

## Types and Sources

The table below details the five Nectar types, their associated buffs, where they can be obtained, and which planters provide enhanced yields.

*Note: All nectar types receive a base bonus of x0.75 from Paper Planters, x1.5 from The Planter Of Plenty, x2 from Ticket Planters and Sticker Planters, and x3 from Festive Planters.*

| Nectar Type | Buffs | Fields/Sources | Planter Bonuses |
| :---: | :--- | :--- | :--- |
| **Comforting** | x1.2 - x2 Colorless Bee [Convert Rate] <br> x1.1 - x1.5 Blue Pollen <br> x1.1 - x2 [Convert Rate At Hive] | Dandelion Field, Bamboo Field, Pine Tree Forest | x1.2 from Blue Clay Planter <br> x1.25 from Tacky Planter <br> x1.4 from Hydroponic Planter <br> x1.5 from Petal Planter |
| **Motivating** | x1.1 - x1.5 [Convert Rate] <br> x1.1 - x1.5 Blue Pollen <br> +1% - +5% [Bee Ability Rate] | Mushroom Field, Spider Field, Stump Field, Rose Field | x1.2 from Candy Planter <br> x1.3 from Pesticide Planter <br> x1.4 from Heat-Treated Planter |
| **Satisfying** | x1.2 - x2 Red [Convert Rate] <br> x1.2 - x2 White Pollen <br> x1.05 - x1.5 [Honey at Hive] | Sunflower Field, Pineapple Patch, Pumpkin Patch | x1.2 from Red Clay Planter <br> x1.25 from Tacky Planter <br> x1.3 from Pesticide Planter <br> x1.5 from Petal Planter |
| **Refreshing** | x1.2 - x2 Blue [Convert Rate] <br> x1.1 - x1.5 Red Pollen <br> +5% - +20% [Unique Instant Conversion] | Blue Flower Field, Strawberry Field, Coconut Field | x1.2 from Blue Clay Planter <br> x1.4 from Hydroponic Planter |
| **Invigorating** | x1.1 - x1.5 [Convert Rate] <br> x1.1 - x1.5 Red Pollen <br> x1.02 - x1.10 [Bee Attack] | Clover Field, Cactus Field, Mountain Top Field, Pepper Patch | x1.2 from Red Clay Planter <br> x1.4 from Heat-Treated Planter |

*Note: In addition to these buffs, every nectar grants an additional bonus of x1.01 - x1.05 [Honey Per Pollen].*

## Buff Scaling Formula

The amount of a buff received is not static; it scales based on the time remaining on the effect. The following formula calculates the final value:

$$
\text{Buff Value} = \min + (\max - \min) \times \left( \frac{t}{86400} \right)^{0.7}
$$

Where:
*   $t$ is the number of seconds left on the buff.
*   $\min$ and $\max$ are the minimum and maximum possible values for that specific buff.
*   The result is rounded to the nearest 0.001.

**Example Calculation:**
To calculate Blue Pollen from 18 hours of Comforting Nectar:

1.  Convert time to seconds: $t = 18 \text{ hours} \times 3600 \text{ seconds/hour} = 64,800$ seconds.
2.  Identify min and max values for Comforting Nectar's Blue Pollen: $\min = 1.1$, $\max = 1.5$.
3.  Apply the formula:
    $$
    \text{Buff Value} = 1.1 + (1.5 - 1.1) \times \left( \frac{64800}{86400} \right)^{0.7}
    $$
    $$
    \text{Buff Value} = 1.1 + (0.4) \times (0.75)^{0.7} \approx 1.42704...
    $$

The player will receive x1.427 Blue Pollen.

## Gallery Stickers

*   Satisfying Nectar Icon Sticker
*   Refreshing Nectar Icon Sticker
*   Motivating Nectar Icon Sticker
*   Invigorating Nectar Icon Sticker
*   Comforting Nectar Icon Sticker

## Trivia

*   Every nectar icon (except Refreshing) features a letter representing the first initial of its type. Refreshing has no visible letter, though it is presumed to have gaps resembling an 'R'.
    *   **C:** Comforting (resembles a crescent moon).
    *   **S:** Satisfying (resembles a lightning bolt in its decal).
    *   **M:** Motivating (in the lightbulb filament).
    *   **I:** Invigorating (the lower part of 'I' at the bottom of the fire).
*   The Shy Bee possesses the passive ability "Nectar Lover," making it twice as likely to sip nectar and gather double the amount. It also contributes twice as much to planter growth.
*   Nectar cannot be collected from the Ant Field, despite Onett claiming it contains Invigorating Nectar. Similarly, nectar cannot be collected from the Hub Field, although a glitch allowed planters there; harvesting in this field grants Comforting Nectar, but abusing this exploit may result in account flagging.