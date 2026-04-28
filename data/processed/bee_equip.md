# Beequip Guide

A **beequip** is a type of inventory item that can be worn by bees, altering their stats and providing bonuses to the hive. When equipping a beequip, the target bee must be at or above the level required by the item. Some beequips have specific requirements; for example, the Bubble Light requires a bee with an energy mutation.

## The Beequip Case

When obtained, beequips are initially stored in a **Beequip Case**. Items within this case can be given to bees by dragging them to a hive slot, or moved between the case, general storage, and inbox.

The Beequip Case is acquired after speaking with Dapper Bear at his shop. Players start with five slots but can expand this capacity through quests from Dapper Bear and Bee Bear during Beesmas 2020, eventually reaching a maximum of 15 slots.

Opening the case allows players to view all equipped beequips across their hives, though interaction is limited to the player's own hive. Clicking or holding an equipped beequip in the case highlights its location on the hive slot by making it enlarge and sway.

## Beequip Storage

If the Beequip Case slots are full, or if the player does not possess a Case, excess beequips are moved to the **Beequip Storage**. This storage is located near the Dandelion Field or the Public Sticker Board in the Hive Hub. Items in this general storage cannot be given directly to bees.

By default, the storage holds 10 slots. Players can purchase up to 90 additional slots for a total of 100, costing 123,500 tickets. Some extra slots may also have been obtained through Bee Bear's quests during Beesmas 2020.

If both the Case and Storage are full, beequips default to the **Beequip Inbox**. The inbox holds the player's 25 most recent items but has a strict 48-hour time limit before automatic disposal. To prevent an item from being deleted, players must free up a slot in the Beequip Case.

**Permanent Beeequips:**
Special beequips can be stored in the 'Permanents' section of the Storage without consuming space. However, these items still require a case slot to be equipped onto a bee. Previously, items like Reindeer Antlers and Festive Wreath were permanent, but they have since been converted into standard beequips.

**Storage Capacity Tiers:**
| Tickets | Case Slots | Storage Slots |
| :---: | :---: | :---: |
| 10 | 15 | 10 |
| 20 | 15 | 25 |
| 30 | 15 | 45 |
| 40 | 15 | 80 |
| 50 | 15 | 125 |
| 60 | 15 | 185 |
| 70 | 15 | 255 |
| 80 | 15 | 340 |
| 90 | 15 | 440 |
| 100 | 15 | 555 |
| 115 | 15 | 680 |
| 135 | 15 | 825 |
| 155 | 15 | 980 |
| 175 | 15 | 1155 |
| 200 | 15 | 1340 |

## Generation Mechanics

### Potential
Beequips possess a potential ranging from 0 to 5 stars. This potential is fixed and cannot change. When displayed, the potential rounds to the nearest star (or half-circle in Dapper Bear's Shop).

Generally, higher potential leads to:
*   A better probability of having superior base stats.
*   Easier acquisition of rarer stats when upgrading with waxes.
*   An increased likelihood that a wax upgrade will yield higher stat increases.

### Base Stats
When a beequip is first generated or upgraded using a Swirled Wax, it receives a new set of base stats. Each possible stat has a chance to appear in this set, either at an exact value or within a range defined by two limits. These ranges are biased toward values that may increase with the beequip's potential.

While higher potential generally increases both the likelihood and magnitude of base stats, generation is randomized due to complex internal functions (detailed in Module:RQValue). Importantly, base stats are not dependent on specific waxes; a Caustic-only stat can appear as a base stat even if no Caustic Wax has been applied.

### Waxes
Waxes grant **wax points** upon successful application. Each wax point can upgrade exactly one of the beequip's stats. Swirled Waxes do not provide wax points but reroll every existing wax point on the item.

The value of waxes is as follows:

| Wax | Wax Points |
| :--- | :---: |
| Soft Wax | 1 |
| Hard Wax | 2 |
| Caustic Wax / Debug Wax | 4 |
| Swirled Wax | 0 |

**Stat Upgrading:**
Every upgradable stat has a weight value. The probability of a wax point upgrading a specific stat is determined by its weight divided by the sum of all upgradable stats' weights. This weight may increase with the beequip's potential.

When an upgrade occurs, the stat increases by either an exact amount or within two pre-determined ranges, biased toward values that rise with the item's potential. A stat can only be upgraded a finite number of times; once it reaches its maximum limit, it is removed from the pool, which improves the probability of upgrading other available stats.

## Beequip Types

Beeequips are categorized by how they are acquired:

### Non-Event Beequips
These items were introduced on April 1, 2022, and can be obtained primarily from planters (the Dandelion Field offers a higher drop chance).
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
These items were added during the Beesmas 2020 event. While they are only obtainable during the Beesmas period, they remain usable year-round.
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