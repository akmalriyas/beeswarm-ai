# Amulets

An **amulet** is an item introduced in the 2018-07-11 update. These items grant various buffs to the player and/or their bees, and are obtained by completing specific challenges.

## Obtaining Amulets

When a player collects an amulet, a table appears displaying the statistics of both the old and new amulets, along with options to keep the current amulet or replace it. The scheme provided below illustrates this comparison, showing the player's current amulet type alongside other rewards. If the amulet was obtained from the Ant Challenge or Stick Bug Challenge, the corresponding score is displayed above the reward table.

*   Clicking "**Keep Old**" retains the player's existing amulet.
*   Clicking "**Replace**" triggers a confirmation message asking if the player wishes to swap amulets. If confirmed, the old amulet is permanently replaced by the new one; this action cannot be reversed. Note that all drops associated with the challenge are received regardless of whether the amulet was replaced.

If multiple reward tables are displayed simultaneously, previous tables close, and the newest table becomes active.

**Update History:**
*   As of the 2020-06-06 update, a confirmation message now appears if a player attempts to replace an amulet they already possess.
*   As of the 2021-12-26 update, disconnecting while an amulet choice is undecided allows the player another chance to select their amulet upon rejoining the server.

## Generation Mechanics

Amulets are generated with a specific quality level, which is influenced by various actions (e.g., different challenge scores yield proportionally different qualities, up to a limit). Increasing an amulet's quality improves the probability of receiving a higher-quality amulet, though this does not eliminate the possibility of receiving a lower one.

The generation process involves two main stages: choosing stats and determining stat strength.

### Choosing Stats

An amulet's statistics are grouped, and during generation, the system selects a number of stats from each group to place on the item. Some stat groups only appear based on specific probabilities.

After a stat is selected, the game checks if that stat has an independent probability of appearing (different from its parent stat group). If so, it may randomly remove itself from the amulet based on this secondary probability. This mechanism explains why some amulets may possess fewer stats than initially expected. Currently, this selection process is not influenced by the amulet's quality level.

### Determining Stat Strength

Once a stat is picked, its strength is calculated before being assigned to the player. The final strength of these stats is heavily influenced by the amulet's overall quality. Quality places a strong bias toward a certain value, making it more likely that the stat's strength will be close to that bias.

**Bias Calculation:**
Every stat possesses a `bias` table consisting of two values: `biasQuality` and `biasDirect`.

*   A higher `biasQuality` increases how much the amulet's quality affects the stat's final bias, and vice versa.
*   A higher `biasDirect` directly influences the stat's bias, irrespective of the amulet's quality.
*   The default value for both variables (if not assigned by the game) is 1.

The bias is calculated using the following formula:
$$\text{bias} = \text{minValue} + (\text{maxValue} - \text{minValue}) \times \text{biasDirect} \times {\frac{\text{quality}}{\max(1, \text{biasQuality} \times (1-\text{quality}))}}$$

After calculating the bias, the `RandomBias` function is called with parameters:
`randomBias(minValue, maxValue, bias, 1)`

The resulting value is then rounded to the stat's resolution interval to finalize the stat's strength. For detailed information on this function, see the designated module page.

## Amulet Types

*   [King Beetle Amulet]
*   [Star Amulet]
*   [Ant Amulet]
*   [Moon Amulet]
*   [Shell Amulet]
*   [Stick Bug Amulet]
*   [Cog Amulet]

## Gallery and Visuals

**Equip New Amulet Confirmation:**
*(Image showing the confirmation message when replacing an amulet.)*

**Undecided Amulet Disconnection Message:**
*(Image showing the message displayed upon server re-entry after disconnecting with an undecided amulet.)*

**Visual Bug Report:**
*(Image illustrating a visual bug where Supreme Star and Ant Amulets appear black.)*

## Trivia

Supreme amulets are unique in that they exhibit slight color changes. Occasionally, a rare visual bug causes a supreme amulet to appear entirely black; the cause of this anomaly is currently unknown.