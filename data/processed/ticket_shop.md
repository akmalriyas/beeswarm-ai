# Ticket Shop

[ ![TicketShop-0](https://static.wikia.nocookie.net/bee-swarm-simulator/images/f/fa/TicketShop-0.png/revision/latest?cb=20180604171105) ](https://static.wikia.nocookie.net/bee-swarm-simulator/images/f/fa/TicketShop-0.png/revision/latest?cb=20180604171105 "TicketShop-0")

## Overview
The Ticket Shop is a specialized shop located outside the Mountain Top Shop, situated to the right of the Field Booster. Its primary function is selling Tickets for Honey.

### Mechanics and Pricing
The shop sells tickets in increments of 1, 10, 100, and 500. It features a black semicircle with a grey separator that functions as a rotary dispenser mechanism.

Like other shops (such as the Basic Egg Shop, Royal Jelly Shop, Stinger Shop, and Treat Shop), it shares a similar appearance, but is distinguished by having a ticket icon on its front and sides. A key mechanic of this shop is that the price for subsequent tickets increases with each purchase.

To calculate the cost of the next ticket, you can refer to the official spreadsheet or use the following formula:

$$P(n)=\begin{cases}100{,}000+1000n^{1.2},&{\text{for }}1\leq n\leq 500\\\100{,}000+1000n^{1.7},&{\text{for }}n\geq 501\end{cases}$$

Where:
*   $P(n)$ is the price of the $n$-th ticket purchased from the shop.
*   $n$ is the total number of tickets already bought.

## Trivia
*   The cost calculation formula was updated during the 2018-11-25 update.