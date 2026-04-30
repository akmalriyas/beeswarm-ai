# Wealth Clock

[![The Wealth Clock.](https://static.wikia.nocookie.net/bee-swarm-simulator/images/e/e0/Wealth_Clock.png/revision/latest?cb=20180910204647)](https://static.wikia.nocookie.net/bee-swarm-simulator/images/e/e0/Wealth_Clock.png/revision/latest?cb=20180910204647) [](/wiki/File:Wealth_Clock.png)

The **Wealth Clock** is a machine that boosts Honey Per Pollen and grants tickets to the player. It is located next to the Brown Bear, the entrance to Commando Chick's Hideout, and the Honeystorm Summoner.

## Mechanics and Usage

To use the Wealth Clock, the player must have discovered 5 different types of bees. The clock can only be used once every hour of playtime.

**Honey Per Pollen Boost:**
Each use grants a x1.01 Honey Per Pollen increase, which stacks up to 5 times, resulting in a maximum boost of x1.05 Honey Per Pollen.

**Ticket Rewards:**
The clock awards tickets based on usage:
*   **First Use (Stack 1):** Awards 1 ticket.
*   **Subsequent Uses (Stacks 2-5):** The amount awarded increases by 1 for each subsequent use, capping at 5 tickets per use.
*   **Fifth Use Onward:** The clock is fully powered and consistently awards 5 tickets per hour.

The in-game notifications vary based on the usage level:

**(First Four Times)**
> 🕒 The Wealth clock has powered up... 🕒
> It increases Honey made from pollen by #%.
> It printed a Ticket/# Tickets!
> Come back in 1 hour and it'll print #!
> Remember, it resets if you leave the game.
> +# Ticket (from Wealth Clock)

**(Fifth Time Onward)**
> 🕒 The Wealth clock is fully powered! 🕒
> It prints 5 Tickets per hour!
> Remember, it resets if you leave the game.
> +5 Tickets (from Wealth Clock)

## Notes and Trivia

*   **Grace Period:** There is a 15-minute grace period before the Wealth Clock buff resets. A player can exit and rejoin within this window to maintain the boost. However, joining during this period will reset the cooldown back to one hour.
    *   *Note:* This reset can be bypassed by entering the hive hub and then leaving the game; the clock will not reset in this scenario.
*   **Code Redemption:** The Wealth Clock boost can also be obtained by redeeming certain codes, such as `FrogFix` (which activates Wealth Clock x5 plus other effects).
*   **Location History:** The Wealth Clock was previously located where the Honeystorm Summoner used to be.
*   **Update Changes (November 25, 2018):** Since this update, the clock increases the number of tickets printed per interval. It now starts printing tickets immediately upon use, but the player must remain in the server for a full hour to utilize the boost (instead of the previous 30-minute cooldown).
*   **Ticket Calculation:** The amount of tickets granted is based on the player's current stack of the Wealth Clock buff, not strictly how many times they have used it. For example, if a player has 1 stack and uses the clock for the first time, they will receive 2 tickets instead of 1.
*   **Badges:** The Playtime Badge is represented by the Wealth Clock.
*   **Sticker Chance:** The Wealth Clock has a 1/250 (0.4%) chance to spawn an Hourglass Sticker in the Clover Field.

### Ticket Earning Formula

The total number of tickets earned over $x$ hours can be represented by the following piecewise function:

$$
f(x)=
\begin{cases}
0 & \text{if } 0\leq x<1 \\
1 & \text{if } 1\leq x<2 \\
3 & \text{if } 2\leq x<3 \\
6 & \text{if } 3\leq x<4 \\
10 & \text{if } 4\leq x<5 \\
5x-10 & \text{if } x\geq 5
\end{cases}
$$