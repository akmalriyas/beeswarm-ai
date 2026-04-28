# Commando Chick

![TransparentCommandoChick](https://static.wikia.nocookie.net/bee-swarm-simulator/images/7/78/TransparentCommandoChick.png/revision/latest/scale-to-width-down/268?cb=20250616073900)

**Note:** This content contains information obtained through datamining. Due to the nature of the information, details may be inaccurate or outdated.
*Datamined Information:* The formula for calculating Commando Chick's level at a given capture count.
*Date of Datamined File:* December 19th, 2024

## Overview

Commando Chick is a mini-boss chick that spawns in its dedicated hideout. Its hideout is located to the left of the Brown Bear and the Wealth Clock. To access the hideout, players must cut the surrounding vines using Clippers, Scissors, Scythe, or Dark Scythe; once cut, these vines will not regrow.

Commando Chick has a respawn time of 30:00 seconds (or 25:30 seconds when boosted by the Gifted Bee Vicious Bee hive). It is visually distinct from other chicks, being twice as large as a normal chick, featuring a green shell and red eyes.

### Stats & Mechanics

| Attribute | Value | Notes |
| :--- | :--- | :--- |
| **Base Health** | 150 - 10,000,000 | Increases significantly with level/captures. |
| **Damage (Collision)** | 20 | Damage dealt when colliding with the player. |
| **Damage (Grenade)** | 50 | Damage dealt to players near an exploding grenade. |
| **Base Battle Points** | 0 | |
| **Base Bond** | 5 | |
| **Base Honey** | 2,400 - 18B | Varies based on the chick's current level. |
| **Level Range** | 3 - 25 | Dependent on the number of captures. |

#### Combat Behavior
When Commando Chick is in its egg, it throws grenades:
*   1 grenade if health > 2/3.
*   2 grenades if health < 2/3 but > 1/3.
*   3 grenades if health < 1/3 but > 1/100.
*   4 grenades if health < 1/100.

The chick starts at Level 3 with 150 HP. With each successive capture, its health and level increase. It reaches Level 6 by the fifth capture, after which it gains another level for progressively higher amounts of captures.

When in its shell, Commando Chick remains still and blocks attacks. After a period, it jumps out to resume roaming within the hideout.

## Levels & Progression

The Commando Chick's level is determined by the total number of kills recorded against it.

**Level Calculation Formula:**
Let $x$ be the number of kills.
*   If $x < 2$, its level is 3.
*   Otherwise, its level is calculated using:
    $$3+\left\lfloor \frac{-1.375+{\sqrt {0.390625+1.5x}}}{0.75}+1 \right\rfloor$$
    This result is clamped between 1 and 25.

The higher the level, the more HP it possesses and the faster it moves (increasing by 0.5 studs per level).

**Level Progression Table:**

| Level | Kills Required | Health |
| :---: | :---: | :---: |
| 3 | 0 | 150 |
| 4 | 2 | 2,000 |
| 5 | 3 | 10,000 |
| 6 | 6 | 15,000 |
| 7 | 9 | 25,000 |
| 8 | 13 | 50,000 |
| 9 | 18 | 100,000 |
| 10 | 23 | 150,000 |
| 11 | 29 | 200,000 |
| 12 | 36 | 300,000 |
| 13 | 44 | 400,000 |
| 14 | 53 | 500,000 |
| 15 | 62 | 750,000 |
| 16 | 72 | 1,000,000 |
| 17 | 83 | 2,500,000 |
| 18 | 94 | 5,000,000 |
| 19 | 106 | 7,500,000 |
| 20 | 119 | 10,000,000 |
| 21 | 133 | 10,000,000 |
| 22 | 148 | 10,000,000 |
| 23 | 163 | 10,000,000 |
| 24 | 179 | 10,000,000 |
| 25 | 196 | 10,000,000 |

## Drops & Milestones

While a complete list of drops is available on the dedicated Commando Chick/Drops page, certain items are guaranteed upon reaching specific capture milestones:

*   **Honey From Tokens:** This system page increases the honey output from each capture.
*   **Loot Luck:** Does not affect Commando Chick's drop rates.
*   Commando Chick tokens are automatically collected when they fade away.

**Milestone Rewards:**
*   5th Capture: Glue
*   10th Capture: Gold Egg
*   15th Capture: Star Jelly
*   20th Capture: 3 Blue Extracts
*   25th Capture: 100 Tickets
*   30th Capture: 10 Stingers
*   40th Capture: 10 Ant Passes and 10 Stingers
*   50th Capture: Mythic Egg
*   100th Capture: Star Treat
*   200th Capture: Commander Bee Egg

## Strategy Guide

*   **Damage Mitigation:** Standing on the last stair, closest to the hideout, often causes Commando Chick to flee. However, if the player stands precisely on the edge of that stair (as close as possible to the hideout), the chick will not flee, allowing players' bees to damage it without taking damage themselves. This strategy is not guaranteed and may fail due to the chick accidentally jumping onto the stair while entering its egg; moving in and out of the hideout can resolve this.
*   **Grenade Spawning:** Re-entering the hideout while Commando Chick is still inside its egg will cause it to revert to its roaming state, although it will spawn another set of grenades upon exiting.
*   **Cooperative Play:** Since any player can damage Commando Chick, having multiple players assist in the fight can significantly speed up progress.

## Trivia & Lore

*   Commando Chick is one of only three mobs (along with King Beetle and Tunnel Bear) that possesses its own dedicated hideout; furthermore, it is the only one requiring an obby to enter.
*   It is the only chick species with a green-colored egg.
*   The chick can spawn numerous grenades by repeatedly leaving and reentering its spawn area.
*   Commando Chick is unique among chicks for having red eyes (all others have black eyes).
*   It is one of two chicks that drops a Mythic Egg; the other is the Mondo Chick.
*   Like Stump Snail, Commando Chick is one of only two mobs whose health persists if the player leaves the session mid-fight.
*   While only your Commando Chick can deal damage to you via contact, all grenades it throws can damage any nearby player.
*   **Glitch Information:**
    *   A glitch exists where the chick disappears during combat, triggering a specific fleeing message: "🐣 Commando Chick got away! 🐣" (The normal message is "🐣 Commando Chick fled! (HP Saved) 🐣").
    *   There is a clipping bug where its feet get stuck in the ground, causing it to slide and move extremely fast, even while in its egg. If this occurs near a corner, it may stay there until it resumes roaming.
    *   A previous glitch caused the chick to remain indefinitely inside its egg; exiting and re-entering the hideout usually resolved this issue.