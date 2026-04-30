# Passive Abilities Guide

Passive abilities, or simply passives, are effects found on certain accessories, amulets, or bees. These abilities can be active at all times or activate only when specific actions occur, providing an additional effect to those actions.

**Mechanics Overview:**
*   **Display:** Passives granted by an accessory or amulet are displayed near the hotbar.
*   **Activation Counters:** Some passives require repeated actions; a number on the icon indicates how close it is to activating (resets to 0 upon activation).
*   **Cooldowns:** If a passive is on cooldown, the remaining time in seconds is shown in pale red. No trigger will activate the ability or increase the counter while cooling down. Initial cooldowns prevent players from bypassing these timers by equipping items.

---

## Accessory Passives

### Haste Pulser
*   **Source:** Cobalt Guard
*   **Activation:** Activates every 30th Haste token collected.
*   **Effect:** Fires a blue pulse that hops to each blue bee, identical to the effect of a Cobalt Bee. (Does nothing if no blue bees are present.)

### Focus Pulser
*   **Source:** Crimson Guard
*   **Activation:** Activates every 30th Focus token collected.
*   **Effect:** Fires a red pulse that hops to each red bee, identical to the effect of a Crimson Bee. (Does nothing if no red bees are present.)

### Bubble Bombs
*   **Source:** Bubble Mask or Diamond Mask (if owning Bubble Mask)
*   **Activation:** Activates every 25th Bomb token collected, with a 2-minute cooldown.
*   **Effect:** Spawns 25 bubbles randomly in the player's current field.

### Diamond Drain
*   **Source:** Diamond Mask
*   **Activation:** Activates every 30th Blue ability token collected, with a 45-second cooldown.
*   **Effect:** Summons a giant diamond that instantly converts 5 million pollen plus the player's total conversion amount. The conversion amount increases by 10% for every blue bee and by 50% for every Gifted Blue bee type owned. It also pollinates 10 (+3 per Blue bee) blue flowers in the field.

### Ignite
*   **Source:** Fire Mask or Demon Mask (if owning Fire Mask)
*   **Activation:** Activates every 15th Red ability token collected.
*   **Effect:** Creates 5 flames in a plus shape where the 15th red token is collected.

### X-Flame
*   **Source:** Demon Mask
*   **Activation:** Activates every 25th Battle ability token collected, with a 20-second cooldown.
*   **Effect:** Creates 29 flames in an X shape around the player.

### Coin Scatter
*   **Source:** Honey Mask or Gummy Mask (if owning Honey Mask)
*   **Activation:** Activates every 20th Mark token collected, with a 2-minute cooldown.
*   **Effect:** Converts pollen equal to 300% of the player's total conversion amount and scatters it into 24 honey tokens around the last field the player was in. These tokens last for 1 minute. Each token grants a minimum of 1,000 honey, increasing with converted pollen and the player's Honey From Tokens stat. (Cannot be collected by Token Link, but can be collected by Triangulate.)

### Gummy Morph
*   **Source:** Gummy Mask
*   **Activation:** Activates every 30 Gumdrops used or 10 Gummy Bee ability tokens collected (Gummy Bee tokens count as 3 gumdrops).
*   **Effect:** The player transforms into a Gummy Bear, the Gummy Bee glows, and the field is covered in goo.
    *   **As Gummy Bear:** Grants +75% Goo, +100% Instant Goo Conversion, +24 Movespeed, and +60 Jump Power.
    *   **Glow Effect (for 10 seconds):** The Gummy Bee gains +1000% Gather Amount, +300 Attack, and +200% Movespeed while leaving a trail.

### Coconut Haste
*   **Source:** Coconut Clogs or Gummy Boots
*   **Activation:** Activates whenever the player is hit by a falling Coconut.
*   **Effect:** The player gains one stack of Haste and 2 seconds of Coconut Surge, granting x1.5 Bee Movespeed and +10 Player Movespeed.

### Goo Trail
*   **Source:** Gummy Boots
*   **Activation:** Always active while equipped.
*   **Effect:** Passively covers 5 surrounding flowers with goo wherever the player walks on a field. Flowers directly behind the player receive more goo than those surrounding them.

### Emergency Coconut Shield
*   **Source:** Coconut Canister
*   **Activation:** Activates when the player takes damage directly from a mob, with a 5-minute cooldown.
*   **Effect:** Summons 5 Coconuts in the player's last field, grants 100% Defense, and increases Bee Attack by x1.25 for 10 seconds. (Does not protect against instant kill sources like Tunnel Bear or Cave Monsters.)

### Inspire Coconuts
*   **Source:** Coconut Canister
*   **Activation:** Activates every 5th Inspire token collected, Star Shower's shooting stars, or Beesmas Light collected.
*   **Effect:** Summons 5 falling Coconuts in the player's last field.

### Petal Storm
*   **Source:** Petal Belt or Coconut Belt (if owning Petal Belt)
*   **Activation:** Activates every 30th Boost token collected, with a 30-second cooldown.
*   **Effect:** Fires 30 Petal Shurikens in a spiral pattern around the player. When passing through a bee, the bee instantly converts 10,000 pollen, increased by 7% of its conversion amount.

### Combo Coconuts
*   **Source:** Coconut Belt
*   **Activation:** Activates every 40th Coconut dropped onto a field (via items or abilities).
*   **Effect:** The 40th coconut becomes a Combo Coconut. When caught, it is kicked and falls onto the summoner's field (if caught on the first drop within the blue circle) or another player's field. Each kick grants stacks of Coconut Combo:
    *   Default: 1 stack.
    *   Different Field Catch: +1 bonus stack.
    *   Same Color Classification Bonus: +1 to +4 bonus stacks (based on time since last catch in that color).
    *   New Player/Color Combination: +10 bonus stacks.
    *   **Buff:** Grants between 25% to 75% Unique Instant Conversion, between x1.2 to x2 Pollen, and between +1% to +50% Red/Blue/White Pollen, Bee Attack, and Honey From Tokens.
    *   **Notes:** Fails if not caught; reapplies buff to all previous catchers. Cannot be passed in the Ant Field. Limited to 50 kicks before premature end.

---

## Star Amulet Passives

### Guiding Star
*   **Source:** Diamond or Supreme Star Amulet (with passive)
*   **Activation:** Activates every 250th Boost token collected, with a 5-minute cooldown.
*   **Permanent Bonus:** Grants 1.25x capacity permanently.
*   **Effect:** Summons a Guiding Star over one of the five least collected fields for 10 minutes. The chance of selection is based on collection amount (the $n$-th least collected field has a $(6-n)/15$ chance).
    *   **Buffs:** Grants x2.5 Pollen, Convert Rate, and Capacity to the summoner, and x1.25 Pollen, Convert Rate, and Capacity to others in that field.
    *   **Pollination:** While active, it pollinates 15 (+1 per Gifted Bee Type) flowers every 15 seconds. Disappears if the summoner leaves the server.

### Star Shower
*   **Source:** Diamond or Supreme Star Amulet (with passive)
*   **Activation:** Activates every 40th Boost or Mark token collected, with a 30-second cooldown.
*   **Permanent Bonus:** Grants 1.25x capacity permanently.
*   **Effect:** 10 shooting stars fall onto the player's field. Each star collects and instantly converts 30 pollen (+50% per Gifted Bee Type) from 5 flowers. Catching a star grants an Inspire stack and instantly converts 1,000,000 pollen, plus 200% of the player's total conversion amount.

### Pop Star
*   **Source:** Supreme Star Amulet (with passive)
*   **Activation:** Activates every 30th Boost token collected, with a 1-minute cooldown.
*   **Permanent Bonus:** Grants x1.25 Blue Field Capacity permanently.
*   **Effect:** Summons a Pop Star for 45 seconds, granting 10% Instant Blue Conversion and x2 Blue Pollen. It automatically applies 2 minutes of Bubble Bloat.
    *   **Bubble Interaction:** While active, every bubble popped increases the bonus Blue Pollen by 1% (up to x4.5 from x2) and grants 4 seconds of Bubble Bloat (6s for gold bubbles, 1s otherwise).
    *   **Bubble Bloat Effect:** Increases Blue Field Capacity and Convert Rate at Hive by up to x6 for up to 2.5 hours. When the star ends, it spawns bubbles based on how many were popped.

### Gummy Star
*   **Source:** Supreme Star Amulet (with passive)
*   **Activation:** Activates at a 2% chance when using Gumdrops, or at the 75th use after cooldown, with a 1-minute cooldown.
*   **Permanent Bonus:** Grants x1.25 White Field Capacity permanently.
*   **Effect:** Summons a Gummy Star for 45 seconds, granting 10% Instant White and Goo Conversion. Collecting goo makes the star grow, granting bonus White Pollen and Goo (up to x2).
    *   **Pop Effect:** After 45 seconds, it pops, scattering honey tokens and Gumdrops tokens on the last field. Honey token value is based on a percentage of collected goo (1.5% per gifted colorless bee type), and the number of Gumdrops tokens increases with collected goo.

### Scorching Star
*   **Source:** Supreme Star Amulet (with passive)
*   **Activation:** Activates every 30th Boost token collected, with a 1-minute cooldown.
*   **Permanent Bonus:** Grants x1.25 Red Field Capacity permanently.
*   **Effect:** Summons a Scorching Star for 45 seconds, granting 50% Instant Flame Conversion, +5 Conversion Links, and x2 Red Pollen/Convert Rate. Standing near flames causes the star to grow, increasing bonus Red Pollen/Convert Rate (up to x5 from x2) and Conversion Links (up to 30 from 5). When it ends, it converts all pollen in the player's bag into Honey.

### Star Saw
*   **Source:** Supreme Star Amulet (with passive)
*   **Activation:** Activates after using 3 Stingers. The third Stinger used is refunded, and the saw summons for 30 seconds.
*   **Effect:** Circles around the player, damaging hostile mobs (15% of Total Attack, accuracy based on average hive bee level). It collects tokens and instantly converts 3 pollen (+0.5 per every 100 Total Attack) from 5 flowers ten times a second, converting all gathered pollen immediately.

---

## Bee Passives

### Gathering Bubbles
*   **Source:** Bubble Bee, Tadpole Bee, or Frogs
*   **Effect:** Certain bees have a percentage chance to spawn bubbles while gathering.
    *   Bubble Bees: 35% chance (50% if gifted).
    *   Tadpole Bees: 65% chance (85% if gifted).

### Gathering Flames
*   **Source:** Fire Bee, Demon Bee, Spicy Bee's Inferno, or Electric Candle Beequip.
*   **Effect:** Certain bees have a percentage chance to spawn flames while gathering.
    *   Fire Bees: 35% chance (50% if gifted).
    *   Demon Bees: 55% chance (75% if gifted).

### Steam Engine
*   **Source:** Spicy Bee (Exclusive)
*   **Effect:** Boosts any Spicy Bee's speed by up to 100% while active with Flame Heat. While active, the Spicy Bee increases steam particle output proportionally to the amount of flame heat.

### Fuzzy Coat
*   **Source:** Fuzzy Bee (Exclusive)
*   **Effect:** Has a chance to pollinate up to 5 surrounding flowers when gathering (9 if gifted). Lower-tier flowers have a higher probability of being pollinated.

### Nectar Lover
*   **Source:** Shy Bee (Exclusive)
*   **Effect:** Makes the Shy Bee twice as likely to sip from a planter compared to any other bee. When sipping, it collects double the nectar and contributes double to the planter's growth.

### Shimmering Honey
*   **Source:** Diamond Bee (Exclusive)
*   **Effect:** Whenever this bee converts at the hive, it grants a 25% bonus honey (+2.5% per level). This bonus is doubled if the bee is Gifted.

### Balloon Enthusiast
*   **Source:** Buoyant Bee (Exclusive)
*   **Effect:** When converting from Balloons, this bee gains x3 its normal convert amount. Additionally, its base attack scales up to x3 with Balloon Blessing.

### Sniper
*   **Source:** Precise Bee (Exclusive)
*   **Effect:** In battle, uses slow, long-range, more accurate shots dealing x2 damage. Accuracy is calculated as if the bee were 1 level higher (2 if gifted), and cannot be below 5%. Critical Hits halve reload time; Super-Crits reduce it by 75%.

### Drive Expansion
*   **Source:** Digital Bee (Exclusive)
*   **Effect:** Using a Drive while this bee is active in Robo Bear's Challenge corrupts the field based on matching flower color (Glitched Drives corrupt all fields equally). It permanently enhances the bee, granting stats:
    *   Red Drive: +0.03 Attack
    *   Blue Drive: +2 Convert Amount
    *   White Drive: +0.25 Gather Amount
    *   Glitched Drive: +0.05% Ability Rate
    *   **Enhancement Bonus:** Every 10 Glitched Drives grants a Hive Bonus of 0.03% Ability Duplication Chance.
    *   **Maxing Out:** Upon maxing out with all 2000 Drives, Digital Bee gains +10 Movespeed.

---

## Other Passives

### Unlimited Gumdrops (Free Gumdrops)
*   **Source:** Buffs obtained via certain codes and the Glue Dispenser.
*   **Effect:** Allows the player to use Gumdrops without losing them from their inventory. This buff does not increase the total amount of gumdrops in the inventory.

## Trivia
*   There is a visual glitch where, if the player has the Fire, Honey, Bubble, Demon, Gummy, or Diamond Mask equipped, looking at it through the coconut shield will make the front of the mask disappear due to glass textures overriding particles.
*   Bubble Bombs causes each bubble popped to increase in pitch; this effect is unique to that passive.