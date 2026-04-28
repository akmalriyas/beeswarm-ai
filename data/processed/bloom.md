# Bloom

Blooms are passive, field-based entities that can spawn naturally or be summoned using a [Bloom Shaker](/wiki/Bloom_Shaker). They first appeared in the 2025-12-25 update. These large flowers are adorned with colored petals and serve as sources of buffs and honey.

A Bloom's maximum petal count scales with its level. When collected, petals grant their respective color buff and honey equal to half of the bloom's original HP. Even if a bloom's health is under 100 pollen, collecting petals guarantees at least 50 honey.

## Mechanics

### Spawning and Progression
When a Bloom is first created, it has a 20-second timer and a set "base" petal color, which usually constitutes the majority of its petals. Once the required pollen requirements are met, the bloom pops, scattering all its petals in a circular pattern. Upon popping, a new "child" bloom of a higher level and identical base color spawns. Child blooms cease spawning one minute after the original parent bloom appeared.

Blooms have multiple levels; upon defeat, they respawn at a higher level, similar to [Puffshrooms](/wiki/Puffshroom). A Bloom has a small chance to be "mutated" when created, meaning one or more petals may be a different color than the base color. As the bloom's level increases, the chance of mutation also increases. Mutation in a parent bloom does not affect the probability of its child blooms being mutated.

### Interaction
Hitting Blooms with a Petal Shuriken (from a [Petal Wand](/wiki/Petal_Wand) or [Petal Belt](/wiki/Petal_Belt)) causes them to spawn bonus petals. This action also deals 20% of the remaining HP and 5% of the Bloom's maximum HP.

## Levels and Stats

### Petals per Level
The number of petals a bloom can have is capped at 11 for level 20 and above. For levels below 20, the petal count can be calculated using the formula: $\lfloor (level \times 2) \div 5 \rfloor + 3$.

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

### Health (Pollen Required)
A Bloom's health depends heavily on both its level and the field it spawns in. The following table shows the pollen required per level for various fields:

| Field | Lvl 1 | Lvl 2 | Lvl 3 | Lvl 4 | Lvl 5 | Lvl 6 | Lvl 7 | Lvl 8 | Lvl 9 | Lvl 10 | Lvl 11 | Lvl 12 | Lvl 13 | Lvl 14 | Lvl 15 | Lvl 16 | Lvl 17 | Lvl 18 | Lvl 19 | Lvl 20 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [Sunflower Field](/wiki/Sunflower_Field) | 30 | 40 | 70 | 130 | 220 | 380 | 650 | 1.11K | 1.91K | 3.29K | 5.65K | 9.72K | 16.7K | 28.8K | - | - | 146K | - | - | - |
| [Dandelion Field](/wiki/Dandelion_Field) | 50 | 90 | 170 | 320 | 590 | 1.1K | 2.03K | 3.77K | 7K | 13K | 24.1K | 44.6K | 82.8K | 154K | 285K | 528K | - | - | 3.37M | - |
| [Mushroom Field](/wiki/Mushroom_Field) | 50 | 90 | 170 | 320 | 590 | 1.1K | 2.03K | 3.77K | 7K | 13K | 24.1K | 44.6K | 82.8K | 154K | 285K | 528K | - | - | 3.37M | - |
| [Clover Field](/wiki/Clover_Field) | 80 | 150 | 290 | 580 | 1.15K | 2.27K | 4.48K | 8.86K | 17.5K | 34.6K | 68.5K | 135K | 268K | 530K | 1.05M | 2.07M | 4.09M | - | 16M | - |
| [Blue Flower Field](/wiki/Blue_Flower_Field) | 150 | 250 | 430 | 730 | 1.24K | 2.1K | 3.55K | 6.02K | 10.2K | 17.3K | 29.3K | 49.8K | 84.1K | - | - | - | - | - | - |
| [Bamboo Field](/wiki/Bamboo_Field) | 250 | 600 | 1.43K | 3.42K | 8.17K | 19.5K | 46.7K | 112K | 267K | 639K | 1.53M | 3.65M | 20.9M | - | - | - | - | 1.63B | - |
| [Strawberry Field](/wiki/Strawberry_Field) | 250 | 600 | 1.43K | 3.42K | 8.17K | 19.5K | 46.7K | 112K | 267K | 639K | 1.53M | 3.65M | 20.9M | - | - | - | - | 1.63B | - |
| [Spider Field](/wiki/Spider_Field) | 1K | 2.07K | 4.28K | 8.86K | 18.3K | 37.9K | 78.5K | 162K | 336K | 695K | 1.44M | 2.98M | 6.16M | - | 26.4M | - | 113M | - | - |
| [Pineapple Patch](/wiki/Pineapple_Patch) | 500 | 1.13K | 2.57K | 5.81K | 13.2K | 29.8K | 67.6K | 153K | 347K | 785K | 1.78M | 4.03M | 9.13M | 20.7M | 46.9M | 106M | 240M | 545M | 1.23B | 2.8B |
| [Stump Field](/wiki/Stump_Field) | 5K | 12.3K | 30K | 73.6K | 180K | 442K | 1.08M | 2.66M | 6.51M | 16M | 39.1M | 95.9M | 235M | 576M | 1.41B | 3.46B | - | 20.8B | 51B | 125B |
| [Rose Field](/wiki/Rose_Field) | 50 | 210 | 890 | 3.77K | 15.9K | 67.4K | 285K | 1.2M | 5.09M | 21.5M | 90.9M | 384M | 1.62B | 6.86B | 29B | - | 518B | 2.19T | - | 39.1T |
| [Cactus Field](/wiki/Cactus_Field) | 500 | 1.13K | 2.57K | 5.81K | 13.2K | 29.8K | 67.6K | 153K | 347K | 785K | 1.78M | 4.03M | 9.13M | 20.7M | - | 106M | 240M | - | 1.23B | - |
| [Pumpkin Patch](/wiki/Pumpkin_Patch) | 2.5K | 3.77K | 5.7K | 8.6K | 13K | 19.6K | 29.6K | 44.6K | 67.4K | 102K | 154K | 232K | 350K | 528K | 797K | 1.2M | 1.82M | 2.74M | 4.14M | - |
| [Pine Tree Forest](/wiki/Pine_Tree_Forest) | 10K | 16.2K | 26.4K | 42.8K | 69.5K | 113K | 183K | 298K | 483K | 785K | 1.27M | 2.07M | 3.36M | - | - | 14.4M | - | - | - |
| [Mountain Top Field](/wiki/Mountain_Top_Field) | 10K | 20.7K | 42.8K | 88.6K | 183K | 379K | 785K | 1.62M | 3.36M | 6.95M | 14.4M | - | - | - | - | - | - | 1.13B | - |
| [Coconut Field](/wiki/Coconut_Field) | 25K | 61.9K | 153K | 379K | 937K | 2.32M | 5.74M | 14.2M | 35.2M | 87M | 215M | 533M | 1.32B | 3.26B | 8.07B | 20B | 49.4B | 122B | 303B | 749B |
| [Pepper Patch](/wiki/Pepper_Patch) | 25K | 61.9K | 153K | 379K | 937K | 2.32M | 5.74M | 14.2M | 35.2M | 87M | 215M | 533M | 1.32B | 3.26B | 8.07B | 20B | 49.4B | 122B | 303B | 749B |
| [Hub Field](/wiki/Hub_Field) | 250 | 450 | 800 | 1.43K | 2.56K | 4.57K | 8.17K | 14.6K | 26.1K | 46.7K | 83.6K | 149K | 267K | 478K | - | 1.53M | 2.73M | - | - | 15.6M |

## Petal Buffs and Effects

When a Bloom explodes, it releases petals that grant temporary buffs corresponding to their color. These boosts function similarly to [Jelly Bean](/wiki/Jelly_Beans) effects and can stack up to 100 times, with each individual stack lasting 10 seconds. Every stack grants at least +40% [Unique Instant Conversion](/wiki/Instant_Conversion).

Petals are randomized but have altered chances depending on the field. Notably, petals in the [Hub Field](/wiki/Hub_Field) have nearly equal probabilities.

| Petal Type | Fields | Min Boost | Max Boost |
| :---: | :--- | :--- | :--- |
| **Red Petal** | [Mushroom Field](/wiki/Mushroom_Field), [Strawberry Field](/wiki/Strawberry_Field), [Rose Field](/wiki/Rose_Field), [Mountain Top Field](/wiki/Mountain_Top_Field), [Pepper Patch](/wiki/Pepper_Patch), [Spider Field](/wiki/Spider_Field) (Rare), [Cactus Field](/wiki/Cactus_Field) (Partial, Rare), [Clover Field](/wiki/Clover_Field), [Hub Field](/wiki/Hub_Field) | 1.25x Red Pollen +40% Unique Instant Conversion | 2x Red Pollen +60% Unique Instant Conversion |
| **Blue Petal** | [Blue Flower Field](/wiki/Blue_Flower_Field), [Clover Field](/wiki/Clover_Field), [Bamboo Field](/wiki/Bamboo_Field), [Stump Field](/wiki/Stump_Field), [Pine Tree Forest](/wiki/Pine_Tree_Forest), [Mountain Top Field](/wiki/Mountain_Top_Field), [Cactus Field](/wiki/Cactus_Field) (Partial, Rare), [Pineapple Patch](/wiki/Pineapple_Patch) (Partial, Very Rare), [Coconut Field](/wiki/Coconut_Field) (Partial, Very Rare), [Hub Field](/wiki/Hub_Field) | 1.25x Blue Pollen +40% Unique Instant Conversion | 2x Blue Pollen +60% Unique Instant Conversion |
| **White Petal** | [Dandelion Field](/wiki/Dandelion_Field), [Mushroom Field](/wiki/Mushroom_Field), [Blue Flower Field](/wiki/Blue_Flower_Field), [Clover Field](/wiki/Clover_Field), [Strawberry Field](/wiki/Strawberry_Field), [Spider Field](/wiki/Spider_Field), [Bamboo Field](/wiki/Bamboo_Field), [Sunflower Field](/wiki/Sunflower_Field) (Partial), [Pineapple Patch](/wiki/Pineapple_Patch) (Partial), [Mountain Top Field](/wiki/Mountain_Top_Field) (Partial), [Coconut Field](/wiki/Coconut_Field), [Hub Field](/wiki/Hub_Field) | 1.25x White Pollen +40% Unique Instant Conversion | 2x White Pollen +60% Unique Instant Conversion |
| **Scarlet Petal** | [Rose Field](/wiki/Rose_Field) (Partial, Uncommon), [Mountain Top Field](/wiki/Mountain_Top_Field) (Partial, Uncommon), [Pepper Patch](/wiki/Pepper_Patch), [Hub Field](/wiki/Hub_Field) | 2x Flames Pollen +40% Unique Instant Conversion | 3x Flames Pollen +60% Unique Instant Conversion |
| **Cyan Petal** | [Blue Flower Field](/wiki/Blue_Flower_Field) (Rare), [Bamboo Field](/wiki/Bamboo_Field), [Stump Field](/wiki/Stump_Field), [Pumpkin Patch](/wiki/Pumpkin_Patch), [Cactus Field](/wiki/Cactus_Field) (Partial), [Mountain Top Field](/wiki/Mountain_Top_Field) (Partial, Uncommon), [Coconut Field](/wiki/Coconut_Field) (Partial), [Pineapple Patch](/wiki/Pineapple_Patch), [Hub Field](/wiki/Hub_Field) | 2x Bubble Pollen +40% Unique Instant Conversion | 3x Bubble Pollen +60% Unique Instant Conversion |
| **Grey Petal** | [Coconut Field](/wiki/Coconut_Field), [Pumpkin Patch](/wiki/Pumpkin_Patch) (Partial), [Dandelion Field](/wiki/Dandelion_Field) (Uncommon), [Spider Field](/wiki/Spider_Field) (Uncommon), [Rose Field](/wiki/Rose_Field) (Uncommon), [Strawberry Field](/wiki/Strawberry_Field) (Partial, Rare), [Stump Field](/wiki/Stump_Field) (Rare), [Hub Field](/wiki/Hub_Field) | 2x Mark Ability Pollen +40% Unique Instant Conversion | 3x Mark Ability Pollen +60% Unique Instant Conversion |
| **Black Petal** | [Dandelion Field](/wiki/Dandelion_Field) (Uncommon), [Spider Field](/wiki/Spider_Field), [Cactus Field](/wiki/Cactus_Field), [Pine Tree Forest](/wiki/Pine_Tree_Forest) (Rare), [Mushroom Field](/wiki/Mushroom_Field) (Partial, Rare), [Bamboo Field](/wiki/Bamboo_Field) (Partial, Rare), [Rose Field](/wiki/Rose_Field) (Partial, Rare), [Mountain Top Field](/wiki/Mountain_Top_Field) (Partial, Rare), [Hub Field](/wiki/Hub_Field) | 2x Bomb Pollen +40% Unique Instant Conversion | 3x Bomb Pollen +60% Unique Instant Conversion |
| **Yellow Petal** | [Sunflower Field](/wiki/Sunflower_Field), [Blue Flower Field](/wiki/Blue_Flower_Field), [Pineapple Patch](/wiki/Pineapple_Patch), [Pumpkin Patch](/wiki/Pumpkin_Patch), [Mountain Top Field](/wiki/Mountain_Top_Field) (Partial, Uncommon), [Bamboo Field](/wiki/Bamboo_Field) (Partial, Uncommon), [Hub Field](/wiki/Hub_Field) | 2x Tool Pollen +40% Unique Instant Conversion | 3x Tool Pollen +60% Unique Instant Conversion |
| **Green Petal** | [Clover Field](/wiki/Clover_Field), [Strawberry Field](/wiki/Strawberry_Field) (Partial, Rare), [Cactus Field](/wiki/Cactus_Field), [Pineapple Patch](/wiki/Pineapple_Patch), [Pine Tree Forest](/wiki/Pine_Tree_Forest) (Partial, Rare), [Pumpkin Patch](/wiki/Pumpkin_Patch), [Pepper Patch](/wiki/Pepper_Patch) (Partial, Uncommon), [Spider Field](/wiki/Spider_Field) (Partial, Rare), [Hub Field](/wiki/Hub_Field) | +1% Critical Chance +40% Unique Instant Conversion | +10% Critical Chance +60% Unique Instant Conversion |
| **Pink Petal** | [Strawberry Field](/wiki/Strawberry_Field), [Mountain Top Field](/wiki/Mountain_Top_Field) (Partial, Uncommon), [Sunflower Field](/wiki/Sunflower_Field) (Partial, Rare), [Pepper Patch](/wiki/Pepper_Patch) (Partial), [Coconut Field](/wiki/Coconut_Field) (Partial), [Hub Field](/wiki/Hub_Field) | 2x Bee Gather Pollen +40% Unique Instant Conversion | 3x Bee Gather Pollen +60% Unique Instant Conversion |
| **Violet Petal** | [Clover Field](/wiki/Clover_Field) (Partial), [Blue Flower Field](/wiki/Blue_Flower_Field) (Partial, Very Rare), [Rose Field](/wiki/Rose_Field) (Rare), [Strawberry Field](/wiki/Strawberry_Field) (Partial, Rare), [Stump Field](/wiki/Stump_Field) (Partial, Rare), [Mushroom Field](/wiki/Mushroom_Field) (Partial, Rare), [Bamboo Field](/wiki/Bamboo_Field) (Partial, Rare), [Pineapple Patch](/wiki/Pineapple_Patch) (Partial), [Cactus Field](/wiki/Cactus_Field) (Partial), [Coconut Field](/wiki/Coconut_Field) (Rare), [Hub Field](/wiki/Hub_Field) | +5% Super-Crit Chance +40% Unique Instant Conversion | +10% Super-Crit Chance +60% Unique Instant Conversion |
| **Merigold Petal** | [Sunflower Field](/wiki/Sunflower_Field) (Uncommon), [Clover Field](/wiki/Clover_Field) (Partial, Rare), [Pineapple Patch](/wiki/Pineapple_Patch) (Partial, Very Rare), [Mountain Top Field](/wiki/Mountain_Top_Field) (Partial, Rare), [Pepper Patch](/wiki/Pepper_Patch) (Partial, Very Rare), [Hub Field](/wiki/Hub_Field) | +70% Unique Instant Conversion | +90% Unique Instant Conversion |
| **Periwinkle Petal** | [Pepper Patch](/wiki/Pepper_Patch) (Partial, Rare), [Hub Field](/wiki/Hub_Field), [Coconut Field](/wiki/Coconut_Field) (Partial, Very Rare), [Stump Field](/wiki/Stump_Field) (Very Rare) | 1.25x Mythic Bee Pollen +40% Unique Instant Conversion | 1.5x Mythic Bee Pollen +60% Unique Instant Conversion |

## Media and Gallery
*   **Sounds:** [PetalCollect.wav](/wiki/File:PetalCollect.wav), [BloomSpawn.wav](/wiki/File:BloomSpawn.wav)
*   **Visuals:** The wiki contains several images detailing the appearance of Blooms, their petal colors, and various buff effects.

## Trivia
*   The name "Merigold" is often misspelled throughout the game; the correct spelling should be 'Marigold'. This issue also affects the [Merigold Jelly Bean](/wiki/Jelly_Beans#Types_and_Effects). The quest "Festive Fetching Frolic," given by [Bee Bear](/wiki/Bee_Bear), used the correct spelling before the 2026-01-16 update.
*   Unique to others, Merigold, Scarlet, Violet, and Periwinkle Petals feature glitter-like particles when falling.