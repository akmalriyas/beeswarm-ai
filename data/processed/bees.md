# Bees

Bees are a core feature of Bee Swarm Simulator. They follow the player, automatically collect pollen from fields, and defend the beekeeper against mobs and bosses. Most bees produce Ability Tokens upon returning to the hive, where they convert collected pollen into Honey—the primary currency used in shops.

## Mechanics and Behavior

**Energy and Sleep:** Bees require energy to work. When a bee runs out of energy, it returns to the hive to sleep for approximately 15 seconds before resuming its duties. The player receives a notification when this occurs (e.g., "[Bee's name] is out of energy! It's going to sleep.").

**Growth and Leveling:** Bees gather pollen, fight mobs, and consume treats. Their bond with the Beekeeper grows, increasing their level once certain thresholds are met. Higher-level bees can collect and convert more pollen into honey, possess greater working energy (with exceptions), and attack higher-level mobs.

**Hatching and Transformation:**
*   Bees hatch from eggs. The potential rarity of a bee is determined by the rarity of the egg (e.g., a Gold Egg can hatch an Epic, Legendary, or Mythic bee).
*   The type of an already-hatched bee can be changed by applying Royal Jelly or hatching it from another egg.

**Hive Management:**
*   Initially, the hive has 25 default Hive Slots. Players can expand this limit by purchasing additional slots at the Mountain Top Shop. While these slots increase in price exponentially, they allow for a maximum of 50 bees.
*   It is possible to exceed the 50-bee limit using temporary mechanics such as Onett's Lid Art, Honeyday Candles, Gummy Siege, or through Spicy Bee's Inferno ability.

**Bee Rarities and Types:**
There are currently 46 discoverable bee types. The rarities include: Common, Rare, Epic, Legendary, Mythic, and Event bees.

### Gifted Bees
A gifted bee is a variant with improved stats that grants the hive or player a bonus (which cannot stack). Most Gifted Event bees have enhanced abilities, such as Photon Bee's Beamstorm.

The chance of obtaining a gifted bee varies by rarity:
*   **Rare:** 1/8000 (0.0125%) when feeding its favorite treat.
*   **Epic:** 1/10000 (0.01%).
*   **Legendary & Common:** 1/12000 (0.0083%).
*   **Mythic:** 1/24000 (0.004%).

Additionally, gifted bees can be obtained:
*   With a 1/287 chance when using Royal Jelly or hatching from a Basic Egg.
*   Guaranteed by feeding them a Star Treat with a Star Jelly, or hatching one from a star egg.
*   From Gingerbread Bears (1% chance) and Aged Gingerbread Bears (1.1% chance).

## Bee Stats Table

| Name | Rarity | Color | Energy | Speed | Attack | Gather Amount | Gather Speed | Conversion Amount | Conversion Speed | Other Stats | Gifted Hive Bonus | Tokens | Passive Abilities | Likes | Dislikes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Basic Bee** | Common | Colorless | 20 | 14 | 1 | 10 Pollen | 4 s | 80 Honey | 4 s | x1.2 Pollen | - | - | * Sunflower Field, Clover Field, Mountain Top Field | * Spider Field |
| **Bomber Bee** | Rare | Colorless | 20 | 15.4 | 2 | 10 Pollen | 4 s | 120 Honey | 4 s | x1.1 Bomb Pollen | - | Buzz Bomb | * Dandelion Field, Cactus Field | * Pumpkin Patch |
| **Brave Bee** | Rare | Colorless | 30 | 16.8 | 5 | 10 Pollen | 4 s | 200 Honey | 4 s | +1 Bee Attack | - | - | * Spider Field, Clover Field | * Dandelion Field |
| **Bumble Bee** | Rare | Blue | 50 | 10.5 | 1 | 18 Pollen | 4 s | 80 Honey | 4 s | x1.1 Capacity | - | Blue Bomb | * Blue Flower Field, Pine Tree Forest, Stump Field | * Mushroom Field |
| **Cool Bee** | Rare | Blue | 20 | 14 | 2 | 10 Pollen | 3 s | 120 Honey | 4 s | x1.1 Blue Pollen | - | Blue Boost | * Bamboo Field, Pine Tree Field | * Strawberry Field |
| **Hasty Bee** | Rare | Colorless | 20 | 19.6 | 1 | 10 Pollen | 3 s | 80 Honey | 3 s | +15% Player Movespeed | - | Haste | * Sunflower Field, Cactus Field | * Pumpkin Patch, Stump Field |
| **Looker Bee** | Rare | Colorless | 20 | 14 | 1 | 13 Pollen | 4 s | 160 Honey | 4 s | +25% Critical Power | - | Focus | * Clover Field, Mountain Top Field | * Sunflower Field |
| **Rad Bee** | Rare | Red | 20 | 14 | 1 | 13 Pollen | 4 s | 80 Honey | 3 s | x1.1 Red Pollen | - | Red Boost | * Rose Field, Mushroom Field | * Pine Tree Forest |
| **Rascal Bee** | Rare | Red | 20 | 16.1 | 3 | 10 Pollen | 4 s | 80 Honey | 4 s | x1.25 Red Bomb Pollen | - | Red Bomb | * Rose Field, Mushroom Field | * Pine Tree Forest |
| **Stubborn Bee** | Rare | Colorless | 20 | 11.9 | 2 | 10 Pollen | 4 s | 80 Honey | 3 s | +15% Ability Token Lifespan | - | Pollen Mark | * Dandelion Field, Pineapple patch | * Rose Field |
| **Bubble Bee** | Epic | Blue | 20 | 16.1 | 3 | 10 Pollen | 4 s | 160 Honey | 4 s | x1.25 Bubble Pollen | Blue Bomb | Gathering Bubbles | * Blue Flower Field, Pine Tree Forest | * Strawberry Field |
| **Bucko Bee** | Epic | Blue | 30 | 15.4 | 5 | 17 Pollen | 4 s | 80 Honey | 3 s | +20% Blue Field Capacity | - | Blue Boost | * Pine Tree Forest, Bamboo Field, Blue Flower Field | * Rose Field, Strawberry Field |
| **Commander Bee** | Epic | Colorless | 30 | 14 | 4 | 15 Pollen | 4 s | 80 Honey | 4 s | +3% Critical Chance | - | Buzz Bomb, Focus | * Cactus Field, Spider Field | * Dandelion Field |
| **Demo Bee** | Epic | Colorless | 20 | 16.8 | 3 | 10 Pollen | 4 s | 200 Honey | 4 s | x1.25 Buzz Bomb Pollen | - | Buzz Bomb+ | * Cactus Field, Dandelion Field | * Rose Field |
| **Exhausted Bee** | Epic | Colorless | Unlimited | 10.5 | 1 | 10 Pollen | 4.6 s | 240 Honey | 4 s | +20% White Field Capacity | Buzz Bomb, Token Link | - | * Sunflower Field, Dandelion Field, Stump Field | * Cactus Field |
| **Fire Bee** | Epic | Red | 25 | 11.2 | 4 | 10 Pollen | 4 s | 80 Honey | 4 s | x1.25 Flame Pollen | Red Bomb+ | Gathering Flames | * Mushroom Field, Strawberry Field | * Pine Tree Forest |
| **Frosty Bee** | Epic | Blue | 25 | 11.2 | 1 | 10 Pollen | 4 s | 80 Honey | 4 s | x1.25 Blue Bomb Pollen | Blue Bomb+ | Blue Boost | * Blue Flower Field, Mountain Top Field | * Mushroom Field |
| **Honey Bee** | Epic | Colorless | 20 | 14 | 1 | 10 Pollen | 4 s | 360 Honey | 2 s | x1.5 Honey From Tokens | Honey Gift, Honey Mark | - | * Mountain Top Field, Pumpkin Patch | * Spider Field |
| **Rage Bee** | Epic | Red | 20 | 15.4 | 4 | 10 Pollen | 4 s | 80 Honey | 4 s | +10% Bee Attack | Token Link, Rage | - | * Rose Field, Spider Field | * Blue Flower Field |
| **Riley Bee** | Epic | Red | 25 | 15.4 | 5 | 10 Pollen | 2 s | 140 Honey | 4 s | +20% Red Field Capacity | Red Boost | - | * Rose Field, Strawberry Field, Mushroom Field | * Pine Tree Forest, Bamboo Field |
| **Shocked Bee** | Epic | Colorless | 20 | 19.6 | 2 | 10 Pollen | 4 s | 80 Honey | 2 s | -50% Sleep Time | Haste, Token Link | - | * Spider Field, Pineapple Patch | * Mushroom Field |
| **Baby Bee** | Legendary | Colorless | 15 | 10.5 | 0 | 10 Pollen | 5 s | 80 Honey | 5 s | +25% Loot Luck | Baby Love | - | * Dandelion Field, Sunflower Field, Mushroom Field, Blue Flower Field | * Spider Field, Cactus Field, Pine Tree Forest, Rose Field, Stump Field |
| **Carpenter Bee** | Legendary | Colorless | 25 | 11.2 | 4 | 10 Pollen | 3 s | 120 Honey | 4 s | x1.25 Tool Pollen | Pollen Mark, Honey Mark+ | - | * Pine Tree Forest, Bamboo Field | * Mountain Top Field |
| **Demon Bee** | Legendary | Red | 20 | 10.5 | 8 | 35 Pollen | 4 s | 60 Honey | 4 s | +20% Instant Bomb Conversion | Red Bomb, Red Bomb+ | Gathering Flames+ | * Spider Field, Mushroom Field | * Mountain Top Field |
| **Diamond Bee** | Legendary | Blue | 20 | 14 | 1 | 10 Pollen | 4 s | 1,000 Honey | 4 s | x1.2 Convert Rate | Honey Gift+, Blue Boost | Shimmering Honey | * Blue Flower Field, Pineapple Patch | * Rose Field |
| **Lion Bee** | Legendary | Colorless | 60 | 19.6 | 9 | 20 Pollen | 4 s | 160 Honey | 2 s | +5% Gifted Bee Pollen | Buzz Bomb+ | - | * Pineapple Patch, Ant Field | * Clover Field |
| **Music Bee** | Legendary | Colorless | 20 | 16.1 | 1 | 16 Pollen | 4 s | 240 Honey | 4 s | +25% Pollen From Bee Gathering | Focus, Token Link, Melody | - | * Clover Field, Dandelion Field | * Cactus Field |
| **Ninja Bee** | Legendary | Blue | 20 | 21 | 4 | 10 Pollen | 2 s | 80 Honey | 3 s | +5% Bee Movespeed | Blue Bomb+, Haste | - | * Bamboo Field, Blue Flower Field | * Mushroom Field |
| **Shy Bee** | Legendary | Red | 40 | 18.2 | 2 | 10 Pollen | 2 s | 320 Honey | 4 s | +5% Bee Ability Pollen | Red Bomb, Red Boost | Nectar Lover | * Strawberry Field, Pumpkin Patch | * Pine Tree Forest |
| **Buoyant Bee** | Mythic | Blue | 60 | 14 | 3 | 15 Pollen | 5 s | 150 Honey | 3 s | x1.2 Capacity | Blue Bomb, Inflate Balloon, Surprise Party (Gifted) | Balloon Enthusiast | * Coconut Field, Mountain Top Field, Bamboo Field, Blue Flower Field | - |
| **Fuzzy Bee** | Mythic | Colorless | 50 | 11.9 | 3 | 100 Pollen | 6 s | 40 Honey | 6 s | x1.1 Bomb Power | Buzz Bomb+, Fuzz Bombs, Pollen Haze (Gifted) | Fuzzy Coat | * Pine Tree Forest, Dandelion Field | * Pepper Patch |
| **Precise Bee** | Mythic | Red | 40 | 11.2 | 8 | 20 Pollen | 4 s | 130 Honey | 4 s | +5% Critical Chance, +3% Super-Crit Chance | Target Practice | +3% Super-Crit Chance | Sniper | * Rose Field, Mountain Top Field | * Pine Tree Forest, Bamboo Field |
| **Spicy Bee** | Mythic | Red | 20 | 14 | 5 | 14 Pollen | 4 s | 200 Honey | 2 s | +25% Flame Duration | Rage, Inferno, Flame Fuel (Gifted) | Steam Engine | * Pepper Patch | * Stump Field |
| **Tadpole Bee** | Mythic | Blue | 10 | 11.2 | 1 | 10 Pollen | 6 s | 120 Honey | 4 s | +25% Bubble Duration | Blue Boost, Baby Love (Gifted), Summon Frog | Gathering Bubbles+ | * Pine Tree Forest, Stump Field | * Cactus Field |
| **Vector Bee** | Mythic | Colorless | 45.6 | 16.24 | 5 | 18 Pollen | 4 s | 144 Honey | 2.72 s | +15% Mark Duration | Pollen Mark+, Triangulate, Mark Surge (Gifted) | - | * Coconut Field, Spider Field | * Pineapple Patch |
| **Bear Bee** | Event | Colorless | 35 | 14 | 5 | 15 Pollen | 2 s | 200 Honey | 2 s | +10% Pollen | Bear Morph | - | * Pine Tree Forest, Pumpkin Patch | * Blue Flower Field |
| **Cobalt Bee** | Event | Blue | 35 | 18.2 | 6 | 10 Pollen | 4 s | 120 Honey | 3 s | +15% Instant Blue Conversion | Blue Pulse, Blue Bomb Sync | - | * Pine Tree Forest, Clover Field | * Pineapple Patch |
| **Crimson Bee** | Event | Red | 35 | 18.2 | 6 | 10 Pollen | 4 s | 120 Honey | 3 s | +15% Instant Red Conversion | Red Pulse, Red Bomb Sync | - | * Rose Field, Clover Field | * Pineapple Patch |
| **Digital Bee** | Event | Colorless | 20 | 11.9 | 1 | 10 Pollen | 4 s | 80 Honey | 4 s | +1% Ability Duplication Chance | Glitch, Mind Hack, Map Corruption (Gifted) | Drive Expansion | * Coconut Field, Mountain Top Field, Dandelion Field | * Pine Tree Forest |
| **Festive Bee** | Event | Red | 20 | 16.1 | 1 | 40 Pollen | 4 s | 150 Honey | 1 s | x1.25 Convert Rate at Hive | Honey Mark, Red Bomb+, Festive Gift, Festive Mark (Festive Wreath) | - | * Pine Tree Forest, Mountain Top Field, Mushroom Field | * Blue Flower Field |
| **Gummy Bee** | Event | Colorless | 50 | 14 | 3 | 10 Pollen | 4 s | 700 Honey | 4 s | +5% Honey Per Pollen | Glob, Gumdrop Barrage | - | * Mountain Top Field, Pineapple Patch, Stump Field | * Pumpkin Patch |
| **Photon Bee** | Event | Colorless | Unlimited | 21 | 3 | 20 Pollen | 2 s | 240 Honey | 2 s | +5% Instant Conversion | Haste, Beamstorm | - | * Pumpkin Patch, Pineapple Patch | * Clover Field |
| **Puppy Bee** | Event | Colorless | 40 | 16.1 | 2 | 25 Pollen | 4 s | 280 Honey | 4 s | +20% Bond From Treats | Puppy Love, Fetch / Reindeer Fetch (Reindeer Antlers), Focus (Reindeer Antlers) | - | * Clover Field, Pumpkin Field | * Rose Field |
| **Tabby Bee** | Event | Colorless | 28 | 16.1 | 4 | 10 - 110 Pollen | 4 s | 160 - 1,760 Honey | 3 s | +50% Critical Power | Scratch, Tabby Love | - | * Clover Field, Spider Field | * Cactus Field |
| **Vicious Bee** | Event | Blue | 50 | 17.5 | 8 | 10 Pollen | 4 s | 80 Honey | 4 s | -15% Monster Respawn Time | Blue Bomb+, Impale | - | * Rose Field, Cactus Field | * Dandelion Field |
| **Windy Bee** | Event | Colorless | 20 | 19.6 | 3 | 10 Pollen | 3 s | 180 Honey | 2 s | +15% Instant White Conversion, x2 Boosts From Clouds | White Boost, Rain Cloud, Tornado | - | * Coconut Field, Dandelion Field | * Strawberry Field, Bamboo Field |

## Summoned Bees
Summoned bees are temporary entities that function like regular bees until they despawn. They collect pollen and convert it into honey using a random hive slot. Unlike permanent bees, summoned bees have unlimited energy until despawning, do not return to the hive if the player dies, and their gifted status does not grant a hive bonus or contribute to average hive level.

**Obtaining Summoned Bees:**

| Summoner | Bees Generated | Duration | Notes |
| :--- | :--- | :--- | :--- |
| Spicy Bee's Inferno ability | 2 Fire Bees (Level = Summoner Level - 2) | 15s (+1s per level) | |
| Onett's Lid Art | Bumble Bee (Level 20), Baby Bee (Level 1), and one random bee from the pool below. | 30 minutes | Random Pool: Lion, Music, Cobalt, Crimson, Festive, Tabby Bees. |
| Honeyday Candles | Three bees from the following pool. | 30 minutes | Level 10; decreased chance for higher rarities. Pool: Fire, Demon, Spicy Bees. |
| Gummy Beacon | 3 Gummy Bees (Level 8-20) | 30 minutes | |
| Honey Wreath | 1 Honey Bee (Level 20) | 5 minutes | Requires completion of the Honey Bee's Beesmas quest. |

## Trivia and Lore

*   The Mythic bee type was the first and only rarity added in an update.
*   Buoyant Bee is the only bee that dislikes no fields.
*   If a player experiences slow internet, bees are more likely to be slower at fighting mobs, making honey, and collecting pollen.
*   When converting honey, if the player moves too far from their hive pad, the conversion stops. However, minor movements do not interrupt the process. Moving closer to the hive increases conversion speed by reducing travel time.
*   If a player gets too far from their bees, they will fly toward the player, ignoring any flowers or mobs in their path.
*   When sleeping in a Hive Slot, bees emit faint "Z" particles until they wake up.
*   The higher a bee's level, the more effective it is at attacking, converting, and collecting. The average attack of a bee is approximately 3.
*   All event bees dislike only one field, with Windy Bee being an exception (disliking two).
*   A white sparkle indicates a token production; green sparkles indicate critical pollen collection or critical damage.
*   The Marshmallow Bee is the sole "item bee."
*   Legendary and Mythic bees are capable of activating special pads: Legendary for Honeystorm and Special Sprout Summoner, and Mythic for Mythic Meteor Shower Summoner.
*   Hive slot colors correspond to rarity: Bronze (Common), White (Rare), Yellow (Epic), Light Blue (Legendary), Purple (Mythic), Green (Event).
*   A bee's face color in its hive slot matches its body color (red bees have red faces, blue bees have blue faces, and colorless bees have black faces).

***

**Bee Performance Extremes:**

**Highest Stats:**
*   **Base Attack:** Lion Bee (10). Precise Bee and Digital Bee (16) [Max Red Drives].
*   **Base Speed:** Ninja Bee and Photon Bee (21). Digital Bee (21.9) [Max Drives].
*   **Base Conversion:** Diamond Bee (250/sec).
*   **Base Energy:** Photon Bee and Exhausted Bee (Unlimited). Excluding unlimited, Lion Bee and Buoyant Bee (60).
*   **Base Gather Amount:** Fuzzy Bee (16.7/sec). Digital Bee (33.75/sec) [Max White Drives].
*   **Abilities:** Fuzzy Bee, Spicy Bee, Tadpole Bee, Buoyant Bee (4).

**Lowest Stats:**
*   **Base Attack:** Baby Bee (0). Basic Bee, Bumble Bee, Hasty Bee, Looker Bee, Rad Bee, Diamond Bee, Music Bee, Tadpole Bee, Digital Bee, and Festive Bee (1).
*   **Base Speed:** Baby Bee, Bumble Bee, Exhausted Bee, and Demon Bee (10.5).
*   **Base Conversion:** Fuzzy Bee (6.7/sec).
*   **Base Energy:** Tadpole Bee (10).
*   **Base Gather Amount:** Tadpole Bee (1.7/sec).
*   **Abilities:** Basic Bee and Brave Bee (0).