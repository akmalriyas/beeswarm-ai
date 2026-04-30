# Goo

Patches of Goo cover various fields in Bee Swarm Simulator. This purple-to-teal substance provides players with bonus honey when spread across flowers.

Goo is a crucial resource required for several quests, including those associated with Onett, Spirit Bear, Gummy Bear, Gifted Riley Bee, Gifted Bucko Bee, and Science Bear.

### Mechanics

**Acquiring Goo:**
The easiest method to manually obtain goo is by using gumdrops. To collect existing goo, players must gather pollen from flowers that are covered in the substance, utilizing tools, bees, or ability tokens.

**Goo Properties:**
*   Unlike ability tokens, goo can be freely shared with other players.
*   Collecting goo depletes the underlying flowers but does not consume the goo itself, unless it is collected using a Gummyballer.
*   Goo puddles naturally disappear over a short period of time.

**Bonus Honey Formula:**
The amount of bonus honey gained from collecting goo is determined by the size of the puddle. The formula is:

$$ \text{Bonus Honey} = p\sqrt{\frac{f}{200}} $$

Where:
*   $p$ = Amount of pollen collected from the goo puddle.
*   $f$ = Number of flowers inside the goo puddle.

This indicates that larger puddles yield significantly more bonus honey. For instance, collecting 500,000 pollen from a puddle containing 80 flowers grants approximately 316,228 bonus honey.

### Trivia and Advanced Mechanics

*   **Gummy Cannon:** Gummy Bear's Gummy Cannon can shoot gumdrops (which turn into goo) at all fields except the Mountain Top Field, Ant Field, Hub Field, and Brick Fields. Gummy Bear cycles through 13 eligible fields in a random order, announcing his target field via server notification and chat.
    *   The cannon does not always aim precisely; sometimes gumdrops land outside the field boundaries, causing them to vanish or potentially spill into adjacent fields.
*   **Disappearance:** If a gumdrop falls outside of a field and fails to land on a flower, it disappears.
*   **Gummy Abilities:** Both Gummy Bee's Glob ability and Gumdrop Barrage ability are capable of spreading goo in fields.
*   **Gummy Mask:** Activating the Gummy Morph passive ability while wearing the Gummy Mask covers the entire field the wearer is currently occupying with goo.
*   **Visual Coloration:** The color of the goo (pink or teal) is determined by the specific flower it falls upon. This coloration is purely visual and does not affect the amount of honey earned. For example, a specific corner flower in Dandelion Field will always produce pink goo, while another specific corner flower will always produce teal goo.