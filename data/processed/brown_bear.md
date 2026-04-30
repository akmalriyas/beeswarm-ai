# Brown Bear

[![Brown](https://static.wikia.nocookie.net/bee-swarm-simulator/images/0/06/Brown.png/revision/latest?cb=20190402221124)](https://static.wikia.nocookie.net/bee-swarm-simulator/images/0/06/Brown.png/revision/latest?cb=20190402221124)

**Overview**
| Attribute | Value |
| :--- | :--- |
| **Species** | Quest Bear |
| **Location** | Near the Clover Field and the Wealth Clock. |
| **Bee Prerequisites** | None |
| **Color Scheme (Fur)** | Fur #634929 / Shade #554026 |
| **Color Scheme (Details)** | Snout: #634929, #C8A77F \| Torso: #785d3d \| Arms: #94744e \| Legs: #634b2f |

Brown Bear is a permanent quest giver and one of eight bears available in the game. The other permanent bears are Black Bear, Mother Bear, Panda Bear, Science Bear, Dapper Bear, Polar Bear, and Spirit Bear. He is located behind the Clover Field and next to the Wealth Clock and the Top Brown Bear Helpers leaderboard. His quests primarily focus on collecting pollen from randomized fields. After completing a quest, a new one becomes available in 1 hour.

## Quest Mechanics
Brown Bear offers infinite quests. These quests require collecting pollen from various fields, with the required amount scaling up in difficulty as the player completes more quests and increases their bee count. Certain quests are only given if the player has reached a minimum number of bees.

### Scaling Formula
The amount of pollen required is defined by the function $P(x)$, where $x$ is a hard-coded value specific to each quest. The value of $P(x)$ scales with the total number of Brown Bear quests the player has completed ($\text{cnt}$).

**Variables:**
*   $\text{cnt}$: Number of Brown Bear quests completed as of claiming the quest.
*   $\text{base} = \lfloor \frac{2500\times x+0.5}{100}\rfloor \times 100$
*   $\text{inc} = \lfloor \frac{5000\times x+0.5}{100}\rfloor \times 100$
*   $\text{max} = \lfloor \frac{10,000,000,000,000\times x+0.5}{100}\rfloor \times 100$

**Calculations:**
1.  $\text{basePollen} = \text{base} + \text{cnt} \times \text{inc}$
2.  Determine $\text{scaling}$:
    *   If $\frac{\text{cnt}}{1000} < 1$: $\text{scaling} = (\frac{\text{cnt}}{1000})^4$
    *   Otherwise: $\text{scaling} = (\frac{\text{cnt}}{1000})^2$
3.  $\text{requiredPollen} = \text{basePollen} + (\text{max} - \text{basePollen}) \times \text{scaling}$
4.  Determine $\text{interval}$: $\text{interval}=10^{\max(\lfloor \log _{10}(\text{requiredPollen})\rfloor -1, 1)}$
5.  $\text{roundedPollen} = \lfloor \frac{\text{requiredPollen}}{\text{interval}}+0.5\rfloor \times \text{interval}$

The function returns $\text{roundedPollen}$.

## Possible Quests
Brown Bear can give a total of 41 different quests.

| Quest Name | Min Bees Required | Requirements |
| :--- | :--- | :--- |
| Brown Bear: Sun-Dand | 0 | Collect $P(0.3)$ Pollen from Sunflower Field. \| Collect $P(0.3)$ Pollen from Dandelion Field. |
| Brown Bear: Mush-Clove | 0 | Collect $P(0.5)$ Pollen from Clover Field. \| Collect $P(0.3)$ Pollen from Mushroom Field. |
| Brown Bear: Bluf-Clove | 0 | Collect $P(0.6)$ Pollen from Clover Field. \| Collect $P(0.3)$ Pollen from Blue Flower Field. |
| Brown Bear: White-Mush | 0 | Collect $P(0.6)$ White Pollen. \| Collect $P(0.3)$ Pollen from Mushroom Field. |
| Brown Bear: White-Bluf | 0 | Collect $P(0.6)$ White Pollen. \| Collect $P(0.3)$ Pollen from Blue Flower Field. |
| Brown Bear: Solo-Clove | 15 | Collect $P(1)$ Pollen from Clover Field. |
| Brown Bear: Straw-Spide | 5 | Collect $P(0.5)$ Pollen from Strawberry Field. \| Collect $P(0.5)$ Pollen from Spider Field. |
| Brown Bear: Bamb-Spide | 5 | Collect $P(0.5)$ Pollen from Bamboo Field. \| Collect $P(0.5)$ Pollen from Spider Field. |
| Brown Bear: White-Bamb-Mush | 5 | Collect $P(0.6)$ White Pollen. \| Collect $P(0.4)$ Pollen from Bamboo Field. \| Collect $P(0.3)$ Pollen from Mushroom Field. |
| Brown Bear: Red-Straw-Sun | 5 | Collect $P(0.6)$ Red Pollen. \| Collect $P(0.3)$ Pollen from Strawberry Field. \| Collect $P(0.2)$ Pollen from Sunflower Field. |
| Brown Bear: Blue-Clov-Spide | 5 | Collect $P(0.6)$ Blue Pollen. \| Collect $P(0.3)$ Pollen from Clover Field. \| Collect $P(0.2)$ Pollen from Spider Field. |
| Brown Bear: Solo-Spide | 5 | Collect $P(1.1)$ Pollen from Spider Field. |
| Brown Bear: Solo-Straw | 5 | Collect $P(1.1)$ Pollen from Strawberry Field. |
| Brown Bear: Solo-Bamb | 5 | Collect $P(1.1)$ Pollen from Bamboo Field. |
| Brown Bear: Blue-Pinap-Clov | 10 | Collect $P(0.8)$ Blue Pollen. \| Collect $P(0.6)$ Pollen from Pineapple Patch. \| Collect $P(0.3)$ Pollen from Clover Field. |
| Brown Bear: Red-Pinap-Dand | 10 | Collect $P(0.8)$ Red Pollen. \| Collect $P(0.6)$ Pollen from Pineapple Patch. \| Collect $P(0.2)$ Pollen from Dandelion Field. |
| Brown Bear: Pinap-Bamb | 10 | Collect $P(0.6)$ Pollen from Pineapple Patch. \| Collect $P(0.5)$ Pollen from Bamboo Field. |
| Brown Bear: Pinap-Straw | 10 | Collect $P(0.6)$ Pollen from Pineapple Patch. \| Collect $P(0.5)$ Pollen from Strawberry Field. |
| Brown Bear: Solo-Cact | 15 | Collect $P(1.1)$ Pollen from Cactus Field. |
| Brown Bear: White-Cact-Sun | 15 | Collect $P(0.8)$ White Pollen. \| Collect $P(0.6)$ Pollen from Cactus Field. \| Collect $P(0.3)$ Pollen from Sunflower Field. |
| Brown Bear: Blue-Pump-Bluf | 15 | Collect $P(0.8)$ Blue Pollen. \| Collect $P(0.6)$ Pollen from Pumpkin Patch. \| Collect $P(0.3)$ Pollen from Blue Flower Field. |
| Brown Bear: Red-Cact-Rose | 15 | Collect $P(0.8)$ Red Pollen. \| Collect $P(0.5)$ Pollen from Cactus Field. \| Collect $P(0.5)$ Pollen from Rose Field. |
| Brown Bear: Blue-Pine-Mush | 15 | Collect $P(0.8)$ Blue Pollen. \| Collect $P(0.6)$ Pollen from Pine Tree Forest. \| Collect $P(0.4)$ Pollen from Mushroom Field. |
| Brown Bear: White-Pine-Straw | 15 | Collect $P(0.8)$ White Pollen. \| Collect $P(0.6)$ Pollen from Pine Tree Forest. \| Collect $P(0.4)$ Pollen from Strawberry Field. |
| Brown Bear: White-Rose-Bamb | 15 | Collect $P(0.8)$ White Pollen. \| Collect $P(0.6)$ Pollen from Rose Field. \| Collect $P(0.4)$ Pollen from Bamboo Field. |
| Brown Bear: Red-Pump-Dand | 15 | Collect $P(0.8)$ Red Pollen. \| Collect $P(0.6)$ Pollen from Pumpkin Patch. \| Collect $P(0.4)$ Pollen from Dandelion Field. |
| Brown Bear: Red-Mount-Mush | 25 | Collect $P(0.8)$ Red Pollen. \| Collect $P(0.7)$ Pollen from Mountain Top Field. \| Collect $P(0.4)$ Pollen from Mushroom Field. |
| Brown Bear: Blue-Mount-Bluf | 25 | Collect $P(0.8)$ Blue Pollen. \| Collect $P(0.7)$ Pollen from Mountain Top Field. \| Collect $P(0.4)$ Pollen from Blue Flower Field. |
| Brown Bear: Solo-Mount | 25 | Collect $P(1.2)$ Pollen from Mountain Top Field. |
| Brown Bear: Mount-Spide-Rose-Pinap | 25 | Collect $P(0.4)$ Pollen from Mountain Top Field. \| Collect $P(0.2)$ Pollen from Spider Field (x3). |
| Brown Bear: Mount-Bamb-Pump-Sun | 25 | Collect $P(0.4)$ Pollen from Mountain Top Field. \| Collect $P(0.2)$ Pollen from Bamboo Field. \| Collect $P(0.2)$ Pollen from Pumpkin Patch. \| Collect $P(0.2)$ Pollen from Sunflower Field. |
| Brown Bear: Blue-Coco-Bluf | 35 | Collect $P(0.8)$ Blue Pollen. \| Collect $P(0.7)$ Pollen from Coconut Field. \| Collect $P(0.4)$ Pollen from Blue Flower Field. |
| Brown Bear: Red-Coco-Mush | 35 | Collect $P(0.8)$ Red Pollen. \| Collect $P(0.7)$ Pollen from Coconut Field. \| Collect $P(0.4)$ Pollen from Mushroom Field. |
| Brown Bear: White-Pepp-Pinap | 35 | Collect $P(0.8)$ White Pollen. \| Collect $P(0.7)$ Pollen from Pepper Patch. \| Collect $P(0.4)$ Pollen from Pineapple Patch. |
| Brown Bear: White-Pepp-Bamb | 35 | Collect $P(0.8)$ White Pollen. \| Collect $P(0.7)$ Pollen from Pepper Patch. \| Collect $P(0.4)$ Pollen from Bamboo Field. |
| Brown Bear: Coco-Pepp-Clove-Pine | 35 | Collect $P(0.3)$ Pollen from Coconut Field. \| Collect $P(0.3)$ Pollen from Pepper Patch. \| Collect $P(0.3)$ Pollen from Clover Field. \| Collect $P(0.3)$ Pollen from Pine Tree Forest. |
| Brown Bear: Coco-Mount-Cact-Rose | 35 | Collect $P(0.3)$ Pollen from Coconut Field. \| Collect $P(0.3)$ Pollen from Mountain Top Field. \| Collect $P(0.3)$ Pollen from Cactus Field. \| Collect $P(0.3)$ Pollen from Rose Field. |
| Brown Bear: Solo-Coco | 35 | Collect $P(1.2)$ Pollen from Coconut Field. |
| Brown Bear: Solo-Stump | 40 | Collect $P(1.2)$ Pollen from Stump Field. |
| Brown Bear: Red-Stump-Mush | 40 | Collect $P(0.8)$ Red Pollen. \| Collect $P(0.7)$ Pollen from Stump Field. \| Collect $P(0.3)$ Pollen from Mushroom Field. |
| Brown Bear: Blue-Stump-Rose | 40 | Collect $P(0.8)$ Blue Pollen. \| Collect $P(0.7)$ Pollen from Stump Field. \| Collect $P(0.3)$ Pollen from Rose Field. |
| Brown Bear: Mount-Spide-Rose-Pinap (Archival) | 25 | Collect $P(0.4)$ Pollen from Mountain Top Field. \| Collect $P(0.2)$ Pollen from Spider Field (x3). |

## Rewards System
Every quest rewards the player with 1 Ticket, increasing amounts of Royal Jelly and Honey based on difficulty. Additionally, every 3 quests grant 3 Jelly Beans. Certain milestones reward other items.

### Royal Jelly Progression Table
| Quests Completed | Royal Jelly Amount |
| :--- | :--- |
| 0-5 | 1 |
| 6-15 | 2 |
| 16-25 | 3 |
| 26-30 | 5 |
| 31-40 | 10 |
| 41-50 | 20 |
| 51-60 | 30 |
| 61-75 | 50 |
| 76-100 | 100 |
| 101-110 | 125 |
| 111-120 | 150 |
| 121-125 | 250 |
| 126-150 | 500 |
| 151-200 | 750 |
| 201-225 | 1,000 |
| 226-250 | 1,500 |
| 251-300 | 2,000 |
| 301-350 | 3,000 |
| 351-400 | 5,000 |
| 401-450 | 7,500 |
| 451-500 | 10,000 |
| 501-525 | 12,500 |
| 526-550 | 15,000 |
| 551-575 | 25,000 |
| 576-600 | 50,000 |
| 601-700 | 100,000 |
| 701-800 | 250,000 |
| 801-900 | 500,000 |
| 901-1,000 | 1,000,000 |
| 1,001-1,250 | 1,250,000 |
| 1,251-1,500 | 1,500,000 |
| 1,501-2,000 | 2,000,000 |
| 2,001-2,250 | 2,250,000 |
| 2,251-2,500 | 2,500,000 |

### Milestone Rewards (Dialogue Triggers)
Bolded quest numbers trigger special dialogue and rewards.

| Quest Number | Reward |
| :--- | :--- |
| 5 | Field Dice x3 |
| 10 | Micro-Converters x5 |
| 15 | Field Dice x5 |
| 20 | Bitterberries x25 |
| **25** | Silver Egg x1 |
| 30 | Micro-Converters x5 |
| 35 | Oil x1 |
| 40 | Bitterberries x50 |
| 45 | Enzymes x1 |
| **50** | Gold Egg x1 |
| 55 | Magic Bean x1 |
| 60 | Bitterberries x50 |
| 65 | Field Dice x5 |
| 70 | Micro-Converters x5 |
| **75** | Diamond Egg x1 |
| 80 | Micro-Converters x10 |
| 85 | Tropical Drink x1 |
| 90 | Star Jelly x1 |
| 95 | Gumdrops x100 |
| **100** | Mythic Egg x1 |
| 105 | Oil x1 |
| 111 | Boxes-O-Frogs x5 |
| 115 | Enzymes x1 |
| 120 | Magic Bean x1 |
| 123 | Shy Brown Bear Sticker x1 |
| 125 | Atomic Treat x1 |
| 130 | Enzymes x1 |
| 135 | Bitterberries x50 |
| 140 | Glue x1 |
| 145 | Field Dice x5 |
| **150** | Tickets x100 |
| 155 | Micro-Converters x5 |
| 160 | Oil x3 |
| 165 | Enzymes x1 |
| 170 | Micro-Converters x5 |
| 175 | Gumdrops x100 |
| 180 | Bitterberries x50 |
| 185 | Oil x1 |
| 190 | Magic Bean x1 |
| 195 | Star Jelly x1 |
| **200** | Mythic Egg x1 |
| 205 | Field Dice x5 |
| 210 | Bitterberries x50 |
| 215 | Micro-Converters x5 |
| 220 | Magic Bean x1 |
| 225 | Atomic Treat x1 |
| 230 | Enzymes x3 |
| 235 | Glue x1 |
| 240 | Gumdrops x100 |
| 245 | Bitterberries x50 |
| **250** | Tickets x250 |
| 255 | Oil x3 |
| 260 | Boxes-O-Frogs x5 |
| 265 | Field Dice x5 |
| 270 | Micro-Converters x5 |
| **275** | Gifted Gold Egg x1 |
| 280 | Magic Bean x1 |
| 285 | Oil x3 |
| 290 | Gumdrops x100 |
| 295 | Bitterberries x50 |
| **300** | Brown Cub x1 (Cub Buddy Skin) |
| 305 | Enzymes x3 |
| 310 | Glue x3 |
| 315 | Star Jellies x3 |
| 320 | Field Dice x5 |
| 325 | Micro-Converters x10 |
| 330 | Bitterberries x75 |
| 333 | Boxes-O-Frogs x3 |
| 335 | Gumdrops x150 |
| 340 | Gold Egg x1 |
| 345 | Magic Beans x3 |
| **350** | Tickets x250 |
| 355 | Enzymes x5 |
| 360 | Oil x5 |
| 365 | Field Dice x5 |
| 370 | Bitterberries x75 |
| 375 | Atomic Treat x1 |
| 380 | Micro-Converters x5 |
| 385 | Micro-Converters x10 |
| 390 | Gold Egg x1 |
| 395 | Glue x5 |
| **400** | Mythic Egg x1 |
| 405 | Gumdrops x50 |
| 410 | Oil x10 |
| 415 | Field Dice x5 |
| 420 | Neonberries x4 |
| **425** | Gifted Diamond Egg x1 |
| 430 | Micro-Converters x10 |
| 435 | Enzymes x10 |
| 440 | Gifted Silver Egg x1 |
| 444 | Boxes-O-Frogs x4 |
| 445 | Magic Beans x3 |
| **450** | Tickets x250 |
| 455 | Magic Beans x5 |
| 460 | Field Dice x7 |
| 465 | Star Jellies x5 |
| 470 | Glue x5 |
| 475 | Boxes-O-Frogs x5 |
| 480 | Oil x15 |
| 485 | Bitterberries x75 |
| 490 | Micro-Converters x15 |
| 495 | Gold Egg x1 |
| **500** | Star Treat x1 |
| 505 | Enzymes x15 |
| 510 | Glue x5 |
| 515 | Field Dice x8 |
| 520 | Tropical Drinks x10 |
| 525 | Diamond Egg x1 |
| 530 | Oil x25 |
| 535 | Magic Beans x5 |
| 540 | Bitterberries x75 |
| 545 | Micro-Converters x15 |
| **550** | Tickets x250 |
| 555 | Boxes-O-Frogs x5 |
| 560 | Gumdrops x200 |
| 565 | Enzymes x25 |
| 570 | Oil x25 |
| 575 | Magic Beans x7 |
| 580 | Star Jellies x10 |
| 585 | Tropical Drinks x15 |
| 590 | Bitterberries x100 |
| 595 | Atomic Treats x3 |
| **600** | Mythic Egg x1 |
| **650** | Tickets x250 |
| **700** | Mythic Egg x1 |
| **750** | Tickets x500 |
| **800** | Mythic Egg x1 |
| **1000** | Star Treats x5 |

## Dialogue Scripts

### Initial Quest Talk
*   **First quest:** "Hey there bud! Ready to get started? The road to an awesome hive is paved by Royal Jelly! If you want to unlock Epic, Legendary, and even Mythic Bees, you'll need Royal Jelly for sure. I've got plenty to share, and not just Royal Jelly... After certain milestones, I'll give all sorts of cool rewards, including Gold, Diamond, and even Mythic Eggs! But those'll come way down the road. For now, let's keep it simple. Check out the quest I've put in your Quest Menu, and report back when you've collected all the pollen."
*   **During:** "Looks like you haven't quite finished my quest yet. Check the quest menu, then collect all of the requested pollen. Come back when the meters are filled all the way up, and I'll give you your prize!"
*   **Completion:** "Great job bud! Here's some Royal Jelly. You've completed [# of Brown Bear quests] of my quests so far. Complete [#] more, and I'll give you [milestone reward]. And if you complete [#] more, I'll give you a [major milestone reward]! I haven't quite finished preparing the next quest for you. Come back to me in [time left], and we'll be ready to roll."

### Repeatable Quests
*   **Welcome:** "Welcome back! You ready for a new quest? Complete it and I'll give you some Royal Jelly - and a Ticket! You've completed [# of Brown Bear quests] of my quests so far. And every new quest becomes a bit more challenging. Check your Quest Menu to see what's up next!"
*   **During:** "Looks like you haven't quite finished my quest yet. Check the quest menu, then collect all of the requested pollen. Come back when the meters are filled all the way up, and I'll give you your prize!"
*   **Completion:** "Great job bud! Here's some Royal Jelly. You've completed [# of Brown Bear quests] of my quests so far. Complete [#] more, and I'll give you [milestone reward]. And if you complete [#] more, I'll give you a [major milestone reward]!"
*   **Past Cooldown:** "Looks like it's been over an hour since I gave you your last quest. Talk to me again when you're ready for the next one."
*   **Cooldown:** "I haven't quite finished preparing the next quest for you. Come back to me in [time left], and we'll be ready to roll."

### Milestone Dialogue
*   **Reaching Major Milestone:** "Great job bud! Here's some Royal Jelly. And, more importantly, a [milestone reward]! You've completed [# of Brown Bear quests] of my quests so far. Complete [#] more, and I'll give you [milestone reward]. And if you complete [#] more, I'll give you a [major milestone reward]!"
*   **Reaching Minor Milestone:** "Great job bud! Here's some Royal Jelly. And, as a bonus: [milestone reward]! You've completed [# of Brown Bear quests] of my quests so far. Complete [#] more, and I'll give you [milestone reward]. And if you complete [#] more, I'll give you a [major milestone reward]!"
*   **Cooldown:** "Remember, I can only give one quest once an hour. I need a bit more time to finish preparing your next reward. Check back with me in [time left], and we'll be ready to go!"

### Beesmas Dialogue (Archival)
*   **2018:** (Upon giving present) "Ah, of course! Time to exchange some Beemas gifts. Let me see what you got me this year... Whoa! A 1-year subscription to Bearmazon Prime! I'll get so much out of this, you have NO idea! Thanks buddy. Here's a little something I know you're gonna love as well."
*   **2020:** (Upon giving present) "But not too cold for us to exchange gifts! SO what is it, huh? What'd you get ol' Brown Bear? Whoa! A 1-year subscription to Bearmazon Prime! I'll get so much out of this, you have NO idea! Thanks bud. Now look at what I got you, including the Royal Jelly Ornament! With this on the Beesmas Tree, you'll receive the following boosts: +25% Convert Rate; +25% Capacity in the Clover Field; and +20% Pollen from "Bomb" abilities! Happy Beesmas!"
*   **2021:** (Upon giving present) "But not too cold for us to exchange gifts! So what is it, huh? What'd you get ol' Brown Bear? Whoa! A 1 year subscription to Bearmazon Prime! I'll get so much out of this, you have NO idea! Thanks bud. Now look at what I got you, including the Royal Jelly Ornament! With that on the Beesmas Tree, you'll receive the following boosts: +25% Convert Rate; +25% Capacity in the Clover Field; And +20% Pollen from "Bomb" abilities! Happy Beesmas!"
*   **2022:** (Upon giving present) "Maybe your present will help warm me up! Can't wait to find out. ...(krumple krumple)... Whoa! A 25$ Ubear Eats gift card! I'm ordering some warm soup and hot cocoa right away. I hope they deliver to ROBLOX games... Thanks bud. Now check out what I got you, some Royal Jelly, a Glue... And the Royal Jelly Ornament! With that on the Beesmas Tree, you'll receive the following boosts: +25% Convert Rate +25% Capacity in the Clover Field And +20% Pollen from "Bomb" abilities! Happy Beesmas!"
*   **2024 Summer:** (Upon giving present) "Man, it's REALLY cold this summer! You got something in that Present that could warm me up? ...(krumple krumple)... Whoa! It's a 90 day membership to Beequinox, the bougiest bee-themed gym around! I think they've even got a steam room! That'll warm me up for sure. Is this you hinting that I need to work out more? Haha! Just playing. Thanks bud! Now check out what I got YOU: the Royal Jelly Ornament! With that on the Beesmas Tree, you'll receive the following boosts: +25% Convert Rate, +25% Capacity in the Clover Field And +20% Pollen from "Bomb" abilities! Happy Beesmas!"
*   **2024 Winter:** (Upon giving present) "Brrrr, it's cold! But not too cold for us to exchange gifts! So what is it, huh? What'd you get ol' Brown Bear? ...(krumple krumple)... Whoa! A 12 month subscription to ChatGPBee! Not sure exactly how I'll use this, but I'll try it out! Maybe it can come up with quests to give you. Or maybe it can just keep me company. Thanks bud! Now look at what I got you, including the Royal Jelly Ornament! With that on the Beesmas Tree, you'll receive the following boosts: +25% Convert Rate +25% Capacity in the Clover Field And +20% Pollen from "Bomb" abilities! Happy Beesmas!"

## Stockings Quests (Archival)
The Brown Bear has hosted several seasonal stocking quests.

**Stockings Quest - 2025:**
*   **Requirements:** Collect 2,500,000 Pollen from the Clover Field. \| Pop 10 Blooms in the Clover Field. \| Complete 10 Rounds in the Retro Swarm Challenge. \| Collect 250 Brick Tokens. \| Collect 5 Field Dice. \| Defeat 25 Ladybugs. \| Defeat 25 Rhino Beetles.
*   **Rewards:** Honey x5,000,000, Tickets x10, Royal Jelly x1, Smooth Dice x1, Snowflakes x25.

**Stockings Quest - 2024 (Winter):**
*   **Requirements:** Collect 750,000 Red Pollen. \| Collect 250,000 Pollen from the Clover Field. \| Defeat 10 Ladybugs. \| Collect 50 Bomb Tokens. \| Collect 3 Field Dice. \| Collect 3 Stickers without Trading.
*   **Rewards:** Honey x4,000,000, Tickets x5, Smooth Dice x1, Hard Wax x1, Gingerbread Bear x1.

**Stockings Quest - 2024 (Summer):**
*   **Requirements:** Collect 200,000 Pollen from the Clover Field with Rare Bees. \| Defeat 10 Ladybugs. \| Collect 50 Brick tokens. \| Obtain 3 Field Dice. \| Obtain 1 Green Plus Sign Sticker.
*   **Rewards:** Honey x1,000,000, Tickets x10, Royal Jelly x3, Whirligigs x3, Red Extract x1, Blue Extract x1, Snowflakes x25.

**Stockings Quest - General (Archival):**
*   **Requirements:** Collect 8,000 Pollen from the Mushroom Field. \| Collect 8,000 Pollen from the Blue Flower Field. \| Defeat 25 Ladybugs. \| Defeat 25 Rhino Beetles. \| Use 1 Field Dice. \| Use 1 Micro-Converter.
*   **Rewards:** Honey x30,000, Royal Jelly x1, Atomic Treat x1, Whirligigs x5, Gingerbread Bear x1.

**Stockings Quest - General (Archival):**
*   **Requirements:** Collect 10,000 Pollen from the Clover Field. \| Collect 7,500 Red Pollen. \| Collect 7,500 Blue Pollen. \| Defeat 3 Ladybugs and 3 Rhino Beetles. \| Collect 25 Ability Tokens.
*   **Rewards:** Honey x30,000, Tickets x3, Royal Jelly x1, Magic Bean x1, Micro-Converters x3, Snowflakes x10.

**Stockings Quest - General (Archival):**
*   **Requirements:** Collect 10,000 Red Pollen. \| Collect 10,000 Pollen from the Dandelion Field. \| Collect 20 Ladybugs and 30 Ability Tokens.
*   **Rewards:** Honey x25,000, Snowflakes x10, Micro-Converters x3, Royal Jelly x1.

## Other Quests (Archival)
This section details various event or specialized quests associated with Brown Bear.

### Waiting With Sun Bear (3/6): And Brown Bear
*   **Requirements:** Earn 3 Clover Badges. \| Use 25 Royal Jellies. \| Collect 12,500,000 Pollen from the Clover Field. \| Collect 5,000,000 Pollen with the Vacuum. \| Collect 250 Tokens from Honeystorms. \| Collect 10 Stingers. \| Collect 5 Hard Waxes. \| Collect 5 Red Extracts. \| Collect 5 Blue Extracts. \| Apply 10 Stacks of Clover Field Boost. \| Defeat 25 Rhino Beetles. \| Defeat 10 Giant Ants.
*   **Rewards:** Honey x50,000,000, Tickets x20, Enzymes x5, Red Balloon x1, Star Jelly x1.

### Waiting With Sun Bear (3/6): And Brown Bear Dialogue
"Hey there bud! Mother Bear sent you, right? No need to explain. Sun Bear told me the whole spiel. Us bears are giving you quests to buy more time for the developer of this game. Well, let's get right into it! I'm not gonna ask questions. This quest out to keep you busy for a while! Guess that quest was too easy! Either that, or Onett is just WAY slower than we thought. Nah. He's always been slow! He's been trying to open some lid up there for over 6 years. Everything lines up! Three more quests to go to earn that Stranded Sun Bear Sticker. I think Polar Bear's got the next one for you."

### Commando Chick's Hideout
*   **Requirements:** Cut the vines. \| Capture 1 Commando Chick.
*   **Rewards (Upon receiving quest):** Rage Bee Jelly x1, Stingers x5.
*   **Dialogue:** "These Chicks are really getting out of hand... The longer we wait, the more dangerous they become! I saw one that look totally mad! It had glowing red eyes, and looked up to no good. Tried to catch it, but it was too fast. It ran away behind the vines near the Wealth Clock. We've got to catch it, but be careful. This is no ordinary Chick... I think it could be armed and dangerous. Here, I'll give you a Rage Bee Jelly and some Stingers to help in the fight."
*   **Completion:** "Phew, that looked intense! Thanks to you, that crazy Chick is back in a basket where it belongs. I think we just might be able to get this Chick infestation under control after all. Great job bud! Here's some rewards for your effort!"

### Brown Bear's Ornament
*   **Requirements:** Collect 25,000 Pollen from the Clover Field. \| Collect 50 Ability Tokens. \| Defeat 5 Ladybugs.
*   **Rewards:** Honey x30,000, Tickets x5, Royal Jelly x1, Royal Jelly Ornament x1.
*   **Dialogue:** "Ho ho ho! Merry Beesmas bud! Can you believe another year has gone by already? They seem to be getting faster and faster. But the year's not complete until the Beesmas Tree is decorated! And I've got a royal idea for an Ornament... I'll start working on it while you finish these tasks: Collect 25,000 Pollen from the Clover Field... Collect 50 Ability Tokens... And defeat 5 Ladybugs!"
*   **Completion:** "That was fast! Ok then, let me just finish up. ...(Snip snip snip)... ...(Glue glue glue)... Oh... didn't quite turn out as I expected. But it'll work! It's a Royal Jelly Ornament! It represents the thousand of Royal Jellies I give out everyday! See, I even drew my face on it. With this on the Beesmas Tree, you'll receive the following boosts: +10% Capacity; x1.15 Pollen from "Bomb" Bee Abilities; And x1.25 Pollen from the Clover Field! Don't forget to keep an eye out for gift boxes hidden around the map. Once you've put enough Ornaments on the tree, they're yours to open! Good luck, and Happy Honeydays!"

### Egg Hunt: Brown Bear
*   **Requirements:** Obtain 3 Plastic Eggs.
*   **Rewards:** Honey x1,500, Marshmallow Bee x1, Micro-Converters x3, Royal Jelly x1.
*   **Dialogue:** "Hey there bud! You here for the Egg Hunt? Well then, let's get right into it! When it comes to Egg Hunts, I like to keep things traditional. I've gone ahead and hidden 3 Plastic Eggs around the map for you to hunt down! Snoop around and check all the nooks and crannys. Some of them are pretty sneaky. Return all 3 to me, and I'll give you a tasty Marshmallow Bee. You'll need 3 of those if you want to earn Bee Swarm's Egg Hunt Egg. Got it? Great! Happy hunting."
*   **During:** "Having trouble? Here's a hint. All 3 of the Plastic Eggs are hidden right here in the starting zone! No need to search behind any of the bee gates. That should save you time."
*   **Completion:** "Great work! I thought I had you with the one in the maze. I'll just take those Plastic Eggs and reuse them next year. And in return - here's one delicious Marshmallow Bee! But don't eat it!! You'll need to turn in 3 for the Egg Hunt Egg."

## Trivia
*   Before the 2020-04-19 Update, Brown Bear's quests only focused on a single Field and were scaled relative to the number of bees in the player's hive.
*   Prior to the 2018-09-10 update, Brown Bear gave a "daily" quest every 16 hours. After this update, it changed to 4 hours. Following the 2020-04-19 update, he began giving quests every hour.
*   A Royal Jelly token is located on a hill behind Brown Bear. Players can reach it by having high Jump Power or by using a Parachute/Glider from the top of the Blue HQ roof.
*   He is one of three permanent Bears in the Starter Zone, alongside Black Bear and Mother Bear.
*   Brown Bear, Polar Bear, and Black Bear are the only bears with infinite quests. Brown Bear is typically the first bear to start giving endless quests for new players and is one of six quest givers that give repeating quests.
*   He is the only bear who guarantees Royal Jelly and Tickets upon completing each quest.
*   Brown Bear uses the Knight Animation Package, the same as Sun Bear.
*   He was listed as "Nice" in 2018 by Bee Bear during the Beesmas 2018 Event. If a player gave him a Present during that event, he would give a Star Jelly and Clover Field Boost x4.
*   The Brown Cub rewarded for completing 300 quests is one of six Cub Buddy skins. Lipsisas was the first player to obtain this skin.
*   The Beesmas 2020 present dialogue merged elements from the 2018 and 2019 events.
*   Brown Bear is unique in that he is the only NPC who can receive the same Present twice.
*   He is the only infinite quest bear whose quests scale in difficulty.
*   Excluding event quests, Black Bear and Brown Bear are the only bears that *only* require pollen collection for their tasks.
*   If a player acquires the Brown Cub Buddy without owning any Cub Buddy first, they must obtain the Black Cub as it acts as necessary "equipment."
*   Brown Bear is stated to have known Spirit Bear since he was a cub and is described by Spirit Bear as being very reserved.
*   He is one of three Bears (along with Robo Bear and Bee Bear) who can give out a Cub Buddy.
*   Brown Bear visited the Wind Shrine, as revealed by Spirit Bear, though his purpose there remains unknown.
*   Black Bear states that Brown Bear spends most of his time near the Clover Field, which coincidentally is above King Beetle’s Lair. Black Bear also suggests this may relate to Brown Bear's Royal Jelly stockpile.