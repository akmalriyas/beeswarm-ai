# Amulet

An **amulet** is an item introduced in the [2018-07-11 update](/wiki/Updates#2018-07-11 "Updates"). These items grant various buffs to the player and their bees, and they can be obtained by completing specific challenges.

## Obtaining Amulets

When an amulet is collected, a table appears displaying the stats of both the old and new amulets, along with options to keep or replace the current one. If the amulet was earned from the Ant Challenge or Stick Bug Challenge, the player's score will be displayed above the rewards.

*   **Keep Old:** The player retains their current amulet.
*   **Replace:** A confirmation message appears asking if the player wishes to swap amulets. If confirmed, the old amulet is permanently replaced by the new one; this action cannot be reversed. Note that all drops associated with the challenge are received regardless of whether the amulet was replaced.

If multiple tables are displayed, previous ones close, and the newest table takes precedence.

*   As of the [2020-06-06 update](/wiki/Updates#2020-06-06 "Updates"), a confirmation message now appears if the player attempts to replace an amulet they already possess.
*   As of the [2021-12-26 update](/wiki/Updates#2021-12-26 "Updates"), disconnecting while an amulet choice is undecided allows the player another chance to choose upon rejoining a server.

## Generation Mechanics

Amulets are generated with a specific quality, which changes based on actions taken (e.g., different scores yield proportionally different qualities, up to a limit). Increasing an amulet's quality improves the probability of obtaining a better amulet, though it does not eliminate the possibility of receiving a worse one.

### Choosing Stats

An amulet's stats are drawn from multiple predefined stat groups. When generated, the system selects a number of stats from each group. Some stat groups only appear with a certain probability.

After a stat is selected, the game checks if it has an independent probability of appearing (different from its parent stat group). If so, the stat may randomly be removed from the amulet based on this secondary probability, which can result in amulets having fewer stats than expected. Currently, this selection process is not influenced by the amulet's quality.

### Determining Stat Strength

The strength of the picked stats is determined through a complex process heavily influenced by the amulet's quality. The quality places a heavy bias on a target value, making it more likely that the stat's final strength will be near that bias.

Each stat possesses a `bias` table consisting of two values: `biasQuality` and `biasDirect`.
*   A higher `biasQuality` increases how much the amulet's overall quality affects the stat's bias, and vice versa.
*   A higher `biasDirect` directly influences the stat's bias, regardless of the amulet's quality.
*   The default value for both variables is 1 if not explicitly assigned by the game.

The final bias is calculated using the following formula:

$$\text{bias} = \text{minValue} + (\text{maxValue} - \text{minValue}) \times \text{biasDirect} \times {\frac{\text{quality}}{\max(1, \text{biasQuality} \times (1-\text{quality}))}}$$

After calculating the bias, the `RandomBias` function is called with parameters:
`randomBias(minValue, maxValue, bias, 1)`

The resulting value is then rounded to the stat's resolution interval to determine the final stat strength. For detailed information on this function, see [Module:RandomBias](/wiki/Module:RandomBias).

## Available Amulets

*   [King Beetle Amulet](/wiki/King_Beetle_Amulet)
*   [Star Amulet](/wiki/Star_Amulet)
*   [Ant Amulet](/wiki/Ant_Amulet)
*   [Moon Amulet](/wiki/Moon_Amulet)
*   [Shell Amulet](/wiki/Shell_Amulet)
*   [Stick Bug Amulet](/wiki/Stick_Bug_Amulet)
*   [Cog Amulet](/wiki/Cog_Amulet)

## Gallery

### Confirmation Message
This image shows the confirmation message that appears when a player attempts to replace their amulet.

### Undecided Amulet Rejoin Message
This image displays the message shown to a player who joins a server after disconnecting while an amulet choice was undecided, giving them another chance to choose.

### Visual Bug Example
This image illustrates a visual bug where Supreme Star and Ant Amulets incorrectly appear colored black.

## Trivia

*   Supreme amulets are unique in that they slightly change color.
*   Occasionally, a rare visual bug causes a supreme amulet to display as black; the cause of this bug is currently unknown.