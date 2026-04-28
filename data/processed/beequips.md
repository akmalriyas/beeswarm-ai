# Beequips

A **beequip** is a type of inventory item that can be worn by bees, altering their stats and providing bonuses to the hive. Beequips can only be given to bees that are at or above the level of the beequip. Some beequips have specific requirements; for example, the Bubble Light requires a bee with an energy mutation.

## The Beequip Case

When a beequip is obtained, it is initially stored in a **Beequip Case**. Equipping items from this case involves dragging the beequip to a hive slot, or moving them between the case, storage, and inbox.

The Beequip Case is acquired by speaking with Dapper Bear at his shop. Players start with five slots but can expand this capacity through quests given by Dapper Bear and Bee Bear during Beesmas 2020, allowing for a maximum of 15 beequips in the case.

Opening the Beequip Case allows players to view all equipped Beequips across their hives, though interaction is limited to their own hive. Clicking or holding an equipped Beequip within the case will cause it to enlarge and sway, highlighting its location on the hive slot.

## Beequip Storage

If the slots in the Beequip Case are full, or if the player does not possess a Beequip Case, excess beequips are moved to the Beequip Storage. This storage is located near the Dandelion Field or the Public Sticker Board in the Hive Hub. Beequips stored here cannot be given to bees.

By default, the storage has 10 slots. Players can purchase up to 90 additional slots for a total of 100, costing 123,500 tickets. Additional slots may also have been obtained by completing Bee Bear's quests during Beesmas 2020.

If both the Case and Storage are full, beequips move into the Beequip Inbox. The inbox holds the player's 25 most recent beequips but has a strict 48-hour time limit before they are automatically discarded. To prevent an item from being deleted, the player must free up a slot in the Case.

Permanent beequips can be stored in the 'Permanents' section of the Beequip Storage without consuming space. However, these special items still require a case slot to be equipped. Previously permanent items (like Reindeer Antlers and Festive Wreath) were converted into normal beequips, with Onett noting that the permanent feature might be removed entirely.

### Storage Slot Costs
| Slots | Tickets Required |
| :---: | :---: |
| 10 | Default |
| 15 | N/A (Quest Reward) |
| 20 | 250 |
| 25 | 450 |
| 30 | 800 |
| 35 | 1,250 |
| 40 | 1,850 |
| 45 | 2,550 |
| 50 | 3,400 |
| 55 | 4,400 |
| 60 | 5,550 |
| 65 | 6,800 |
| 70 | 8,250 |
| 75 | 9,800 |
| 80 | 11,550 |
| 85 | 13,400 |
| 90 | 15,450 |
| 95 | 17,650 |
| 100 | 20,000 |
| **Total** | **123,500** |

## Generation Mechanics

### Potential
Beequips have a potential ranging from 0 to 5 stars. This potential is fixed and cannot change. When displayed, the potential rounds to the nearest star (or half-circle in Dapper Bear’s Shop). Generally, higher potential results in:
*   A better probability of having superior base stats.
*   Easier acquisition of rarer stats when upgrading with waxes.
*   A higher probability that a wax upgrade will grant more stats.

### Base Stats
When a beequip is generated or receives a Swirled Wax, it is assigned new base stats. Each possible stat has a chance of being included in this set, either as an exact value or within a range defined by two predetermined limits. This range is biased toward values that may increase with the beequip's potential.

While higher potential generally increases both the likelihood and magnitude of base stats, generation quirks mean probabilities are randomized. Internally, this process uses a complex function (see Module:RQValue). Base stats are not dependent on Caustic Wax; it is possible for a stat exclusive to Caustic Waxes to appear in the initial base stats.

### Waxes
When successfully applied, a wax grants the beequip **wax points**. Each point can upgrade exactly one of the beequip's stats. Swirled Waxes do not grant points but reroll every existing wax point on the item.

The amount of wax points granted varies by type:

| Wax | Wax Points |
| :--- | :---: |
| Soft Wax | 1 |
| Hard Wax | 2 |
| Caustic Wax / Debug Wax | 4 |
| Swirled Wax | 0 |

Every upgradable stat has a weight value. The probability of a wax point upgrading a specific stat is determined by its weight divided by the sum of all upgradable stats' weight values. This weight may increase with the beequip's potential.

When a wax point upgrades a stat, it increases that stat by either an exact value or within two predetermined ranges, biased toward higher values associated with the item's potential. A stat can only be upgraded a finite number of times; once its maximum upgrade limit is reached, it is removed from the pool, which improves the probabilities for upgrading other stats.

Similar to base stats, while higher potential generally favors rarer stats and larger upgrades, generation quirks ensure that the probability selection remains randomized. Internally, this process uses a complex function (see Module:RQValue).

## Beequip Types

Beequips are categorized by how they are obtained: Non-Event or Beesmas.

### Non-Event Beequips
These were introduced on April 1, 2022, and can be found in planters (with a higher drop chance in the Dandelion Field).
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
These beequips were added during the Beesmas 2020 event. While they are only obtainable during the event, they remain usable year-round.
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