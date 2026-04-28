# Nectar

**Disclaimer:** This content contains information obtained through datamining. Due to the nature of this data, details may be inaccurate or outdated. (Datamined scaling of all Nectars' buffs; Data collected: December 19th, 2024).

---

Nectar is a set of powerful buffs added in the **2021-12-26 update**. It can be obtained through several methods: harvesting [Planters], having [Bees] sip from planters, using Dapper Bear's Samovar during Beesmas, or collecting nectar vial items. Certain [Quests] require specific amounts and types of nectar; all sources contribute to these quests (except collection from the Nectar Pot).

There are five distinct types of Nectar: Invigorating, Satisfying, Motivating, Comforting, and Refreshing.

## Mechanics and Storage

Nectar buffs can last for up to 24 hours. The boosts granted scale based on the amount of time remaining.

**Condensing:**
12 hours of nectar can be converted into a [Nectar Vial] using the [Nectar Condenser]. If a player possesses more than 12 hours of nectar, the excess will not be condensed.

**Storage:**
Nectar can also be stored in the [Nectar Pot], located in the 30 Bee Zone, for up to 5 [Tickets]. All types of Nectar are storable, but before depositing new nectar, any existing stored nectar must first be withdrawn. If nectar is not stored, it will continue to deplete even when the player is offline.

## Types and Sources

The table below details the five different Nectar types, their associated buffs, where they can be obtained, and which planters provide enhanced yields.

**Planter Bonus Multipliers:**
*   Paper Planter: x0.75 bonus
*   The Planter Of Plenty: x1.5 bonus
*   Ticket Planters & Sticker Planters: x2 bonus
*   Festive Planters: x3 bonus

| Nectar Type | Buffs | Fields | Planter Bonuses |
| :--- | :--- | :--- | :--- |
| **Comforting** | x1.2 - x2 Colorless Bee [Convert Rate] <br> x1.1 - x1.5 [Blue Pollen] <br> x1.1 - x2 [Convert Rate At Hive] | Dandelion Field, Bamboo Field, Pine Tree Forest | x1.2 from Blue Clay Planter <br> x1.25 from Tacky Planter <br> x1.4 from Hydroponic Planter <br> x1.5 from Petal Planter |
| **Motivating** | x1.1 - x1.5 [Convert Rate] <br> x1.1 - x1.5 [Blue Pollen] <br> +1% - +5% [Bee Ability Rate] | Mushroom Field, Spider Field, Stump Field, Rose Field | x1.2 from Candy Planter <br> x1.3 from Pesticide Planter <br> x1.4 from Heat-Treated Planter |
| **Satisfying** | x1.2 - x2 Red [Convert Rate] <br> x1.2 - x2 [White Pollen] <br> x1.05 - x1.5 [Honey at Hive] | Sunflower Field, Pineapple Patch, Pumpkin Patch | x1.2 from Red Clay Planter <br> x1.25 from Tacky Planter <br> x1.3 from Pesticide Planter <br> x1.5 from Petal Planter |
| **Refreshing** | x1.2 - x2 Blue [Convert Rate] <br> x1.1 - x1.5 [Red Pollen] <br> +5% - +20% [Unique Instant Conversion] | Blue Flower Field, Strawberry Field, Coconut Field | x1.2 from Blue Clay Planter <br> x1.4 from Hydroponic Planter |
| **Invigorating** | x1.1 - x1.5 [Convert Rate] <br> x1.1 - x1.5 [Red Pollen] <br> x1.02 - x1.10 [Bee Attack] | Clover Field, Cactus Field, Mountain Top Field, Pepper Patch | x1.2 from Red Clay Planter <br> x1.4 from Heat-Treated Planter |

*Note: In addition to these buffs, every nectar grants an additional x1.01 - x1.05 [Honey Per Pollen].*

## Buff Scaling Formula

The amount of a buff received is calculated based on the time remaining on the nectar.

**Formula:**
$$\text{Buff Amount} = \min + (\max - \min) \times \left( \frac{t}{86400} \right)^{0.7}$$

Where:
*   $t$: The number of seconds left on the buff.
*   $\min$: The minimum possible value of the given buff (e.g., 1.1).
*   $\max$: The maximum possible value of the given buff (e.g., 1.5).

The result is rounded to the nearest 0.001.

**Example Calculation:**
To find the Blue Pollen received from 18 hours of Comforting Nectar:
1.  Convert time to seconds: $t = 64800$ (18 hours $\times$ 3600 seconds/hour).
2.  Identify min and max values for Comforting Nectar's Blue Pollen buff: $\min = 1.1$, $\max = 1.5$.
3.  Apply the formula: $1.1 + (1.5 - 1.1) \times \left( \frac{64800}{86400} \right)^{0.7} = 1.42704...$
4.  Rounded result: The player receives x1.427 Blue Pollen.

## Gallery Stickers

The following stickers can be obtained in the game:
*   Satisfying Nectar Icon Sticker
*   Refreshing Nectar Icon Sticker
*   Motivating Nectar Icon Sticker
*   Invigorating Nectar Icon Sticker
*   Comforting Nectar Icon Sticker

## Trivia and Notes

*   Every nectar icon (except Refreshing) features a letter representing the first initial of its type. Refreshing has no visible letter, though it is presumed to have gaps resembling 'R'.
    *   **C**omforting resembles a crescent moon shape.
    *   **S**atisfying resembles a lightning bolt in its decal.
    *   **M**otivating features the letter 'M' within the lightbulb filament.
    *   **I**nvigorating has the lower part of an 'I' at the bottom of the fire icon.
*   The [Shy Bee] possesses the passive ability "Nectar Lover," making it twice as likely to sip nectar and gather twice as much nectar. It also contributes twice as much to planter growth.
*   Nectar cannot be collected from the [Ant Field], despite announcements suggesting Invigorating Nectar is present there. Similarly, harvesting planters in the [Hub Field] does not yield collectible nectar, although a known glitch allows placement and collection of Comforting Nectar—abusing this glitch may result in account flagging.