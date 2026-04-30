# Sprouts

A **sprout** is a plant that spawns in the center of a [field](Fields). Sprouts emit a bright yellow beacon reaching into the sky, and display a counter at their base representing the amount of [pollen](Pollen) required for harvest.

When players collect pollen, or when a [cloud](Clouds) is present on the field (requiring at least one player to be in the field for cloud growth), the pollen counter counts down, allowing the sprout to gradually grow taller. Once the pollen counter reaches zero, the sprout sends out a shockwave and scatters various tokens throughout the field. If no interaction occurs with a sprout for more than five minutes, it will despawn.

## Spawning Mechanics

Sprouts can spawn randomly across the map or be planted using [Magic Beans](Magic_Bean). They can also be summoned via the [Special Sprout Summoner](Special_Sprout_Summoner) near the [Red HQ](Red_HQ), provided the player has discovered all eight [Legendary Bee](Bees/Legendary) types. This summoning ability is available once every sixteen hours.

When a sprout spawns naturally, it broadcasts a server-wide message:
🌱A (Rarity) Sprout has appeared...🌱

If a player plants a sprout, the message reads:
🌱 {Username} has planted a (Rarity) Sprout...🌱

Specific spawn messages include:
*   **Sticker Sprouts in Hive Hub:** 🌱 Sticker Sprouts are about to spawn in the Hive Hub...🌱
*   **Sticker Sprout Spawned:** 🌱 A Sticker Sprout has spawned in the Hive Hub...🌱

Sprouts cannot spawn or be planted within the [Ant Field](Ant_Field).

## Variants and Rarities

There are ten different variants of sprouts, each with unique characteristics:

| Variant | Color/Appearance | Rarity | Notes |
| :--- | :--- | :--- | :--- |
| Sprout (Green) | Green | Common | Standard sprout. |
| Rare Sprout | Silver | Rare | |
| Epic Sprout | Gold | Very Rare | |
| Legendary Sprout | Teal | Extremely Rare | |
| Supreme Sprout | Luminescent green | Unfathomably Rare | Only type guaranteed to drop an egg. Glows. |
| Moon Sprout | Luminescent blue (day/night) | Common | Only available during nighttime. Glows. |
| Gummy Sprout | Translucent pink | Very Rare | The only translucent sprout. |
| Sticker Sprout | Rainbow, colors shifting | N/A | Spawns every 3 hours in the [Hub Field](Hub_Field), or rarely when planting a magic bean there. Grows without clouds (loses ~1M pollen per second). |
| Festive Sprout | White and Red stripes | N/A | Planted using [Festive Beans](Festive_Bean) or by [Onett](Onett_(Developer)). Has a red notification color. |
| Debug Sprout | Black | N/A | Can only be planted by [Onett](Onett). Does not drop honey tokens. Has a gray notification color. |

The amount of pollen required for harvest depends on both the sprout's rarity and the field it is located in.

## Drops and Harvest Statistics

### Location Specific Yields
The type of field affects the yield and specific items dropped:

*   **Red Fields:** Yield 4 times more [Strawberries](Strawberry) than other red fields. No [Blueberries](Blueberry) will spawn.
*   **Strawberry Field:** Yields twice as many [Strawberries](Strawberry) compared to sprouts in other red fields.
*   **Blue Fields:** Yields 6 times more [Blueberries](Blueberry) than any other field. No [Strawberries](Strawberry) will spawn.
*   **Sunflower Field:** Yields 7 times more [Sunflower Seeds](Sunflower_Seed).
*   **Pineapple Patch:** Yields 7 times more [Pineapples](Pineapple).
*   **35 Bee Zone (Windy Bee Gate):** Yields 20% more rewards, but requires significantly more pollen to pop.
*   **Coconut Field:** Drops [Coconuts](Coconut) and [Tropical Drinks](Tropical_Drink) in addition to standard treats.
*   **Other Fields:** May produce more regular [Treats](Treat) than other fields, depending on the specific field type.

### Harvest Table (Pollen Requirements & Tokens)
The higher the sprout tier, the more tokens spawn upon harvest.

| Sprout Type | Special Drops | Tickets | Royal Jellies | Treats | Honey | Pollen Range |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Common (Green)** | Crafting Materials | 1 | 1-3 | 1 | 400 | 50,000 to 2,500,000 |
| **Rare (Silver)** | Silver Egg, Star Jellies, Crafting Materials | 1 | 1-3 | 3 | 2,000 | 250,000 to 12,500,000 |
| **Epic (Gold)** | Gold Egg, Star Jellies, Crafting Materials | 1 | 1-3 | 5 | 7,500 | 2,500,000 to 125,000,000 |
| **Legendary (Teal)** | Diamond Egg, Star Jellies, Crafting Materials | - | 1-5 | 10 | 10,000 | 10,000,000 to 500,000,000 |
| **Gummy (Pink)** | Gumdrops, Glues, Glitter, Neonberry | X | X | X | 4,500 | 1,000,000 to 50,000,000 |
| **Moon (Blue)** | Glitter, Moon Charms, Star Jelly, Neonberry | X | X | 1 | 1,500 | 500,000 to 25,000,000 |
| **Supreme (Green)** | Diamond Egg, Star Jellies, Crafting Materials | 1 | 1-10 | 30 | 10,000 | 15,000,000 to 750,000,000 |
| **Debug (Black)** | Bitterberries, Neonberries, Atomic Treats | X | X | X | X | 10,000,000 to 30,000,000 |
| **Festive (Stripes)** | Festive Blessing, Beesmas Cheer, Gumdrops, Snowflakes, Gingerbread Bears, Crafting Materials | 1 | 1 | 15 | 15,000 | 1,000,000 to 50,000,000 |
| **Sticker Sprout (Rainbow)** | Silver Egg, Gifted Silver Egg, Diamond Egg, Gifted Diamond Egg, Star Egg, Stickers, Waxes, Sticker Planters, Star Jellies, Crafting Materials | 1-5 | 1 | 10 | 5,000 | 1,000,000,000 |

*Note: An 'X' indicates that the specified sprout does not spawn that item.*
*Crafting Materials include Red Extracts, Blue Extracts, Oils, Enzymes, and Glitter.*

## Gameplay Tips for Token Collection

To maximize token collection efficiency before sprouts despawn (5 minutes):

**Speed Buffs:**
*   **Oil:** Grants 1.2x player movespeed.
*   **Hasty Guard:** Equips grant 1.1x player movespeed.
*   **Haste Buff:** Can increase movespeed up to 2x. Sources include:
    *   [Haste producing bees](Ability_Tokens#Haste).
    *   Honey, Treat, Strawberry, and Blueberry Dispensers (5 stacks of Haste each).
    *   Royal Jelly Dispenser (10 stacks of Haste).
    *   Free Royal Jelly Dispenser (1 stack of Haste+).
*   **Coconut Clogs/Gummy Boots:** Allows players to trigger a short burst of [Coconut Haste Surge] when hit by a coconut.
*   **Bear Bee's Bear Morph ability:** Significantly increases player movespeed.

**Token Collection Methods:**
*   [Tadpole Bee](Tadpole_Bee) and [Boxes-O-Frogs](Box-O-Frogs) can summon frogs that collect sprout tokens.
*   The [Star Saw](Passive_Abilities#Star_Saw) passive ability collects massive amounts of tokens.
*   [Windy Bee's Tornado ability](Ability_Tokens#Tornado) also collects large quantities of tokens.
*   [Cub Buddies](Cub_Buddy#Skins) can collect sprout tokens.

**Sticker Sprout Strategy:**
When collecting Sticker Sprouts, focus on staying in one location and gathering loot within immediate reach, as distant items are likely to be claimed by other players first.

## Trivia & Mechanics Deep Dive

*   **Planting Authority:** [Onett](Onett_(Developer)) can plant sprouts server-wide under unique names (e.g., Festive, Debug, Gummy).
*   **Token Collection Rules:** If a player who planted the sprout leaves before it pops, the sprout will not drop any items.
*   **Pollen Visibility:** If a sprout spawns before a player joins the server, its pollen counter is invisible to that player, though they can still pop it.
*   **Despawn Mechanics:** Sprouts despawn if left un-interacted with for 5 minutes. Festive sprouts planted by players will also despawn if the planter leaves the server.
*   **Sticker Sprout Growth:** Sticker Sprouts are unique as they grow on their own without requiring clouds, continuously losing approximately 1 million pollen per second in the Hub Field.
*   **Notification Colors:** While most sprout notifications are gold, specific variants have distinct colors: Gummy (light purple), Supreme/Moon/Debug (gray), Festive (red), and Sticker Sprouts (rainbow).
*   **Historical Context:** Sprouts were originally called "Seedlings" until the 2019-12-23 update. The [Special Sprout Summoner] was previously known as the "Sprout Summoner." Supreme Sprouts were formerly named "Mythical Sprouts."
*   **Egg Drops:** If a player completes the [Stick Bug's Egg Hunt 2019 Quest](Stick_Bug#Egg_Hunt_2019_Quest), Stick Bug will spawn an Epic, Legendary, and a Supreme Sprout.

## Gallery

*(Image gallery content retained for visual reference)*