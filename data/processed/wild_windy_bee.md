# Wild Windy Bee

The **Wild Windy Bee** is a Mini-Boss that appears across various fields in the game. This guide details its mechanics, attacks, and rewards.

## General Information

| Attribute | Value | Notes |
| :--- | :--- | :--- |
| Type | Mini-Boss | A wild, powerful bee variant. |
| Base Health | 500 | Increases with level. |
| Contact Damage | 40 | Minimum damage is 1/0.5s; increases upon defeat and proximity to the tornado. |
| Battle Points | None | N/A |
| Level Range | 1 - No limit | Maximum level is typically 6, unless spawned by Onett (Developer). |

### Spawning Locations

The Wild Windy Bee normally spawns in:
*   Dandelion Field
*   Pineapple Patch
*   Pumpkin Patch
*   Mountain Top Field
*   Coconut Field

During the Beesmas event, it may also spawn in:
*   Clover Field
*   Spider Field
*   Bamboo Field
*   Pepper Patch

### Spawning Mechanics

1.  **Natural Spawn:** It can spawn naturally every two in-game Day/Night Cycles or via an offering to the Wind Shrine. If the dialogue from the Wind Shrine is, "A sudden breeze sweeps the {item} into the sky," a Wild Windy Bee will appear in a random field.
2.  **De-spawn Timer:** If the player does not interact with the cloud containing the bee within 3 minutes, it will de-spawn.
3.  **Quest Spawn:** It can be summoned by Spirit Bear's quests:
    *   "Tickle The Wind" (Level 20): Summons 3 Wild Windy Bees at Mountain Top Field.
    *   "Space Oblivion" (Level 24): Summons a single Wild Windy Bee.
    *   "Spring Out Of The Mountain" (Level 30): Summons a single Wild Windy Bee.

### Encountering the Bee

When a Wild Windy Bee spawns, players must locate a floating cloud over a field containing the bee. This cloud will be camouflaged and possess a distinct white trail. Touching the cloud initiates the fight.

**Server Notifications:**
*   **Start of Fight:** "☁️ (Player Username) found Windy Bee in the {field} Field! ☁️"
*   **Fleeing:** "☁️ Windy Bee is fleeing... ☁️"

The chimes on the Wind Shrine continuously moving from left to right indicate that a Wild Windy Bee is currently active on the map, either camouflaged or fighting.

## Attack Patterns

Wild Windy Bee utilizes two distinct attack patterns:

### 1. Tornado Summon
*   **Effect:** Summons three tornadoes that clear Pollen off the field and deal damage every 0.5 seconds.
*   **Damage:** Damage varies from 1 to 20, depending on proximity to the tornado and how many times the bee has been defeated.
*   **Scaling:** The duration and speed of the tornadoes increase with each defeat.
*   **Targeting:** This attack can damage other mobs present in the field.
*   **Cycle:** This attack occurs first and cycles after three Wind blows.

### 2. Gust of Wind
*   **Effect:** Forms a powerful gust of wind that flings players away within a rectangular area. It deals no damage but prevents affected players from dealing damage for a period.
*   **Warning:** A red attack indicator is displayed for approximately one second before the attack occurs.
*   **Direction/Size:** The direction depends on the bee's position and the location of a randomly targeted player. The size of the area is determined by the distance between the bee and the edge of the field it is looking toward. If no players are detected, the attack targets a random direction.
*   **Cycle:** This attack follows the tornado sequence.

## Rewards and Loot Mechanics

Upon defeat, Wild Windy Bee drops rewards and immediately moves to a new, random field (excluding the Hub Field, Ant Field, and Stump Field). It repeats this process for 5 minutes before fleeing.

### Post-Defeat Effects
*   **Cloud Drop:** A cloud is left in the center of the field that regrows flowers and grants +25% Pollen for 10 seconds (or +50% if a Gifted Windy Bee is present). This effect refreshes while standing under the cloud.
*   **Conversion Bonus:** It grants +10% Unique Instant Conversion.
*   **Loot Ring:** A ring of tokens appears underneath the bee, and each player receives loot proportional to the damage they dealt.

### Leveling and Drops
Every defeat increases the Wild Windy Bee's level, granting it more health (similar to Stick Bug). Higher levels also increase its chance of dropping Cloud Vials and rarer items.

**Loot Drop Rate:** The value and amount of drops are highly dependent on the damage distribution among players fighting the bee. Defeating it too many times in a single day significantly weakens drop quality (Law of Diminishing Marginal Utility).

### Health Formula
The health is calculated using the following formula:
$$\text{Health} = (\text{level}^2 \times 250) + 250$$

| Level | Health |
| :--- | :--- |
| 1 | 500 |
| 6 | 9,250 |
| 10 | 25,250 |
| 15 | 56,500 |
| 20 | 100,250 |
| 25 | 164,500 |

## Field Movement Pathing

After being defeated, the bee moves to a new field based on its current location. Below are examples of possible transitions:

*   **Sunflower Field** $\rightarrow$ Mushroom Field, Dandelion Field, Coconut Field, Rose Field
*   **Dandelion Field** $\rightarrow$ Clover Field, Rose Field, Sunflower Field, Blue Flower Field, Mushroom Field
*   **Mushroom Field** $\rightarrow$ Sunflower Field, Strawberry Field, Coconut Field, Spider Field, Dandelion Field
*   **Blue Flower Field** $\rightarrow$ Bamboo Field, Spider Field, Coconut Field, Clover Field
*   ... (All possible transitions are defined by the game's pathing system.)

## Combat Tips and Strategy

### Preparation
1.  **Pre-Fight:** Defeat tough mobs and bosses beforehand to ensure a smoother fight, especially the Coconut Crab and Mondo Chick.
2.  **Summoning Cost:** A cheap but reliable summoning method involves 5–10 Field Dice / 3–5 Oils / 5–10 Glue. Alternatives include 1 Star Jelly or 3–5 Glitters.

### Buffs and Gear
*   **Nectars:** Invigorating Nectar grants x1.01 - x1.10 Bee attack and provides 1% - 5% Bee Ability Rate (Motivating).
*   **Accessories:** Equip items that boost bee attack, such as the Fire Mask, Demon Mask, Coconut Clogs, or Gummy Boots. Stingers can provide an extra 1.5x bee attack if paired with a Vicious Bee.
*   **Movement/Crit Buffs:** Oils and Tropical Drinks grant 1.2x player and Bee Movespeed and +5% Critical Chance. Super Smoothies offer improved Movespeed, Bee Movespeed, Critical Chance, and Super-Crit Chance (though they are rare and expensive).

### In-Combat Tactics
*   **Token Stacks:** Build up Focus tokens before the fight to increase critical hit chances. Also, build a precision stack for Super-Crit chance (which is 33% stronger than a critical hit) and reduced cooldowns for Precise Bees. Melody can grant 100% critical power for 30 seconds.
*   **Evasion:** During the wind gust attack, move into an open space to avoid being flung away.
*   **Camouflage Exploitation:** Standing on decorations or ramps around the field may make the Windy Bee believe no one is present, preventing it from targeting you.
*   **Damage Mitigation:** Going just outside the field boundary while near the bee prevents damage from its tornadoes, though the wind gust attack still functions.
*   **Reward Collection:** Since tokens have a limited lifespan, players should follow the Wild Windy Bee to its next location first, then collect rewards using a Token Link or by being hit/targeting all enemies with Precise Bees.

## Trivia and Lore

*   The player can detect the bee's presence via the continuous movement of the Wind Shrine chimes (provided there hasn't been a recent donation).
*   If the timer expires before reward tokens are generated, the bee leaves without rewards. However, if it has already started producing them, it will finish spawning them as it flees.
*   Wild Windy Bee and Vicious Bee are unique among bosses/mobs that are Bees; unlike Rogue Vicious Bee, Wild Windy Bee does not have a gifted variant.
*   The bee is the only mob/enemy capable of knocking players back.
*   It is one of five mobs to have non-fixed levels (along with Ants, Stick Bug, Stick Nymphs, and Festive Nymphs).
*   Onett (Developer) has been known to spawn Wild Windy Bees in various fields, sometimes specifically to aid in growing sprouts. If spawned in the Stump Field, they freeze upon defeat until the timer expires because they cannot fly elsewhere from that location.