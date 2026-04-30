# Bee Stats

The stats section details the core attributes that determine how a bee performs in Bee Swarm Simulator. These statistics are fundamental to gameplay and can increase as bees gain higher levels (Bond).

*Note: For stats related to the player, pollen collection mechanics, or the Hive itself, please refer to the [System Page](/wiki/System_Page).*

## Rarity
**Rarity** dictates how frequently a bee of a specific category is generated from eggs or royal jelly. While bees of greater rarity often possess higher base statistics and unique abilities, rarity itself does not directly influence performance. Bees acquired through specialized methods are categorized as Event tier bees.

## Color
A bee's **Color** affects its ability to gather pollen. Blue and Red bees receive a 50% Gather Amount bonus when collecting from flowers of a matching color. Colorless bees do not benefit from this boost, even when gathering from white flowers.

## Bond
Bond is the stat that determines if a bee has accumulated enough "experience" to level up. Experience can be gained through several activities:
*   Treats
*   Collecting Pollen
*   Battles
*   Puppy Love events
*   Digging in during Beesmas Feast (during Beesmas)

## Energy
**Energy** represents the number of times a bee will gather pollen or attack mobs before it must return to the Hive to rest. A full recharge takes 30 seconds upon entering the hive.

Key mechanics regarding Energy:
*   Spawning Ability Tokens does not cost a bee energy.
*   The energy of all bees in a swarm can be increased via stacks of Polar Power buffs (from the Polar Bear's quests) or through an energy mutation.
*   Energy increases by 5% for each level above Level 1.
*   Resetting yourself sends bees back to the hive, but they will not recharge their energy during this process. An "energy reset" can be achieved by resetting while the bees are inside the Hive after a prior reset.

**Energy Formula:**
$$\text{Base Energy} \times (1 + 0.05 \times (\text{Level} - 1)) \times \text{Polar Power} + \text{Energy Mutation}$$

## Speed
**Speed**, also known as **Bee Movespeed**, determines how quickly a bee moves and executes actions (contrary to its name). This stat indirectly affects all basic processes, including gathering, attacking, sipping nectar in planters, and conversion rates at the Hive.

Movement modifiers:
*   Bees move at approximately 1.5 times their base speed when away from their owner.
*   Bees move at 0.5 times their base speed when returning to the hive to rest.

The speed of all bees in a swarm can be increased by various bonuses, including Gifted Bee/Ninja Bee Hive Bonuses, Beesmas Cheer, Playtime Badge, Oil, Super Smoothies, and activating Coconut Haste.

**Bee Movespeed Formula:**
$$\text{Base Bee Movespeed} \times (1 + 0.03 \times (\text{Level} - 1)) \times (1 + \text{Ninja Bee Hive Bonus} + \text{Playtime Badge Bonus})$$

## Attack
**Attack** determines the amount of damage a bee inflicts when fighting mobs. This stat remains constant across all levels but can be boosted through various accessories, items, amulets, certain Gifted Hive Bonuses, and ability tokens. Gifted bees have 50% more attack.

**Attack Formula:**
$$(\text{Base Attack Damage} + \text{Attack Buffs}) \times \text{Attack Multiplier} \quad (\times 1.5 \text{ if the bee is gifted})$$

## Gather Amount
**Gather Amount** describes both the quantity and speed at which a bee collects pollen from a flower. The amount collected increases by 10% for each level above Level 1. This stat can also be increased via amulets, certain Gifted Bee bonuses, Gamepasses, or items.

**Gather Amount Formula:**
$$\text{Base Gather Amount} \times (1 + 0.10 \times (\text{Level} - 1)) \times \text{Gifted Multiplier}$$

## Production Amount
**Production Amount** describes how much pollen a bee converts into honey at the Hive and the speed of that conversion. The amount converted increases by 10% for each level above Level 1.

**Production Amount Formula:**
$$(\text{Base Production Amount} + \text{Production Amount}) \times (1 + 0.10 \times (\text{Level} - 1)) \times \text{Conversion Rate} \times \text{Gifted Multiplier}$$

## Mutations
Mutations are bonuses granted by feeding bitterberries to a bee while it is under the **radioactive** effect. Mutations can grant bonus increases to:
*   Attack
*   Convert Amount
*   Gather Amount
*   Energy
*   Bee Ability Rate
*   Bee Movespeed
*   Critical Chance
*   Instant Conversion

## Gifted
**Gifted** is a status granted by feeding a bee its favorite treat (Star Treat, Gingerbread Bear, or Aged Gingerbread Bear). This grants several benefits:
*   A 1.5x multiplier to gather amount, convert amount, and bee attack simultaneously.
*   The ability to spawn Inspire tokens.
*   A unique gifted hive bonus (only once per bee).
*   An additional gifted ability (if the bee possesses one).
*   A new appearance for the bee.