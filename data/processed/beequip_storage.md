# Beequips and Storage

A **beequip** is an inventory item worn by bees that alters their stats and can provide bonuses to the hive. Beequips can only be equipped on bees that are at or above the level of the beequip. Some beequips have specific requirements; for example, the Bubble Light requires a bee with an energy mutation.

## The Beequip Case

When a beequip is obtained, it is initially stored in a **Beequip Case**. Equipping items involves dragging the beequip from the case to a hive slot, or moving them between the case, storage, and inbox.

The Beequip Case is acquired by speaking with Dapper Bear at his shop. Players start with five slots but can increase this capacity through quests given by Dapper Bear and Bee Bear during Beesmas 2020, eventually reaching a maximum of 15 slots.

Opening the Beequip Case allows players to view all equipped beequips across their hives, though interaction is limited to the player's own hive. Clicking or holding an equipped beequip in the case causes it to enlarge and sway, highlighting its location on the hive slot.

## Beequip Storage

If the slots in the Beequip Case are full, or if the player does not possess a Beequip Case, excess beequips are moved to the **Beequip Storage**. This storage is located near the Dandelion Field or the Public Sticker Board in the Hive Hub. Beequips stored here cannot be given directly to bees.

By default, the storage has 10 slots. Players can purchase up to 90 additional slots for a total of 100, costing 123,500 tickets. Additional slots may also have been obtained by completing certain quests during Beesmas 2020.

If both the Beequip Case and the Beequip Storage are full, beequips overflow into the **Beequip Inbox**. The inbox holds the player's 25 most recent beequips, but these items are automatically discarded after a 48-hour time limit. To prevent an item from being deleted from the inbox, the player must free up a slot in the Beequip Case.

Permanent beequips can be stored in the 'Permanents' section of the Beequip Storage without occupying space. However, these special items still require a case slot to be equipped. Previously, items like Reindeer Antlers and Festive Wreath were permanent, but they have since been converted into standard beequips.

### Storage Capacity Upgrades
| Slots (Storage) | Case Slots | Cost (Tickets) |
| :---: | :---: | :---: |
| 10 | 15 | N/A |
| 100 | 20 | Varies |
| 250 | 25 | Varies |
| 450 | 30 | Varies |
| 800 | 35 | Varies |
| 1,250 | 40 | Varies |
| 1,850 | 45 | Varies |
| 2,550 | 50 | Varies |
| 3,400 | 55 | Varies |
| 4,400 | 60 | Varies |
| 5,550 | 65 | Varies |
| 6,800 | 70 | Varies |
| 8,250 | 75 | Varies |
| 9,800 | 80 | Varies |
| 11,550 | 85 | Varies |
| 13,400 | 90 | Varies |
| 15,450 | 95 | Varies |
| 17,650 | 100 | Varies |
| **Total** | **123,500** |

## Beequip Generation Mechanics

This section details how a beequip generates its stats and upgrades. For detailed technical explanations, refer to the linked subarticles on generation modules.

### Potential
Beequips have a potential ranging from 0 to 5 stars. This potential is permanent and cannot change. When displayed in-game, the potential rounds to the nearest star (or half-circle).

Higher potential generally correlates with:
*   A better probability of having superior base stats.
*   An easier chance of acquiring rarer stats when upgrading with waxes.
*   A higher probability that a wax upgrade will yield increased stats.

### Base Stats
When a beequip is first generated, or when a Swirled Wax is applied to it, it receives a new set of base stats. Each possible stat has a chance of being included in this set, either with an exact value or within a range defined by two predetermined limits. This range is biased toward values that may increase with the beequip's potential.

While higher potential generally increases both the likelihood and magnitude of base stats, generation quirks mean these probabilities are randomized. Internally, this process utilizes a complex function (Module:RQValue). Base stats are not dependent on Caustic Wax; it is possible for a stat exclusive to Caustic Waxes to appear in the base stats.

### Waxes
The main article on [Waxes] provides general information. When a wax is applied successfully, it grants the beequip **wax points**. Each point can upgrade exactly one of the beequip's stats. Swirled Waxes do not grant points but instead reroll every existing wax point on the beequip.

| Wax | Wax Points Granted |
| :---: | :---: |
| Soft Wax | 1 |
| Hard Wax | 2 |
| Caustic Wax / Debug Wax | 4 |
| Swirled Wax | 0 |

Every upgradable stat has a weight value. The probability of a wax point upgrading a specific stat is determined by its weight value divided by the sum of all upgradable stats' weight values. This weight may increase with the beequip's potential.

When a wax point upgrades a stat, it increases that stat by either an exact value or within two predetermined ranges, biased toward higher values as the beequip's potential increases. A stat can only be upgraded a certain number of times; once this limit is reached, the stat is removed from the upgrade pool, which improves the probability of upgrading other stats. Similar to base stats, while higher potential generally favors rarer stats and larger upgrades, generation quirks introduce randomization. Internally, this process also uses a complex function (Module:RQValue).

## Gallery
*   A beequip in the Beequip Storage or Case.
*   Clicking the level for a beequip.
*   Clicking the color for a beequip.
*   Clicking the limit for a beequip.
*   Clicking the potential for a beequip.
*   Clicking the Beesmas icon for a Beesmas beequip.
*   A beequip token's old design, with an orange color.
*   A beequip token's current design, with a green color.
*   A permanent beequip in a player's Beequip Case prior to the 2024-05-23 update.

## Available Beequips

Beequips are categorized by their acquisition method: Non-Event or Beesmas Event.

### Non-Event Beequips
These were added on April 1, 2022, and can be obtained from planters (the Dandelion Field offers a higher drop chance).
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
These were introduced during Beesmas 2020 and are only obtainable during the event, though they remain usable year-round.
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