# Beequip Storage

A **beequip** is an inventory item worn by bees that alters their stats and can provide bonuses to the hive. Beequips can only be given to bees that are at or above the level of the beequip. Some beequips have specific requirements; for instance, the Bubble Light requires a bee with an energy mutation.

## The Beequip Case

When a beequip is obtained, it is initially stored in a **Beequip Case**. From this case, beequips can be given to bees by dragging them to a hive slot, or moved between the case, storage, and inbox.

The Beequip Case is acquired after speaking with Dapper Bear at his shop. Players start with five slots but can expand this capacity through quests from Dapper Bear and during Beesmas 2020 events, reaching a maximum of 15 beequips.

Opening the Beequip Case allows players to view all equipped Beequips on their hives. While viewing other hives is possible, interaction is limited to one's own hive. Clicking or holding an equipped Beequip in the case will cause it to enlarge and sway, visually highlighting its location on the hive slot.

## Beequip Storage

If the slots of the Beequip Case are full, or if the player does not possess a Beequip Case, excess beequips are moved to the **Beequip Storage**. This storage is located near the Dandelion Field or the Public Sticker Board in the Hive Hub. Beequips stored here cannot be given directly to bees.

By default, the storage has 10 slots. Players can purchase up to 90 additional slots for a total maximum of 100 slots, costing 123,500 tickets. Some extra slots may also have been obtained by completing Bee Bear's quests during Beesmas 2020.

If both the storage and case are full, beequips overflow into the **Beequip Inbox**. The inbox can hold the player's 25 most recent beequips, but these items are automatically discarded after a 48-hour time limit. To prevent an item from being deleted, the player must free up a slot in the Beequip Case.

Permanent beequips can be stored in the 'Permanents' section of the Beequip Storage without consuming any space. However, these special items still require a case slot to be equipped to a bee. Previously, items like Reindeer Antlers and Festive Wreath were permanent, but they have since been converted into standard beequips, with developers indicating potential future changes to this feature.

### Storage Capacity Upgrades

| Slots (Storage) | Max Case Slots | Cost (Tickets) |
| :---: | :---: | :---: |
| 10 | 15 | N/A |
| 25 | 20 | 350 |
| 45 | 25 | 800 |
| 70 | 30 | 1,850 |
| 100 | 40 | 3,400 |
| 150 | 45 | 5,550 |
| 200 | 50 | 6,800 |
| 250 | 55 | 9,800 |
| 300 | 60 | 11,550 |
| 350 | 65 | 13,400 |
| 400 | 70 | 15,450 |
| 500 | 75 | 17,650 |
| 600 | 80 | 20,000 |

***

## Beequip Generation Mechanics

This section explains how a Beequip generates its stats. For detailed information on the underlying systems, refer to the linked subarticles.

### Potential

Beequips have a potential rating that ranges from 0 to 5 stars. This potential is permanent and cannot change. When displayed in the game, the potential rounds to the nearest star (or half-circle in Dapper Bear’s Shop).

Generally, higher potential results in:
*   A better probability of having superior base stats.
*   Easier acquisition of rarer stats when upgrading with waxes.
*   A higher probability that a wax upgrade will yield greater stat increases.

### Base Stats

When a beequip is first generated, or after applying a Swirled Wax, it receives a new set of base stats. Each possible stat has a chance of appearing in this set, either at an exact value or within a range defined by two pre-determined limits. This range is biased toward values that may increase with the beequip's potential.

While higher potential generally increases both the likelihood and magnitude of base stats, generation involves randomized quirks, meaning this correlation is not guaranteed. Internally, this process uses a complex function (see `Module:RQValue`).

*Note: Base stats are independent of Caustic Wax; therefore, a beequip can possess a stat typically associated only with Caustic Waxes as its initial base.*

### Waxes

When a wax is applied successfully, it grants the beequip a number of **wax points**. Each point can upgrade exactly one of the beequip's stats. Swirled Waxes do not grant wax points; instead, they reroll every existing wax point on the item.

The amount of wax points provided by different waxes:

| Wax | Wax Points |
| :--- | :---: |
| Soft Wax | 1 |
| Hard Wax | 2 |
| Caustic Wax / Debug Wax | 4 |
| Swirled Wax | 0 |

Every upgradable stat on a beequip has an associated weight value. The probability of a wax point upgrading a specific stat is determined by dividing that stat's weight value by the sum of all upgradable stats' weight values. This weight value may increase with the beequip's potential.

When a wax point upgrades a stat, it increases the stat either by an exact amount or within two pre-determined ranges, biased toward higher values as the potential increases.

A stat can only be upgraded a finite number of times. Once a stat reaches its maximum upgrade limit, it is removed from the pool of upgradable stats, which subsequently improves the probability of upgrading all remaining stats. Similar to base stats, while higher potential generally favors rarer and larger upgrades, generation involves randomization quirks (see `Module:RQValue`).

***

## Beequip Types

### Non-Event Beequips
Non-event beequips were introduced on April 1, 2022, and are primarily obtained from planters. The Dandelion Field offers a significantly higher chance of dropping these items than other fields.

*   Thimble
*   Sweatband
*   Bandage
*   Thumbtack
*   Camo Bandana
*   Bottle Cap
*   Kazoo
*   Smiley Sticker
*   Whistle
*   Charm Bracelet
*   Paperclip
*   Beret
*   Bang Snap
*   Bead Lizard
*   Pink Shades
*   Lei
*   Demon Talisman
*   Camphor Lip Balm
*   Autumn Sunhat
*   Rose Headband
*   Pink Eraser
*   Candy Ring

### Beesmas Beequips
These beequips were added during the Beesmas 2020 event. While they are only obtainable during the Beesmas period, they remain usable year-round.

*   Elf Cap
*   Single Mitten
*   Warm Scarf
*   Peppermint Antennas
*   Beesmas Top
*   Pinecone
*   Icicles
*   Beesmas Tree Hat
*   Bubble Light
*   Snow Tiara
*   Snowglobe
*   Reindeer Antlers
*   Toy Horn
*   Paper Angel
*   Toy Drum
*   Lump Of Coal
*   Poinsettia
*   Electric Candle
*   Festive Wreath