# Beequip Case and Storage

A **beequip** is an inventory item worn by bees that alters their stats and can provide bonuses to the hive. Beequips can only be equipped onto bees at or above the level of the beequip. Some beequips have specific requirements; for example, the Bubble Light requires a bee with an energy mutation.

## The Beequip Case

When a beequip is obtained, it is initially stored in a **Beequip Case**. Items within this case can be given to bees by dragging them to a hive slot, or moved between the case, general storage, and inbox.

The Beequip Case is acquired after the player first speaks with Dapper Bear at his shop. Players start with five slots but can increase their capacity through quests from Dapper Bear and during Beesmas 2020 events, reaching a maximum of 15 beequip slots.

Opening the Beequip Case allows players to view all equipped Beequips across everyone's hives, though interaction is limited to the player's own hive. Clicking or holding an equipped Beequip in the case highlights its location on the hive slot by making it enlarge and sway; simply viewing the item from the hive slot does not trigger this effect.

## Beequip Storage and Inbox

If all slots in the Beequip Case are filled, beequips are automatically moved to the **Beequip Storage**. This storage is located near the Dandelion Field or the Public Sticker Board in the Hive Hub. Items in the general storage *cannot* be given directly to bees.

The default storage capacity is 10 slots. Players can purchase up to 90 additional slots, bringing the maximum total capacity to 100, for a cost of 123,500 Tickets. Additional slots may also have been obtained by completing certain quests during Beesmas 2020.

If both the Beequip Case and the general storage are full, beequips overflow into the **Beequip Inbox**. The inbox holds the player's 25 most recent beequips, but these items are automatically discarded after a 48-hour time limit if not acted upon. To prevent an item in the inbox from being deleted, the player must empty a slot in their Beequip Case.

**Permanent Beequips:**
Special beequips can be stored in the 'Permanents' section of the Beequip Storage without consuming any space. However, these items still require a case slot to be equipped onto a bee. Previously, items like Reindeer Antlers and Festive Wreath were permanent, but they have since been converted into standard beequips.

**Storage Capacity Chart:**
| Tickets | Storage Slots (Max) | Case Slots (Max) |
| :---: | :---: | :---: |
| 10 | 15 |
| 250 | 20 |
| 450 | 25 |
| 800 | 30 |
| 1,250 | 35 |
| 1,850 | 40 |
| 2,550 | 45 |
| 3,400 | 50 |
| 4,400 | 55 |
| 5,550 | 60 |
| 6,800 | 65 |
| 8,250 | 70 |
| 9,800 | 75 |
| 11,550 | 80 |
| 13,400 | 85 |
| 15,450 | 90 |
| 17,650 | 95 |
| 20,000 | 100 |

## Beequip Generation Mechanics

### Potential
Beequips possess a potential rating ranging from 0 to 5 stars. This potential is fixed and cannot change. When displayed in the game, the potential rounds to the nearest star (or half-circle in Dapper Bear’s Shop).

Generally, higher potential beequips have:
*   A better probability of possessing superior base stats.
*   An easier chance of acquiring rarer stats when upgraded using waxes.
*   A higher probability that a wax upgrade will grant more stat points.

### Base Stats
When a beequip is first generated or when a Swirled Wax is applied, it receives a new set of base stats. Each potential stat on the item has a chance to appear in this set, either with an exact value or within a range defined by two predetermined limits. This value is biased toward a target that may increase based on the beequip's potential.

While higher potential generally increases both the likelihood and magnitude of base stats, generation randomness means this correlation is not guaranteed. Internally, this process utilizes complex functions (see Module:RQValue).

*Note: Base stats are independent of Caustic Wax; it is possible for a beequip to possess a stat typically associated with Caustic Waxes as its initial base.*

### Waxes
Waxes are used to upgrade the beequip. Each successful application grants the item a number of **wax points**. Swirled Waxes do not grant wax points, but they reroll all existing applied wax points.

The amount of wax points granted varies by type:

| Wax Type | Wax Points Granted |
| :--- | :---: |
| Soft Wax | 1 |
| Hard Wax | 2 |
| Caustic Wax / Debug Wax | 4 |
| Swirled Wax | 0 |

**Upgrading Stats:**
Every upgradable stat on a beequip has an associated weight value. The probability that a wax point upgrades a specific stat is calculated by dividing that stat's weight value by the sum of all upgradable stats' weight values. This weight value may increase with the beequip's potential.

When a wax point successfully upgrades a stat, it increases the stat either by an exact amount or within a range defined by two predetermined limits, biased toward higher values as the beequip's potential increases.

A stat can only be upgraded a finite number of times. Once a stat reaches its maximum upgrade limit, it is removed from the pool of upgradable stats, which in turn improves the probability distribution for upgrading the remaining stats. Similar to base stats, while higher potential generally favors rarer and larger upgrades, generation randomness applies. Internally, this process also uses complex functions (see Module:RQValue).

## Beequip Types
Beequips are categorized by how they are obtained:

**Non-Event Beequips:**
These items were introduced on April 1, 2022, and can be found in planters. The Dandelion Field offers a significantly higher chance of dropping these items than other fields.
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

**Beesmas Beequips:**
These items were added during the Beesmas 2020 event and are only obtainable during subsequent Beesmas events, though they remain usable year-round.
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