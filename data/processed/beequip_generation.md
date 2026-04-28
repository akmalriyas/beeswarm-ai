# Beequip Generation Mechanics

![Digital Bee](https://static.wikia.nocookie.net/bee-swarm-simulator/images/2/27/Digital_Bee.png/revision/latest/scale-to-width-down/100?cb=20230415203844) | *Note: This content is based on datamined information and may contain inaccuracies or outdated details.*

This article provides an in-depth look at the inner workings of beequip generation. It walks through each step of the function that determines a beequip's stats, highlighting known quirks and bugs along the way.

For context, please read [the shortened explanation of Beequip Generation](/wiki/Beequip#Generation). This article assumes basic knowledge of programming concepts, specifically random number generation and floating-point numbers. A basic understanding of Lua is also helpful.

## Core Concepts

### The Resolve Function (RQValue)

The Resolve function (or RQValue function) is the primary determinant of a beequip's stats. While its full mechanics are detailed on its module page, this article only requires knowing how it outputs values:

1.  **Exact Value:** If the function uses linear scaling or if the stat value is fixed, it returns an exact number. Higher provided *quality* increases the range of possible outcomes (closer to the left and right bounds).
2.  **Random Value:** If the function uses `RandomBias`, it returns a random value between two given limits, biased toward a specific central value. Higher provided *quality* narrows this bias closer to the defined bounds.

*Note: The left bound does not necessarily need to be smaller than the right bound.*

The result is then rounded by a specified *resolution* value, if one is provided. If no resolution value is given, the raw result is kept as-is.

### Weights

When weights are mentioned, they refer to a pool of items (stats or abilities) from which the game selects one or more. The weight determines the probability of an item being picked.

The selection process involves generating a random number between 0 and the total sum of all weights in the pool. The system then iterates through the pool, subtracting each item's weight from the random number until the remaining value is less than or equal to zero. The stat corresponding to that pointer position is selected.

**In simpler terms: An item's probability of being picked equals its weight divided by the total weight sum of all items in the pool.**

### Beequip Data Table Structure

Each beequip's template stats are stored as a table, which the game uses to determine the final statistics. These tables (with minor modifications) can be found in [Module:Beequip Stats/data](/wiki/Module:Beequip_Stats/data).

Key keys important for understanding generation include:

*   `DisplayName`: The name displayed to the player.
*   `Description`: The description viewable in storage or the Inbox.
*   `Rarity`: The *perceived* rarity; this value is not used by the game mechanics.
*   `EquipLimit`: The maximum number of this type of beequip a bee can equip.
*   `Beesmas`: Indicates if the beequip is Beesmas-related.
*   `OldRNG`: Determines whether to use the `Resolve` or `OldResolve` function during generation.
*   `Requirements`: The requirements for a bee to utilize the beequip.
*   `Modifiers`: An array containing RQValue-valid tables that describe every base bee stat the beequip can possess.
*   `HiveBonuses`: An array containing RQValue-valid tables that describe every base hive bonus the beequip can possess.
*   `Abilities`: An array of tables, each containing either a specific ability name or a pool of names. The beequip is guaranteed to have one of these abilities.
*   `Upgrades`: An array of tables describing every upgradable stat and/or ability. (Note: If the table contains `Chance` and `Value`, a different upgrade process is used.)

## Generation Process

### Seed Assignment

Every beequip is assigned a new seed upon initial generation, and again whenever a Swirled Wax is applied. This seed initializes the random number generator for the *entire duration* of that specific beequip's generation. The game stores this seed instead of storing every individual stat value.

While knowing the seed theoretically allows one to predict stats before waxing (assuming only guaranteed successful waxes are used), in practice, this prediction is extremely difficult due to subsequent factors discussed below.

### Base Stat Determination

The beequip determines its base stats by iterating through the `Modifiers`, `HiveBonuses`, and `Abilities` arrays, in that specific order.

#### Modifiers and Hive Bonuses
Every table within these two arrays is passed into the Resolve function. If the function returns `nil`, the stat will not be present. If it returns a single number value, the beequip receives that stat at that strength.

**Quirks:**
*   Since probability resolution uses the Resolve function, the chance of receiving a stat might itself be a random value (if RandomBias is used). The beequip's potential improves its chances of getting a better *probability*, but this does not guarantee an improved final stat.
*   If a stat lacks a resolution value, it remains unrounded internally. However, when displayed to the player, these stats are rounded to a certain resolution (e.g., +24.6% Gather Amount may display as +25%).
*   **Rounding Issue:** If a stat has a resolution value, but its intended limits do not evenly divide that resolution, rounding can change the effective range. For example, if a base stat is intended to be between 3% and 8%, but uses a resolution of 10%, the actual resulting range becomes 0% to 10%. Values between 3-5% round down to 0%, while values between 5-8% round up to 10%.

#### Abilities
Every table in the `Abilities` array is iterated through, and the ability listed is added to the beequip. If a table contains a pool of names, one is selected randomly using the weight system. Currently, all abilities within any beequip's ability pool share equal weights.

### Upgrade Process

The upgrade step only proceeds if the beequip has accumulated wax points from successful waxes.

#### Calculating Chances
If wax points are available, the game iterates through every table in the `Upgrades` array to calculate the weight value for each upgradable stat. This is done by running the Resolve function on the table's `Chance` table and saving the result into a pool.

Two separate pools are maintained: one for all possible upgradable stats, and one for those that do not require wax points from Caustic or Debug Waxes.

**Upgrade Limits:** Upgrades have a maximum allowed number of wax points. Once this limit is reached, the stat is removed from the upgrade pools, which increases the probability of upgrading other available stats.

*Note: Similar to base stats, because weights are resolved using Resolve, it is possible that one or more stats' upgrade weights are randomized (if RandomBias is used). The beequip's potential improves its chance of a higher weight, but this does not guarantee an improved upgrade.*

#### Applying Waxes
Each wax applied to the beequip is iterated through again. If the wax was successful, the associated wax points are added to the beequip.

Crucially, before applying the wax points, **the game uses a random number generator initialized by a stored number (0-16) and runs it that many times.** This specific number is *not* determined by the beequip's seed, making the exact sequence of wax upgrades practically impossible to predict even if the initial beequip seed is known.

#### Determining Upgrade Value
Once an upgrade stat is selected by a wax point, the Resolve function is run on the stat's `Value` table to determine the magnitude of the upgrade. If an ability is chosen, it is granted to the beequip (though the specific ability from a pool is not decided at this step).

**Quirks:**
*   **Display Rounding:** Just like base stats, if the upgrade value lacks a resolution value, it remains unrounded internally. However, when displayed to the player, it is rounded (e.g., +1.6% Gather Amount may display as +2%). This can lead to discrepancies where the total actual stat increase differs from the sum of the rounded values.
*   **Resolution Range Issue:** If an upgrade value has a resolution but its intended limits do not divide evenly, rounding can change the effective range. For example, if an upgrade is intended to be between 3% and 8%, but uses a resolution of 10%, the actual range becomes 0% to 10%. A major issue arises when the resolution value is too high (as seen with certain items), causing the entire range of possible upgrade values to round down to 0%, effectively wasting the wax point.

### Final Cleanup
After all generation steps are complete, the chosen stats are parsed into a format readable by the game code. While this step itself has no major quirks, if an ability pool was selected during the waxing phase, the final choice of ability is made here—*after* every single wax point has been applied. This means that applying extra wax points (via Soft/Debug Wax or successful Hard/Caustic Wax) can change which ability is ultimately chosen, as the random number generation continues to advance through numbers without needing a Swirled Wax.

## Item Effects on Beequips

[Waxes](/wiki/Waxes) and [Turpentines](/wiki/Turpentine) affect beequips in specific ways:

*   **Non-Swirled Waxes:** If successful, these waxes run the beequip's random number generation a random number of times before applying a set amount of wax points.
    *   **Soft Wax:** 1 wax point, 100% success rate.
    *   **Hard Wax:** 2 wax points, 60% success rate.
    *   **Caustic Wax:** 4 wax points, 25% success rate (destroys the beequip if it fails).
    *   **Debug Wax:** 4 wax points, 100% success rate.
*   **Swirled Wax:** Changes the beequip's seed. This effectively alters both the base stats and upgrade values of the beequip, but it *does not* change the number of times each subsequent wax runs the random number generator.
*   **Turpentine:** Resets the beequip's seed to its original value. It then runs the beequip's random number generation once for every Turpentine applied *after* base bee stats and hive bonuses are generated, but *before* abilities are generated. This reverts the base stats/hive bonuses to their originals, meaning that if the beequip has an ability pool, the chosen ability may differ from its original selection.