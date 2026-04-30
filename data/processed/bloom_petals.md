# Blooms and Petals

For a similar mob that only appears in Retro Swarm Challenge, see [Brick Bloom](/wiki/Brick_Bloom).

**Blooms** are passive field-based entities that can spawn naturally on fields or be summoned using a [Bloom Shaker](/wiki/Bloom_Shaker). They first appeared in the [2025-12-25 update](/wiki/Updates#2025-12-25). These large flowers are adorned with colored petals. The maximum amount of petals a bloom can contain scales with its level.

Collecting petals from blooms grants the respective petal's buff and honey equal to half of the bloom's original HP. Petals will always yield at least 50 honey, even if the bloom's health is under 100 pollen.

### Bloom Mechanics
When a bloom is first created, it has a 20-second timer and a set "base" petal color, which usually constitutes the majority of the petals. Once the required pollen is met, the bloom will pop, scattering each petal in a circular pattern. After popping, a "child" bloom of a higher level and identical base color will spawn. Child blooms cease to spawn one minute after the original "parent" bloom spawned.

Blooms have a small chance to be "mutated" upon creation, where one or more petals are a different color from the base color. As the bloom's level increases, the chance of mutation also increases. A parent bloom being mutated does not affect the probability of its child blooms having mutations.

Hitting blooms with a Petal Shuriken (from [Petal Wand](/wiki/Petal_Wand) or [Petal Belt](/wiki/Petal_Belt)'s ability) causes them to spawn bonus petals. This attack also deals 20% of the remaining HP and 5% of the Bloom's maximum HP.

## Levels

Blooms have multiple levels. Each time a bloom is defeated, it respawns at a higher level, similar to how [Puffshrooms](/wiki/Puffshroom) work.

### Petals per Level
The number of petals a bloom can hold is capped at 11 for level 20 and above. For levels below 20, the number of petals can be calculated using the following formula:

$$\lfloor (level \times 2) \div 5 \rfloor + 3$$

| Level Range | Petals |
| :---: | :---: |
| 1–2 | 3 |
| 3–4 | 4 |
| 5–7 | 5 |
| 8–9 | 6 |
| 10-12 | 7 |
| 13-14 | 8 |
| 15-17 | 9 |
| 18-19 | 10 |
| 20+ | 11 |

### Health and Pollen Requirements
A bloom's health depends strongly on its level and the field it spawns in. The following table shows the required pollen per level for various fields:

| Field | Lvl 1 | Lvl 2 | Lvl 3 | Lvl 4 | Lvl 5 | Lvl 6 | Lvl 7 | Lvl 8 | Lvl 9 | Lvl 10 | Lvl 11 | Lvl 12 | Lvl 13 | Lvl 14 | Lvl 15 | Lvl 16 | Lvl 17 | Lvl 18 | Lvl 19 | Lvl 20 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [Sunflower Field](/wiki/Sunflower_Field) | 30 | 40 | 70 | 130 | 220 | 380 | 650 | 1.11K | 1.91K | 3.29K | 5.65K | 9.72K | 16.7K | 28.8K | - | - | 146K | - | - | - |
| [Dandelion Field](/wiki/Dandelion_Field) | 50 | 90 | 170 | 320 | 590 | 1.1K | 2.03K | 3.77K | 7K | 13K | 24.1K | 44.6K | 82.8K | 154K | 285K | 528K | - | - | 3.37M | - |
| [Mushroom Field](/wiki/Mushroom_Field) | 50 | 90 | 170 | 320 | 590 | 1.1K | 2.03K | 3.77K | 7K | 13K | 24.1K | 44.6K | 82.8K | 154K | 285K | 528K | - | - | 3.37M | - |
| [Clover Field](/wiki/Clover_Field) | 80 | 150 | 290 | 580 | 1.15K | 2.27K | 4.48K | 8.86K | 17.5K | 34.6K | 68.5K | 135K | 268K | 530K | 1.05M | 2.07M | 4.09M | - | 16M | - |
| [Blue Flower Field](/wiki/Blue_Flower_Field) | 150 | 250 | 430 | 730 | 1.24K | 2.1K | 3.55K | 6.02K | 10.2K | 17.3K | 29.3K | 49.8K | 84.1K | - | - | - | - | - | - | - |
| [Bamboo Field](/wiki/Bamboo_Field) | 250 | 600 | 1.43K | 3.42K | 8.17K | 19.5K | 46.7K | 112K | 267K | 639K | 1.53M | 3.65M | 20.9M | - | - | - | - | 1.63B | - |
| [Strawberry Field](/wiki/Strawberry_Field) | 250 | 600 | 1.43K | 3.42K | 8.17K | 19.5K | 46.7K | 112K | 267K | 639K | 1.53M | 3.65M | 20.9M | - | - | - | - | 1.63B | - |
| [Spider Field](/wiki/Spider_Field) | 1K | 2.07K | 4.28K | 8.86K | 18.3K | 37.9K | 78.5K | 162K | 336K | 695K | 1.44M | 2.98M | 6.16M | - | 26.4M | - | 113M | - | - | - |
| [Pineapple Patch](/wiki/Pineapple_Patch) | 500 | 1.13K | 2.57K | 5.81K | 13.2K | 29.8K | 67.6K | 153K | 347K | 785K | 1.78M | 4.03M | 9.13M | 20.7M | 46.9M | 106M | 240M | 545M | 1.23B | 2.8B |
| [Stump Field](/wiki/Stump_Field) | 5K | 12.3K | 30K | 73.6K | 180K | 442K | 1.08M | 2.66M | 6.51M | 16M | 39.1M | 95.9M | 235M | 576M | 1.41B | 3.46B | - | 20.8B | 51B | 125B |
| [Rose Field](/wiki/Rose_Field) | 50 | 210 | 890 | 3.77K | 15.9K | 67.4K | 285K | 1.2M | 5.09M | 21.5M | 90.9M | 384M | 1.62B | 6.86B | 29B | - | 518B | 2.19T | - | 39.1T |
| [Cactus Field](/wiki/Cactus_Field) | 500 | 1.13K | 2.57K | 5.81K | 13.2K | 29.8K | 67.6K | 153K | 347K | 785K | 1.78M | 4.03M | 9.13M | 20.7M | - | 106M | 240M | - | 1.23B | - |
| [Pumpkin Patch](/wiki/Pumpkin_Patch) | 2.5K | 3.77K | 5.7K | 8.6K | 13K | 19.6K | 29.6K | 44.6K | 67.4K | 102K | 154K | 232K | 350K | 528K | 797K | 1.2M | 1.82M | 2.74M | 4.14M | - |
| [Pine Tree Forest](/wiki/Pine_Tree_Forest) | 10K | 16.2K | 26.4K | 42.8K | 69.5K | 113K | 183K | 298K | 483K | 785K | 1.27M | 2.07M | 3.36M | - | - | 14.4M | - | - | - | - |
| [Mountain Top Field](/wiki/Mountain_Top_Field) | 10K | 20.7K | 42.8K | 88.6K | 183K | 379K | 785K | 1.62M | 3.36M | 6.95M | 14.4M | - | - | - | - | - | - | 1.13B | - |
| [Coconut Field](/wiki/Coconut_Field) | 25K | 61.9K | 153K | 379K | 937K | 2.32M | 5.74M | 14.2M | 35.2M | 87M | 215M | 533M | 1.32B | 3.26B | 8.07B | 20B | 49.4B | 122B | 303B | 749B |
| [Pepper Patch](/wiki/Pepper_Patch) | 25K | 61.9K | 153K | 379K | 937K | 2.32M | 5.74M | 14.2M | 35.2M | 87M | 215M | 533M | 1.32B | 3.26B | 8.07B | 20B | 49.4B | 122B | 303B | 749B |
| [Hub Field](/wiki/Hub_Field) | 250 | 450 | 800 | 1.43K | 2.56K | 4.57K | 8.17K | 14.6K | 26.1K | 46.7K | 83.6K | 149K | 267K | 478K | - | 1.53M | 2.73M | - | - | 15.6M |

## Petal Buffs and Types

When a bloom explodes, it releases petals that scatter in a ring around its position. Collecting these petals grants a stack of the corresponding petal buff and honey, with the amount scaling based on the bloom's level and field. While petals are randomized, their chances are altered depending on the field they originate from. Notably, petals collected in the [Hub Field](/wiki/Hub_Field) have nearly equal probabilities.

Each petal provides a temporary boost corresponding to its color, functioning similarly to [Jelly Bean](/wiki/Jelly_Beans) boosts. These boosts can stack up to 100 times, with each individual stack lasting 10 seconds. Every single stack grants at least +40% [Unique Instant Conversion](/wiki/Instant_Conversion).

| Petal Type | Fields | Min Boost | Max Boost |
| :---: | :---: | :---: | :---: |
| **Red Petal** | Mushroom Field, Strawberry Field, Rose Field, Mountain Top Field, Pepper Patch, Spider Field (Rare), Cactus Field (Partial, Rare), Clover Field, Hub Field | 1.25x [Red Pollen] +40% [Unique Instant Conversion] | 2x [Red Pollen] +60% [Unique Instant Conversion] |
| **Blue Petal** | Blue Flower Field, Clover Field, Bamboo Field, Stump Field, Pine Tree Forest, Mountain Top Field, Cactus Field (Partial, Rare), Pineapple Patch (Partial, Very Rare), Coconut Field (Partial, Very Rare), Hub Field | 1.25x [Blue Pollen] +40% [Unique Instant Conversion] | 2x [Blue Pollen] +60% [Unique Instant Conversion] |
| **White Petal** | Dandelion Field, Mushroom Field, Blue Flower Field, Clover Field, Strawberry Field, Spider Field, Bamboo Field, Sunflower Field (Partial), Pineapple Patch (Partial), Mountain Top Field (Partial), Coconut Field, Hub Field | 1.25x [White Pollen] +40% [Unique Instant Conversion] | 2x [White Pollen] +60% [Unique Instant Conversion] |
| **Scarlet Petal** | Rose Field (Partial, Uncommon), Mountain Top Field (Partial, Uncommon), Pepper Patch, Hub Field | 2x [Flames Pollen] +40% [Unique Instant Conversion] | 3x [Flames Pollen] +60% [Unique Instant Conversion] |
| **Cyan Petal** | Blue Flower Field (Rare), Bamboo Field, Stump Field, Pumpkin Patch, Cactus Field (Partial), Mountain Top Field (Partial, Uncommon), Coconut Field (Partial), Pineapple Patch, Hub Field | 2x [Bubble Pollen] +40% [Unique Instant Conversion] | 3x [Bubble Pollen] +60% [Unique Instant Conversion] |
| **Grey Petal** | Coconut Field, Pumpkin Patch (Partial), Dandelion Field (Uncommon), Spider Field (Uncommon), Rose Field (Uncommon), Strawberry Field (Partial, Rare), Stump Field (Rare), Hub Field | 2x Mark Ability Pollen +40% [Unique Instant Conversion] | 3x Mark Ability Pollen +60% [Unique Instant Conversion] |
| **Black Petal** | Dandelion Field (Uncommon), Spider Field, Cactus Field, Pine Tree Forest (Rare), Mushroom Field (Partial, Rare), Bamboo Field (Partial, Rare), Rose Field (Partial, Rare), Mountain Top Field (Partial, Rare), Hub Field | 2x [Bomb Pollen] +40% [Unique Instant Conversion] | 3x [Bomb Pollen] +60% [Unique Instant Conversion] |
| **Yellow Petal** | Sunflower Field, Blue Flower Field, Pineapple Patch, Pumpkin Patch, Mountain Top Field (Partial, Uncommon), Bamboo Field (Partial, Uncommon), Hub Field | 2x [Tool Pollen] +40% [Unique Instant Conversion] | 3x [Tool Pollen] +60% [Unique Instant Conversion] |
| **Green Petal** | Clover Field, Strawberry Field (Partial, Rare), Cactus Field, Pineapple Patch, Pine Tree Forest (Partial, Rare), Pumpkin Patch, Pepper Patch (Partial, Uncommon), Spider Field (Partial, Rare), Hub Field | +1% [Critical Chance] +40% [Unique Instant Conversion] | +10% [Critical Chance] +60% [Unique Instant Conversion] |
| **Pink Petal** | Strawberry Field, Mountain Top Field (Partial, Uncommon), Sunflower Field (Partial, Rare), Pepper Patch (Partial), Coconut Field (Partial), Hub Field | 2x [Bee Gather Pollen] +40% [Unique Instant Conversion] | 3x [Bee Gather Pollen] +60% [Unique Instant Conversion] |
| **Violet Petal** | Clover Field (Partial), Blue Flower Field (Partial, Very Rare), Rose Field (Rare), Strawberry Field (Partial, Rare), Stump Field (Partial, Rare), Mushroom Field (Partial, Rare), Bamboo Field (Partial, Rare), Pineapple Patch (Partial), Cactus Field (Partial), Coconut Field (Rare), Hub Field | +5% [Super-Crit Chance] +40% [Unique Instant Conversion] | +10% [Super-Crit Chance] +60% [Unique Instant Conversion] |
| **Merigold Petal** | Sunflower Field (Uncommon), Clover Field (Partial, Rare), Pineapple Patch (Partial, Very Rare), Mountain Top Field (Partial, Rare), Pepper Patch (Partial, Very Rare) | +70% [Unique Instant Conversion] | +90% [Unique Instant Conversion] |
| **Periwinkle Petal** | Pepper Patch (Partial, Rare), Hub Field, Coconut Field (Partial, Very Rare), Stump Field (Very Rare) | 1.25x Mythic Bee Pollen +40% [Unique Instant Conversion] | 1.5x Mythic Bee Pollen +60% [Unique Instant Conversion] |

## Sounds
*   [PetalCollect.wav](https://bee-swarm-simulator.fandom.com/wiki/File:PetalCollect.wav) (Collection sound)
*   [BloomSpawn.wav](https://bee-swarm-simulator.fandom.com/wiki/File:BloomSpawn.wav) (Spawning sound)

## Trivia
*   The Merigold Petal is misspelled throughout the game; the correct spelling should be 'Marigold'. This issue also affects the [Merigold Jelly Bean](/wiki/Jelly_Beans#Types_and_Effects). The "Festive Fetching Frolic" quest given by [Bee Bear](/wiki/Bee_Bear) for Beesmas 2025 used the correct spelling prior to the [2026-01-16 update](/wiki/Updates#2026-01-16).
*   Unique among petals, Merigold, Scarlet, Violet, and Periwinkle Petals feature glitter-like particles when falling.