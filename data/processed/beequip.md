# Beequip

A **beequip** is an inventory item worn by bees that alters their stats and can provide bonuses to the hive. Equipping a beequip requires the bee to be at or above the level of the beequip. Some beequips have restrictions, such as requiring a specific mutation (e.g., the Bubble Light).

## Beequip Case

When obtained, beequips are initially stored in a **Beequip Case**. Items within this case can be given to bees by dragging them to a hive slot, or moved between the case, general storage, and inbox.

The Beequip Case is acquired after speaking with Dapper Bear at his shop. Players start with five slots but can expand this capacity through quests from Dapper Bear and Bee Bear during Beesmas 2020, reaching a maximum of 15 slots.

Opening the Beequip Case allows players to view all equipped beequips across their hives. While viewing, players can only interact with their own hive. Clicking or holding an equipped beequip in the case will highlight its location on the hive by causing it to enlarge and sway; simply reviewing the item from the hive slot does not trigger this effect.

## Beequip Storage

If the Beequip Case is full, or if the player has no Beequip Case, excess beequips are moved to the **Beequip Storage**. This storage is located near the Dandelion Field or the Public Sticker Board in the Hive Hub. Beequips stored here cannot be given to bees.

By default, the storage holds 10 slots. Players can purchase up to 90 additional slots for a maximum total of 100, costing 123,500 tickets. Additional slots may also have been obtained by completing Bee Bear's quests during Beesmas 2020.

If both the storage and case are full, beequips are moved to the **Beequip Inbox**. The inbox holds the player's 25 most recent beequips but has a strict 48-hour time limit before items are discarded automatically. To prevent an item from being deleted, players must empty a slot in their Beequip Case.

Permanent beequips can be stored in the 'Permanents' section of the Beequip Storage without consuming space. However, even permanent beequips still require a case slot to be equipped onto a bee. Previously, items like Reindeer Antlers and Festive Wreath were permanent; however, they have since been converted into standard beequips, with developers noting potential changes to the permanent feature.

| Tickets | Storage Slots (Max) | Case Slots (Max) |
| :---: | :---: | :---: |
| 10 | 100 | 15 |
| 250 | 20 | 20 |
| 450 | 25 | 25 |
| 800 | 30 | 30 |
| 1,250 | 35 | 35 |
| 1,850 | 40 | 40 |
| 2,550 | 45 | 45 |
| 3,400 | 50 | 50 |
| 4,400 | 55 | 55 |
| 5,550 | 60 | 60 |
| 6,800 | 65 | 65 |
| 8,250 | 70 | 70 |
| 9,800 | 75 | 75 |
| 11,550 | 80 | 80 |
| 13,400 | 85 | 85 |
| 15,450 | 90 | 90 |
| 17,650 | 95 | 95 |
| 20,000 | 100 | 100 |
| **Total** | **123,500** | |

## Generation Mechanics

### Potential

Beequips have a potential ranging from 0 to 5 stars. This potential is fixed and cannot change. When displayed in the game, the potential rounds to the nearest star (or half-circle in Dapper Bear's Shop).

Generally, higher potential results in:
*   A better probability of having superior base stats.
*   Easier acquisition of rarer stats when upgrading with waxes.
*   An increased likelihood that a wax upgrade will provide more stat points.

### Base Stats

When a beequip is first generated, or when a Swirled Wax is applied to it, it receives a new set of base stats. Each possible stat has a chance of being included in this set, either with an exact value or within a range defined by two pre-determined limits. This range is biased toward values that may increase with the beequip's potential.

While higher potential generally increases both the likelihood of having a specific base stat and the magnitude of that stat, generation quirks introduce randomization to these probabilities. Internally, this process utilizes a complex function (Module:RQValue).

*Note: Base stats are not dependent on Caustic Wax; it is possible for a beequip to possess a Caustic-only stat as its initial base.*

### Waxes

When a wax is successfully applied, it grants the beequip **wax points**. Each wax point can upgrade exactly one of the beequip's stats. Swirled Waxes do not grant wax points; instead, they reroll every existing wax point on the beequip.

The amount of wax points granted by different waxes is:

| Wax | Wax Points |
| :--- | :---: |
| Soft Wax | 1 |
| Hard Wax | 2 |
| Caustic Wax / Debug Wax | 4 |
| Swirled Wax | 0 |

Every upgradable stat on a beequip has an associated weight value. The probability of a wax point upgrading a specific stat is determined by its weight value divided by the sum of all upgradable stats' weight values. This weight value may increase with the beequip's potential.

When a wax point upgrades a stat, it increases that stat either by an exact amount or within two pre-determined ranges, biased toward higher values as the beequip's potential increases. A stat can only be upgraded a finite number of times; once it reaches its maximum upgrade limit, it is removed from the pool, which subsequently improves the probabilities for upgrading all remaining stats.

Similar to base stats, while higher potential generally favors rarer stats and larger upgrades, generation quirks introduce randomization into the selection process. Internally, this process utilizes a complex function (Module:RQValue).

## Beequip Types

### Non-Event Beeequips
Non-event beequips were introduced on April 1, 2022, and are primarily obtainable from planters (the Dandelion Field offers a significantly higher drop chance than other fields). Examples include Thimble, Sweatband, Bandage, Camo Bandana, Bottle Cap, Kazoo, Smiley Sticker, Whistle, Charm Bracelet, Paperclip, Beret, Bang Snap, Bead Lizard, Pink Shades, Lei, Demon Talisman, Camphor Lip Balm, Autumn Sunhat, Rose Headband, Pink Eraser, and Candy Ring.

### Beesmas Beeequips
Beesmas beequips were added during the 2020 Beesmas event. While they are obtainable only during the Beesmas event period, they remain usable year-round. Examples include Elf Cap, Single Mitten, Warm Scarf, Peppermint Antennas, Beesmas Top, Pinecone, Icicles, Beesmas Tree Hat, Bubble Light, Snow Tiara, Snowglobe, Reindeer Antlers, Toy Horn, Paper Angel, Toy Drum, Lump Of Coal, Poinsettia, Electric Candle, and Festive Wreath.