# Star Passives and Passive Abilities Guide

Passive abilities, or simply passives, are effects found on certain accessories, amulets, or bees. These abilities can be active constantly or only trigger when specific actions are performed as an additional effect of those actions.

**General Mechanics:**
*   Passives granted by an accessory or amulet are displayed near the hotbar.
*   Some passives require repeated actions; a number on the icon indicates how close it is to activating (it resets to 0 upon activation).
*   Many passive abilities have a cooldown, which is shown in pale red on the icon. While cooling down, no trigger will activate the ability, nor will the counter increase.
*   Items with these passives often have an initial cooldown when equipped to prevent bypassing the timer.

---

## Accessory Passives

### Haste Pulser
**Source:** Cobalt Guard
**Trigger:** Activates every 30th Haste token collected.
**Effect:** Fires a blue pulse that hops to each blue bee, identical to the effect of a Cobalt Bee. (If no blue bees are present, nothing happens.)

### Focus Pulser
**Source:** Crimson Guard
**Trigger:** Activates every 30th Focus token collected.
**Effect:** Fires a red pulse that hops to each red bee, identical to the effect of a Crimson Bee. (If no red bees are present, nothing happens.)

### Bubble Bombs
**Source:** Bubble Mask or Diamond Mask (if Bubble Mask is owned)
**Trigger:** Activates every 25th Bomb token collected, with a 2-minute cooldown.
**Effect:** Spawns 25 bubbles randomly in the player's current field.

### Diamond Drain
**Source:** Diamond Mask
**Trigger:** Activates every 30th Blue ability token collected, with a 45-second cooldown.
**Effect:** Summons a giant diamond that instantly converts 5 million pollen plus the total conversion amount.
*   Conversion bonus: +10% for every Blue bee owned; +50% for every Gifted Blue bee type owned.
*   Pollination: Pollinates 10 (+3 per Blue bee) blue flowers within the field.

### Ignite
**Source:** Fire Mask or Demon Mask (if Fire Mask is owned)
**Trigger:** Activates every 15th Red ability token collected.
**Effect:** Creates 5 flames in a plus shape where the 15th red token was collected.

### X-Flame
**Source:** Demon Mask
**Trigger:** Activates every 25th Battle ability token collected, with a 20-second cooldown.
**Effect:** Creates 29 flames in an X shape around the player.

### Coin Scatter
**Source:** Honey Mask or Gummy Mask (if Honey Mask is owned)
**Trigger:** Activates every 20th Mark token collected, with a 2-minute cooldown.
**Effect:** Converts pollen equal to 300% of the player's total conversion amount and scatters it into 24 honey tokens around the last field the player was in.
*   Token value: Minimum of 1000 honey per token, increasing with converted pollen and the Honey From Tokens stat.
*   Collection: Cannot be collected by Token Link, but can be collected by Triangulate.

### Gummy Morph
**Source:** Gummy Mask
**Trigger:** Activates every 30 Gumdrops used or 10 Gummy Bee ability tokens collected (Gummy Bee tokens count as 3 gumdrops).
**Effect:** The player transforms into a Gummy Bear, the Gummy Bee glows, and the field is covered in goo.
*   **As Gummy Bear:** Grants +75% Goo, +100% Instant Goo Conversion, +24 Movespeed, and +60 Jump Power.
*   **Glow Effect (for 10 seconds):** The Gummy Bee gains +1000% Gather Amount, +300 Attack, and +200% Movespeed while leaving a trail.

### Coconut Haste
**Source:** Coconut Clogs or Gummy Boots
**Trigger:** Activates whenever the player is hit by a falling Coconut.
**Effect:** Grants one stack of Haste and 2 seconds of Coconut Surge (x1.5 Bee Movespeed and +10 Player Movespeed).

### Goo Trail
**Source:** Gummy Boots
**Trigger:** Always active while equipped.
**Effect:** Passively covers 5 surrounding flowers with goo wherever the player walks on a field. Flowers directly behind the player receive more goo than those surrounding them.

### Emergency Coconut Shield
**Source:** Coconut Canister
**Trigger:** Activates when the player takes damage directly from a mob, with a 5-minute cooldown.
**Effect:** Summons 5 Coconuts in the last field, grants 100% Defense, and increases Bee Attack by x1.25 for 10 seconds. (Does not protect against instant kill mobs like Tunnel Bear or Cave Monsters.)

### Inspire Coconuts
**Source:** Coconut Canister
**Trigger:** Activates every 5th Inspire token, Star Shower's shooting stars, or Beesmas Light collected.
**Effect:** Summons 5 falling Coconuts in the last field the player was in.

### Petal Storm
**Source:** Petal Belt or Coconut Belt (if Petal Belt is owned)
**Trigger:** Activates every 30th Boost token collected, with a 30-second cooldown.
**Effect:** Fires 30 Petal Shurikens around the player in a spiral pattern. When passing through a bee, the bee instantly converts 10,000 pollen, increased by 7% of its conversion amount.

### Combo Coconuts
**Source:** Coconut Belt
**Trigger:** Activates every 40th Coconut dropped onto a field (via items or abilities).
**Effect:** The 40th coconut becomes a Combo Coconut. When caught by any player, it is kicked and falls onto either the summoner's field (if caught within the blue circle on first drop) or another player's field.
*   **Kicking Effect:** Each kick speeds up the coconut and grants the kicker stacks of Coconut Combo.
    *   Default: 1 stack per kick.
    *   Bonus Stack 1: +1 if caught in a different colored field than where it was last caught.
    *   Bonus Stack 2: Between +1 to +4 depending on how long it has been since it was caught in the same color classification (Red/Blue/White/Mixed) as the current field.
    *   Bonus Stack 3: +10 if the catcher is a new player catching it in a field with a different color classification than where it was previously caught.
*   **Buff:** Grants between 25% to 75% Unique Instant Conversion, between x1.2 to x2 Pollen, and between +1% to +50% Red/Blue/White Pollen, Bee Attack, and Honey From Tokens.
*   **Failure:** If the coconut fails to be caught, it despawns and reapplies the buff to all players who caught it at least once.
*   **Restrictions:** Cannot be passed in the Ant Field; spawned in the Ant Field results in a miss. Has a limit of 50 kicks before premature ending.

---

## Star Amulet Passives

### Guiding Star
**Source:** Diamond or Supreme Star Amulet (with this passive)
**Trigger:** Activates every 250th Boost token collected, with a 5-minute cooldown.
**Permanent Bonus:** Permanently grants 1.25x capacity.
**Effect:** Summons a Guiding Star over one of the five fields the summoner has collected the least from for 10 minutes. The probability of selection is based on relative pollen collection (the $n$-th least collected field has a $(6-n)/15$ chance).
*   **Summoner Buff:** Grants x2.5 Pollen, Convert Rate, and Capacity to the summoner.
*   **Other Players Buff:** Grants x1.25 Pollen, Convert Rate, and Capacity to other players in that field.
*   **Pollination:** While active, it pollinates 15 (+1 per Gifted Bee Type) flowers every 15 seconds.
*   **Duration:** Disappears if the summoner leaves the server.

### Star Shower
**Source:** Diamond or Supreme Star Amulet (with this passive)
**Trigger:** Activates every 40th Boost or Mark token collected, with a 30-second cooldown.
**Permanent Bonus:** Permanently grants 1.25x capacity.
**Effect:** 10 shooting stars fall onto the player's field. Each star collects and instantly converts 30 pollen (+50% per Gifted Bee Type) from 5 flowers.
*   **Catching a Star:** Grants one stack of Inspire and instantly converts 1,000,000 pollen, added by 200% of the player's total conversion amount.

### Pop Star
**Source:** Supreme Star Amulet (with this passive)
**Trigger:** Activates every 30th Boost token collected, with a 1-minute cooldown.
**Permanent Bonus:** Permanently grants x1.25 Blue Field Capacity.
**Effect:** Summons a Pop Star that lasts for 45 seconds, granting 10% Instant Blue Conversion and x2 Blue Pollen. It automatically applies 2 minutes of Bubble Bloat.
*   **Bubble Interaction:** While active, every bubble popped increases the bonus Blue Pollen by 1% (up to x4.5 from x2) and grants 4 seconds of Bubble Bloat (6 seconds if gold; 1 second otherwise).
*   **Bubble Bloat Effect:** Increases Blue Field Capacity and Convert Rate at Hive by up to x6 for up to 2.5 hours.
*   **End State:** When the Pop Star ends, it spawns several bubbles over the field that increase with the number of Bubbles popped.

### Gummy Star
**Source:** Supreme Star Amulet (with this passive)
**Trigger:** Activated at a 2% chance when using Gumdrops, or on the 75th use after the cooldown ends, with a 1-minute cooldown.
**Permanent Bonus:** Permanently grants x1.25 White Field Capacity.
**Effect:** Summons a Gummy Star that lasts for 45 seconds, granting 10% Instant White and Goo Conversion. Collecting goo during this time makes the star grow, granting bonus White Pollen and Goo (up to x2).
*   **End State:** After 45 seconds, it pops, scattering honey tokens and Gumdrops tokens on the last field. The total value of the honey tokens is a percentage of the goo collected, equal to 1.5% per gifted colorless bee type on the hive. The number of Gumdrops tokens increases with the amount of goo collected.

### Scorching Star
**Source:** Supreme Star Amulet (with this passive)
**Trigger:** Activates every 30th Boost token collected, with a 1-minute cooldown.
**Permanent Bonus:** Permanently grants x1.25 Red Field Capacity.
**Effect:** Summons a Scorching Star for 45 seconds, granting 50% Instant Flame Conversion, +5 Conversion Links, and x2 Red Pollen and Convert Rate.
*   **Growth Mechanic:** Standing near flames causes the star to grow, increasing bonus Red Pollen and Convert Rate (up to x5 from x2) and the number of Conversion Links (up to 30 from 5).
*   **End State:** When Scorching Star ends, it converts all pollen in the player's bag into Honey.

### Star Saw
**Source:** Supreme Star Amulet (with this passive)
**Trigger:** Activates after using 3 Stingers. The third Stinger used is refunded, and the Star Saw summons for 30 seconds.
**Effect:** The saw circles around the player, damaging hostile mobs (15% of Total Attack, accuracy based on average bee level), collecting tokens, and converting pollen from flowers.
*   **Conversion Rate:** Collects and instantly converts 3 pollen (+0.5 for every 100 Total Attack) from 5 flowers 10 times a second. The saw instantly converts additional gathered pollen.

---

## Bee Passives (Passive Gathering Effects)

### Gathering Bubbles
**Source:** Bubble Bee, Tadpole Bee, and Frogs
**Effect:** These bees have a percentage chance to spawn bubbles while gathering.
*   Bubble Bees: 35% chance (50% if gifted).
*   Tadpole Bees: 65% chance (85% if gifted).

### Gathering Flames
**Source:** Fire Bee, Demon Bee, Spicy Bee's Inferno, and bees with Electric Candle Beequip.
**Effect:** These bees have a percentage chance to spawn flames while gathering.
*   Fire Bees: 35% chance (50% if gifted).
*   Demon Bees: 55% chance (75% if gifted).

### Steam Engine
**Source:** Spicy Bee (Exclusive)
**Effect:** Boosts any Spicy Bee's speed by up to 100% with Flame Heat. While active, the Spicy Bee increases steam particle output proportional to the amount of flame heat.

### Fuzzy Coat
**Source:** Fuzzy Bee (Exclusive)
**Effect:** Has a chance to pollinate up to 5 surrounding flowers when gathering (9 if gifted). Lower-tier flowers have a higher chance of being pollinated than higher-tier flowers.

### Nectar Lover
**Source:** Shy Bee (Exclusive)
**Effect:** Makes Shy Bee twice as likely to sip from a planter compared to any other bee. When sipping, it collects twice as much nectar and contributes twice as much to the planter's growth.

### Shimmering Honey
**Source:** Diamond Bee (Exclusive)
**Effect:** Whenever this bee converts at the hive, it grants a 25% bonus honey (+2.5% per level). This bonus is doubled if the bee is Gifted.

### Balloon Enthusiast
**Source:** Buoyant Bee (Exclusive)
**Effect:** When converting from Balloons, this bee gains x3 its normal convert amount. Additionally, its base attack scales up to x3 with Balloon Blessing.

### Sniper
**Source:** Precise Bee (Exclusive)
**Effect:** In battle, the bee uses slow, long-range, more accurate shots dealing x2 damage. Accuracy is calculated as if the bee were 1 level higher (2 if gifted), and it cannot be below 5%. Critical Hits cut reload time in half; Super-Crits reduce it by 75%.

### Drive Expansion
**Source:** Digital Bee (Exclusive)
**Effect:** Using a Drive while this bee is active in Robo Bear's Challenge corrupts the field proportional to matching flowers. It permanently enhances the bee, granting stats based on the Drive used:
*   Red Drive: +0.03 Attack
*   Blue Drive: +2 Convert Amount
*   White Drive: +0.25 Gather Amount
*   Glitched Drive: +0.05% Ability Rate

**Enhancements:** Every 10 Glitched Drives grants a Hive Bonus of 0.03% Ability Duplication Chance. Digital Bee can be enhanced with up to 500 of each type of Drive. Upon maxing out (2000 total Drives), Digital Bee gains +10 Movespeed.

---

## Other Passives

### Unlimited Gumdrops
**Source:** Buffs & Debuffs (via Codes and Glue Dispenser)
**Effect:** Allows the player to use Gumdrops without losing any from their inventory. This buff does not increase the total amount of Gumdrops in the inventory.

## Trivia

*   There is a visual glitch where, if the player has the Fire, Honey, Bubble, Demon, Gummy, or Diamond Mask equipped, looking at it through the Coconut Shield will make the front of the mask disappear (caused by glass textures overriding particles).
*   Bubble Bombs causes each bubble popped to increase in pitch; this effect is unique to that passive.