# Gifted Riley Bee NPC

Riley Bee is a permanent quest-giving NPC located in Red HQ. For information on the standard worker bee version, see [Riley Bee].

## Overview
| Attribute | Detail |
| :--- | :--- |
| **Species** | Bee NPC |
| **Location** | Red HQ (on the roof) |
| **Prerequisites** | Must have 15 bees and discovered 4 types of red bees. |

Gifted Riley Bee is one of three permanent Quest Bees, alongside Gifted Bucko Bee and Honey Bee. The player requires a [Translator] (obtained from Science Bear three times) to interact with or complete quests for this NPC.

**Milestone Unlocks:**
*   Completing 150 quests unlocks the crafting of the **Heat-Treated Planter**.
*   Completing 250 quests unlocks the crafting of the **Dark Scythe**.

## Quest Mechanics
Gifted Riley Bee is an infinite quest giver. Quests scale in difficulty based on the player's progress.

**Variable Definition:** For all requirements below, $X$ represents the number of quests the player has completed for Gifted Riley Bee plus 1 ($X = \text{Quests Completed} + 1$). Requirements not represented by a formula are static.

### Standard Quests
| Quest Name | Requirements |
| :--- | :--- |
| **Riley Bee: Abilities** | Collect $1000 + 15 \times (X - 1)$ Red Ability Tokens. |
| **Riley Bee: Booster** | Collect $500 + 5 \times (X - 1)$ Red Boost Tokens.<br>Use the Red Field Booster 1 Time. |
| **Riley Bee: Clean-up** | Collect $250,000 \times X$ Goo from Mushroom Field.<br>Collect $250,000 \times X$ Goo from Strawberry Field.<br>Collect $250,000 \times X$ Goo from Rose Field. |
| **Riley Bee: Extraction** | Collect $1,000,000 \times X$ Red Pollen from Clover Field.<br>Collect $1,000,000 \times X$ Red Pollen from Cactus Field.<br>Collect $1,000,000 \times X$ Red Pollen from Pumpkin Patch. |
| **Riley Bee: Goo** | Collect $2,500,000 \times X$ Goo from Red Flowers. |
| **Riley Bee: Medley** | Collect $250 + 5 \times (X - 1)$ Red Ability Tokens.<br>Collect $500,000 \times X$ Goo from Strawberry Field.<br>Collect $3,000,000 \times X$ Pollen from Rose Field. |
| **Riley Bee: Mushrooms** | Collect $3,000,000 \times X$ Pollen from Mushroom Field. |
| **Riley Bee: Petals** | Catch $250 + 10 \times \lfloor (X - 1) / 4 \rfloor$ Red Bloom Petals.<br>Catch $10 + 5 \times \lfloor (X - 1) / 20 \rfloor$ Red Bloom Petals in Clover Field.<br>Catch 10 Red Bloom Petals in Spider Field. |
| **Riley Bee: Picnic** | Collect $1,000,000 \times X$ Pollen from Mushroom Field.<br>Collect $25 + 5 \times \lfloor X / 10 \rfloor$ Strawberry Tokens.<br>Feed $25 + 5 \times \lfloor X / 50 \rfloor$ Strawberries to your Bees.<br>Defeat $5 + 10 \times \lfloor X / 10 \rfloor$ Fire Ants. |
| **Riley Bee: Pollen** | Collect $10,000,000 \times X$ Red Pollen. |
| **Riley Bee: Rampage** | Collect $25 + (X - 1)$ Rage Tokens.<br>Defeat 10 Ladybugs.<br>Defeat $25 + 5 \times \lfloor X / 25 \rfloor$ Fire Ants. |
| **Riley Bee: Roses** | Collect $7,500,000 \times X$ Pollen from Rose Field. |
| **Riley Bee: Scavenge** | Collect $2,500,000 \times X$ Red Pollen.<br>Collect $500 + 5 \times (X - 1)$ Red Ability Tokens.<br>Collect $25 + 10 \times \lfloor X / 10 \rfloor$ Strawberry Tokens. |
| **Riley Bee: Skirmish** | Collect $1,250,000 \times X$ Pollen from Mushroom Field.<br>Defeat 10 Ladybugs. |
| **Riley Bee: Strawberries** | Collect $5,000,000 \times X$ Pollen from Strawberry Field. |
| **Riley Bee: Tango** | Collect $2,500,000 \times X$ Red Pollen.<br>Collect $500 + 5 \times (X - 1)$ Red Ability Tokens.<br>Defeat 5 Scorpions. |
| **Riley Bee: Tour** | Collect $1,000,000 \times X$ Pollen from Mushroom Field.<br>Collect $1,000,000 \times X$ Pollen from Strawberry Field.<br>Collect $1,000,000 \times X$ Pollen from Rose Field.<br>Defeat 5 Ladybugs.<br>Defeat 3 Scorpions. |

### Rewards System
Rewards vary based on the number of quests completed ($Q = X$). All completions grant one Red Extract and Honey.

**Honey Calculation:** The amount of honey received is determined by the highest value in this table:
| Quest Milestone | Honey Amount |
| :--- | :--- |
| Every 100th quest | $25,000,000 \times Q$ |
| Every 5th quest | $2,500,000 \times \lfloor Q^{0.95} \rfloor$ |
| All other quests | $1,000,000 \times \lfloor Q^{0.9} \rfloor$ |

**Milestone Rewards:** Specific thresholds grant additional items:
*   **3 Quests:** 1 Stinger
*   **9 Quests:** 10 Stingers
*   **25 Quests:** 1 Star Jelly
*   **50 Quests:** 1 Gifted Gold Egg
*   **64 Quests:** 1 Basic Red Hive Skin
*   **75 Quests:** 10 Stingers
*   **100 Quests:** 1 Gifted Diamond Egg
*   **111 Quests:** 500 Strawberries
*   **125 Quests:** 10 Stingers
*   **150 Quests:** 20 Stingers, Access to Heat-Treated Planter
*   **175 Quests:** 10 Stingers
*   **200 Quests:** 20 Stingers
*   **222 Quests:** 100,000 Treats
*   **250 Quests:** 1 Gifted Diamond Egg, Access to Dark Scythe

**Probabilistic Rewards (Non-Milestone):**
*   If the quest rank is divisible by 25: Reward includes a Star Jelly.
*   Else, if the quest rank is divisible by 5: A reward item is selected from the table below.
*   Any other quest has a 5% chance of receiving an item from the table below.

| Item | Amount | Chance to be Picked |
| :--- | :--- | :--- |
| Treats | $(1 + \lfloor \sqrt{Q} \rfloor \times 25)$ | ~23.175% |
| Royal Jelly | $(1 + \lfloor \sqrt{Q} \rfloor \times 5)$ | ~17.381% |
| Gumdrops | 25 | ~11.587% |
| Strawberry | $(1 + \lfloor Q^{0.25} \rfloor \times 10)$ | ~11.587% |
| Ticket | 5 | ~11.587% |
| Stinger | 5 | ~11.587% |
| Magic Bean | 3 | ~11.587% |
| Stinger | 10 | ~1.159% |
| Red Extract | 10 | ~0.116% |
| Enzymes | 10 | ~0.116% |
| Stinger | 10 | ~0.116% |

## Dialogue Logs

### Initial Talk
> BzzzzZZz buzz Bzz. Bzz BZZ bz buzzz zz!! (Gifted Riley Bee is speaking in buzzes) — You leave —
> Bzz buzz?! — You use the translator —
> Get this thing out of my face!! ... Whoa - you understood me? I'm speaking with a beekeeper! That's radder than a Rad Bee!! I'm Riley Bee, Leader of the Red Bees. And this is the Red Headquarters! Here, the Red Bees and I coordinate, plan, train, and strategize... We've discovered how to boost the red flower fields! We've developed highly advanced Red Guards! That's why WE'RE the best. Red ROCKS - Blue just can't keep up! You look like a promising Red Beekeeper! But to truly become a Red Master, you'll need some guidance. Complete my quests, and I'll reward you with some Red Extracts! Those can be used to boost your red pollen collection... Or to craft some of our state-of-the-art red equipment! Each time you perform a quest for me, they'll become more difficult. But every once in a while, you may just earn yourself some RIGHTEOUS rewards! Sound good? OK! Talk to me again when you're ready to start.

### Repeatable Quest Dialogue
**Accepting:**
> It's time for another red-related quest. Complete it, and you'll be 1 step closer to becoming a Red Master! AND - you'll earn yourself a Red Extract! Red Extracts boost red pollen by x1.25 for 10 minutes... And they're used to craft some radical red equipment. After every 5th quest, I'll give you a bonus... And every once in a while - that bonus may be HUGE!!!! I've loaded the next quest into your Quest Menu. Get it done and report back!

**During:**
> Each time you complete one of my quests, they get harder! Harder and harder - they just keep going!!! Want to know why? CAUSE RED BEES DON'T QUIT! That's why WE'RE ON TOP!!! Go out there and finish my quest!

**Completion:**
> Right on right on right on!!! Good work out there, you're advancing the red cause! Here's a Red Extract to help you advance even more!! We gotta keep working, keep on fighting... Keep on keeping on to keep ahead of the Blue Bees! RED RULES!!!!!

### Exclusive Beesmas Dialogue
**2018:** (Upon receiving a present)
> GET OUT!!!!!!. Awee, see, I was right when I took you to be a fine beekeeper. And a good person too! So what'd you get me?? ... RIGHT ON! It's a strawberry scented air freshener! The kind you hang on the reer view mirror of a car. I don't have a car, and I can't smell it very well out here... BUT I LOVE IT! Here, here - this is for you. MERRY BEESMAS from the Red Bees at the Red Headquarters!

**2020:** (Upon receiving a present)
> NUH-UH! You didn't! You DID! Let me open it, let me open it! ...(krumple krumple)... OH. MY. GOSH! It's a bPad Air. 4th generation!!! The newest model! Bubble Bee Man must have gotten my letter this year. He went all out! I can use this to play ROBLOX, and Bee Swarm Simulator! Man, now I feel silly. I got a gift too, bit it's not even in the same league. I hope you like it anyways. It includes the Electric Candle Ornament! With this on the Beesmas Tree, you'll receive the following boosts: +25% Convert Rate, +25% Capacity in the Rose Field and Mushroom Field, and +10% Pollen from Flames! Merry Beesmas! Now if you'll excuse me, I've gotta setup my bPad, oh boy oh boy.

**2021:** (Upon receiving a present)
> NUH-UH! You didn't! You DID! Let me open it, let me open it! ...(krumple krumple)... Whaaat? It's a Dark Scythe!!!! How on earth did you afford this? Do you realize how rare these are? We've only got 1 in the whole HQ! Man, now I feel silly. I got you a gift too, but it's not even in the same league. Hope you'll like it anyways. It includes the Electric Candle Ornament! With that on the Beesmas Tree, you'll receive the following boosts: +25% Convert Rate, +25% Capacity in the Rose Field and Mushroom Field, and +10% Pollen from Flames! Merry Beesmas! Now if you'll excuse me, I've gotta setup my bPad, oh boy oh boy.

**2022:** (Upon receiving a present)
> WHAT! A GIFT? No way! Youuuuuuuu Well hand it over! Come on! ...(krumple krumple)... Oh... my... gumdrops... A permanent Precise Mark! How did you get this?? Did it just, like, fail to despawn? Man, I know some beekeepers who would DIE for one of these. This is going to raise the Red HQ straight to the top! I got you something too. Not quite as OP though. It's the Electric Candle Ornament! With that on the Beesmas Tree, you'll receive the following boosts: +25% Convert Rate, +25% Capacity in the Rose Field and Mushroom Field, and +10% Pollen from Flames! Now let's get out there and heat up the Honeydays! RED ROCKS!

**2024 Summer:** (Upon receiving a present)
> What's that in your hands?? GET OUT!! A present for me? What could it be?! ...(krumple krumple)... WOOOOW! It's a whole book of Red Palm Hand Stickers! How many are in here??? Like 50? This is crazy! I'm going to stick these all over the HQ. And if I don't want to talk to someone I'll just stick one of these on them. And I'll say "talk to the hand", LOL! That'll be awesome! Thanks so much! And hey. I got YOU a present too... It's the Electric Candle Ornament! With that on the Beesmas Tree, you'll receive these boosts: +25% Convert Rate, +25% Capacity in the Rose Field and Mushroom Field, and +15% Pollen from Flames! That should heat things up for the Honeydays!

**2024 Winter:** (Upon receiving a present)
> NUH-UH! You didn’t! You DID! Let me open it, let me open it! ...(krumple krumple)... Alright! Some rechargeable wing warmers!!! Between these and the candles, I MIGHT be able to make it through this stupid, cold, long winter. Just barely. Thank you!! Now here's your gift: the Electric Candle Ornament! With that on the Beesmas Tree, you’ll receive these boosts: +25% Convert Rate, +25% Capacity in the Rose and Mushroom Field, and +15% Pollen from Flames! Merry Beesmas! Now if you’ll excuse me, I’m gonna go warm up my flappers.

## Historical Event Quests (Beesmas/Honeyday Candles)

### Riley Bee's Honeyday Candles (2025)
**Requirements:**
*   Collect 500,000,000 Pollen from Rose Field.
*   Collect 50,000,000 Pollen from Red Brick Field.
*   Catch 1,000 Red Bloom Petals.
*   Catch 100 Scarlet Bloom Petals.
*   Use 25 Soft Waxes.
*   Use 25 Hard Waxes.
*   Spawn 5,000 Flames.
*   Defeat 5 Fire Ants.

**Rewards:**
*   2,000,000,000 Honey
*   25 Tickets
*   25 Red Extracts
*   1 Red Balloon
*   5 Swirled Waxes
*   1 Electric Candle
*   5 Gingerbread Bears
*   Access to Honeyday Candles

**Dialogue:**
**Accepting:** "This is the worst Beesmas ever! It's so cold the Fire Bees can't even ignite the flowers. Demon Bee is threatening to return to the underworld. And Spicy Bee's engine is freezing up! The Blue Bees are trying to make it even WORSE with their Snow Machine! But there's still hope... if we can ignite the Honeyday Candles. They'll provide enough heat to get Red HQ operational again. But we'll need your help! Hurry up, before we all freeze to death!"
**Completion:** "Hurry hurry hurry, light them up! Everyone look! The beekeeper's lighting the candles! Yaaaaaaaaaaay! We're saved! With the Honeyday Candles lit, the Red Bes are back in action! Now every 4 hours, you can use it to recruit 3 temporary Red Bees for 30 minutes... And it'll also give you some Wax! Usually Soft Wax, but sometimes rarer ones! It's pretty rad! Well, thanks for bringing warmth back to Beesmas. Tell Bucko Bee the Snow Machine is powerless now! Happy Honeydays!"

### Honeyday Candles (2024 Winter)
**Requirements:**
*   Collect 1,000,000,000 Red Pollen.
*   Collect 300,000,000 Pollen from Rose Field.
*   Collect 200,000,000 Pollen from Cactus Field.
*   Collect 50,000,000 Pollen with Scythe.
*   Collect 500 Red Boost Tokens.
*   Spawn 1,000 Flames.
*   Collect 50 Soft Waxes.
*   Collect 10 Hard Waxes.
*   Defeat 10 Fire Ants.
*   Pop 1 Rare Puffshroom in the Rose Field.

**Rewards:**
*   2,500,000,000 Honey
*   10 Tickets
*   25 Red Extracts
*   1 Caustic Wax
*   3 Red Balloons
*   5 Gingerbread Bears
*   Access to Honeyday Candles

**Dialogue:**
**Accepting:** "This is the worst Beesmas ever! It's so cold the Fire Bees can't even ignite the flowers. Demon Bee is threatening to return to the underworld. And Spicy Bee's engine is freezing up! The Blue Bees are trying to make it even WORSE with their Snow Machine! But there's still hope... if we can ignite the Honeyday Candles. They'll provide enough heat to get Red HQ operational again. But we'll need your help! Hurry up, before we all freeze to death!"
**Completion:** "Go go go! Light em up! Everyone look! The beekeeper's lighting the candles! Yaaaaaaaaaaay! We won't freeze to death! With the Honeyday Candles lit, the Red Bees are back in action! Now every 4 hours, you can use it to recruit 3 temporary Red Bees for 30 minutes... And it'll also give you some Wax! Usually Soft Wax, but sometimes rarer ones! Thank you so much! Now I can finally start enjoying Beesmas! And I hope you can as well! Have fun out there! Just don't you dare help Bucko Bee with that Snow Machine, got it?"

### Honeyday Candles (2024 Summer)
**Requirements:**
*   Collect 10,000,000 Goo from Red Flowers.
*   Collect 5,000,000 Pollen with Scythe.
*   Collect 10,000,000 Pollen from Red Brick Field.
*   Collect 30 Tokens from Red Clay Planters.
*   Spawn 250 Flames.
*   Use 10 Soft Waxes.
*   Obtain 4 Blowing Leaf or 4 Waxing Crescent Moon Stickers to give to Riley Bee.
*   Obtain 1 Scythe Sticker to give to Riley Bee.
*   Obtain 1 Red Palm Hand, 1 Alert Icon or 3 Small Flame Sticker to give to Riley Bee.

**Rewards:**
*   50,000,000 Honey
*   25 Tickets
*   25 Red Extracts
*   1 Star Jelly
*   1 Electric Candle
*   2 Red Balloons
*   5 Gingerbread Bears
*   Access to Honeyday Candles

**Dialogue:**
**Accepting:** "WHY is it so COLD in the summer??? It just ain't right. Is this some sort of sick joke? The flowers are going to DIE if it keeps snowing like this! It's just not right. Not natural. Everything's falling apart around here! What the heck did Bucko Bee do? The Blue Bees have really gone too far this time. At least we've got these candles. Once we light them up, it'll be a little warmer... But I can't leave my post so I'll need you to do it! Completing this quest should ignite their flames. But please hurry! I'm freezing my wings off!"
**Completion:** "Go go go! Light 'em up! Everyone look! The beekeeper's lighting the candles! Yaaaaaaaaaaay! We won't freeze to death! With the Honeyday Candles lit, the Red Bees are back in action! Now every 4 hours, you can use it to recruit 3 temporary Red Bees for 30 minutes... And it'll also give you some Wax! Usually Soft Wax, but sometimes rarer ones! Thank you so much! Now I can finally start enjoying Beesmas! And I hope you can as well! Have fun out there! Just don't you dare help Bucko Bee with that Snow Machine, got it?"

### Honeyday Candles (2022)
**Requirements:**
*   Collect 50,000,000 Red Pollen.
*   Collect 8 Hours of Invigorating Nectar.
*   Collect 100 Soft Waxes.
*   Spawn 1000 Flames.
*   Defeat 10 Fire Ants.

**Rewards:**
*   100,000,000 Honey
*   1 Robo Pass
*   1 Invigorating Vial
*   10 Red Extracts
*   1 Red Balloon
*   5 Gingerbread Bears
*   Access to Honeyday Candles

**Dialogue:**
**Accepting:** "This is the worst Beesmas ever! It's so cold the Fire Bees can't even ignite the flowers. Demon Bee is threatening to return to the underworld. And Spicy Bee's engine is freezing up! The Blue Bees are trying to make it even WORSE with their snow machine! But there's still hope...if we can ignite the Honeyday Candles. They'll provide enough heat to get Red HQ operational again. But we'll need your help! Hurry up, before we all freeze to death: Collect 50,000,000 Red Pollen... Collect 8 hours of Invigorating Nectar... Collect 100 Soft Waxes... Spawn 1,000 Flames... And defeat 10 Fire Ants!"
**Completion:** "Hurry hurry hurry, light them up! Everyone look! The beekeeper's lighting the candles! Yaaaaaaaaaaay! We're saved! With the Honeyday Candles lit, the Red Bees are back in action! Now every 4 hours, you can use it to recruit 3 temporary Red Bees for 30 minutes... And it'll also give you some Wax! Usually Soft Wax, but sometimes rarer ones! Waxes can be used to improve a bee's Beequip. Beequips with higher potential are more likely to roll better stats. If you have a beequip with high potential and want to test your luck, test one out. To use a Wax, just drag it to the hive slot of the bee holding the Beequip you want to alter. It's pretty rad! Well, thanks for bringing warmth back to Beesmas. Tell Bucko Bee the Snow Machine is powerless now! Happy Honeydays!"

### Honeyday Candles (2021)
**Requirements:**
*   Collect 100,000,000 Red Pollen.
*   Defeat 5 Rare Puffshrooms on Mushroom Field.
*   Defeat 5 Rare Puffshrooms on Strawberry Field.
*   Defeat 5 Rare Puffshrooms on Rose Field.
*   Collect 4 Hours of Satisfying Nectar from Planters.
*   Collect 4 Hours of Invigorating Nectar from Planters.
*   Spawn 250 Flames.
*   Use 10 Soft Waxes.

**Rewards:**
*   250,000,000 Honey
*   5 Tickets
*   1 Ticket Planter
*   5 Gingerbread Bears
*   25 Red Extracts
*   1 Caustic Wax
*   3 Oils
*   Access to Honeyday Candles

**Dialogue:**
**Accepting:** "This is the worst Beesmas ever! It's so cold the Fire Bees can't even ignite the flowers. Demon Bee is threatening to return to the underworld. And Spicy Bee's engine is freezing up! The Blue Bees are trying to make it even WORSE with their Snow Machine! But there's still hope... if we can ignite the Honeyday Candles. They'll provide enough heat to get Red HQ operational again. But we'll need your help! Hurry up, before we all freeze to death: Collect 100,000,000 Red Pollen... Defeat 5 Rare Puffshrooms on the Mushroom Field... Defeat 5 Rare Puffshrooms on the Strawberry Field... Defeat 5 Rare Puffshrooms on the Rose Field... Collect 4 hours of Satisfying Nectar... Collect 4 hours of Invigorating Nectar... Spawn 250 Flames... And use 10 Soft Wax."
**Completion:** "Hurry hurry hurry, light them up! Everyone look! The beekeeper's lighting the candles! Yaaaaaaaaaaay! We're saved! With the Honeyday Candles lit, the Red Bees are back in action! Now every 4 hours, you can use it to recruit 3 temporary Red Bees for 30 minutes... And it'll also give you some Wax! Usually Soft Wax, but sometimes rarer ones! Waxes can be used to upgrade a Bee's Beequip. Beequips with higher potential are more likely to roll better stats. If you have a beequip with high potential and want to test your luck, test them out! To use a Wax, just drag it to the hive slot of the bee holding the Beequip you want to alter. It's pretty rad! Well, thanks for bringing warmth back to Beesmas. Tell Bucko Bee the Snow Machine is powerless now! Happy Honeydays!"

### Honeyday Candles (2023)
**Requirements:**
*   Collect 150,000,000 Red Pollen.
*   Collect 50,000,000 Pollen from Mushroom Field.
*   Collect 50,000,000 Pollen from Pineapple Patch.
*   Spawn 500 Flames.
*   Collect 500 Red Bomb tokens (Note: Dialogue references defeating 50 Scorpions).
*   Use 5 Oils.

**Rewards:**
*   250,000,000 Honey
*   5 Gingerbread Bears
*   5 Field Dice
*   5 Red Extracts
*   Access to Honeyday Candles

**Dialogue:**
**Accepting:** "This is the worst Beesmas ever! It's so cold the Fire Bees can't even ignite the flowers. Demon Bee is threatening to return to the underworld. And Spicy Bee's engine is freezing up! The Blue Bees are trying to make it even WORSE with their Snow Machine! But there's still hope... if we can ignite the Honeyday Candles. They'll provide enough heat to get Red HQ operational again. But we'll need your help! Hurry up, before we all freeze to death: Collect 150,000,000 Red Pollen... Collect 50,000,000 Pollen from the Mushroom Field... Collect 50,000,000 Pollen from the Pineapple Patch... Spawn 500 Flames... Defeat 50 Scorpions [or collect 500 red bomb tokens]... And use 5 Oils!"
**Completion:** "Hurry hurry hurry, light them up! Yaaaaaaaaaaay! We're saved! With the Honeyday Candles lit, the Red Bees are back in action! Now every 4 hours, you can use it to recruit 3 temporary Red Bees for 30 minutes... And it'll also give you a Swirled Wax! Swirled Waxes can be used to re-roll the stats of a Bee's Beequip, for better or worse. Beequips with higher potential are more likely to roll better stats. If you have a beequip with high potential and want to test your luck, test them out! To use a Swirled Wax, just drag it to the hive slot of the bee holding the Beequip you want to alter. It's pretty rad! Well, thanks for bringing warmth back to Beesmas. Tell Bucko Bee the Snow Machine is powerless now! Happy Honeydays!"

### Other Quests
**Riley Bee's Ornament (2019):**
*   **Requirements:** Collect 250,000,000 Red Pollen; Collect 100,000,000 Red Pollen from Cactus Field; Collect 500 Strawberry Tokens; Defeat 25 Scorpions; Defeat 10 Fire Ants; Use the Red Field Booster 5 Times.
*   **Rewards:** 250,000,000 Honey, 5 Tickets, 5 Red Extracts, Electric Candle Ornament.

**Egg Hunt (2019):**
*   **Requirements:** Collect 10,000,000 Goo from Rose Field; Collect 2,500,000 Red Pollen from Clover Field; Collect 200 Strawberry Tokens; Collect 800 Red Bomb Tokens; Collect 5 Red Jelly Bean Tokens; Defeat 50 Fire Ants.
*   **Rewards:** 15,000,000 Honey, 10 Red Extracts, 10 Stingers, 5 Field Dice, 5 Jelly Beans, x7 Mushroom Field Boost (Max stack is x5).

## Trivia & Lore Notes
*   Since quest requirements are randomized, the formula for the first requirement of any quest uses $X$ multiplied by $(\text{Number of Gifted Riley Bee quests completed} + 1)$.
*   Gifted Riley Bee is one of three NPCs based on bees (along with Gifted Bucko Bee and Honey Bee NPC).
*   Riley Bee was the first and only quest giver located in Red HQ.
*   A visual glitch existed where Riley Bee appeared wingless when viewed through the glass roof over Red HQ, but this was fixed in the 2019-09-28 Update when the glass roof was removed.
*   Riley Bee's dialogue regarding the Honeyday Candles (2021) initially stated a Swirled Wax reward per use, but candles can drop various waxes; Swirled Waxes are rare. This change occurred before the 2021-12-26 Update when Swirled Wax was the only wax available and given after every use.
*   The second half of the Beesmas 2021 present dialogue is repeated from Beesmas 2020's, referencing setting up the bPad.
*   "bPad" is a phonetic reference to the iPad, with the 'i' replaced by a 'b' due to Riley Bee being a bee.