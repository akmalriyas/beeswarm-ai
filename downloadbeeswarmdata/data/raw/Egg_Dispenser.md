# Egg dispenser

## Basic Egg Shop

[ ![Egg Shop](https://static.wikia.nocookie.net/bee-swarm-simulator/images/9/9b/Egg_Shop.png/revision/latest/scale-to-width-down/267?cb=20180604172559) ](https://static.wikia.nocookie.net/bee-swarm-simulator/images/9/9b/Egg_Shop.png/revision/latest?cb=20180604172559 "Egg Shop") The Basic Egg Shop

## Information

### Usage

Obtaining [Hive Slots](/wiki/Hive_Slot "Hive Slot") through ![Basic Egg](https://static.wikia.nocookie.net/bee-swarm-simulator/images/f/fa/Basic_Egg.png/revision/latest/scale-to-width-down/25?cb=20230404043532)[Basic Eggs](/wiki/Egg#Basic_Egg "Egg")

### Requirement(s)

![Honey](https://static.wikia.nocookie.net/bee-swarm-simulator/images/c/c6/Honey.png/revision/latest/scale-to-width-down/25?cb=20230410071605)[Honey](/wiki/Honey "Honey") (varies)

### Cooldown

None

### Location

Between the [Sunflower Field](/wiki/Sunflower_Field "Sunflower Field") and the [Dandelion Field](/wiki/Dandelion_Field "Dandelion Field")

  
The **Basic Egg Shop** is a [shop](/wiki/Category:Shops "Category:Shops") located next to the [Sunflower Field](/wiki/Sunflower_Field "Sunflower Field") and behind an [Instant Converter](/wiki/Instant_Converter "Instant Converter"). It sells ![Basic Egg](https://static.wikia.nocookie.net/bee-swarm-simulator/images/f/fa/Basic_Egg.png/revision/latest/scale-to-width-down/25?cb=20230404043532)[Basic Eggs](/wiki/Egg#Basic_Egg "Egg") for increasing amounts of [honey](/wiki/Honey "Honey"). 

The cost begins at 1,000 honey and increases exponentially (see Formula section below), eventually capping off at 10,000,000 honey for the 22nd egg and beyond.

[![](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](https://static.wikia.nocookie.net/bee-swarm-simulator/images/3/36/EggPrices2.png/revision/latest?cb=20180601031936 "A chart for the eggs' price.")A chart for the eggs' price. ![Basic Egg](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)[Basic Eggs](/wiki/Egg#Basic_Egg "Egg") | ![Honey](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)[Honey](/wiki/Honey "Honey")  
---|---  
1  | 1,000   
2  | 2,500   
3  | 4,250   
4  | 6,708   
5  | 10,313   
6  | 15,669   
7  | 23,670   
8  | 35,648   
9  | 53,596   
10  | 80,506   
11  | 120,858   
12  | 181,378   
13  | 272,151   
14  | 408,304   
15  | 612,527   
16  | 918,857   
17  | 1,378,348   
18  | 2,067,580   
19  | 3,101,426   
20  | 4,652,191   
21  | 6,978,337   
22+  | 10,000,000   
  
## Formula[[](https://auth.fandom.com/signin?redirect=https%3A%2F%2Fbee-swarm-simulator.fandom.com%2Fwiki%2FBasic_Egg_Shop%3Fveaction%3Dedit%26section%3D1&uselang=en&metadata=article-registration-edit-article-section "Sign in to edit")]

The cost of egg number N is calculated as follows: 
    
    
    base = 1000
    cost = base
    i = 0
    while i < N-1 do
        cost = 1.5*cost + base/(i+1)
        i = i + 1
    end
    

This comes out roughly exponential, but there isn't a "nice neat numbers" exponential formula. 
    
    
    Base = 1000
    t = Base
    i = 0
    NN = 21
    For [i=0; t= Base, i < NN, i++, t=1.5*t+Base/(i+1);{Print[Floor[t+0.5]]}]
    

This does not work for Term 22, as the price caps out at 10,000,000 honey. 

## Trivia[[](https://auth.fandom.com/signin?redirect=https%3A%2F%2Fbee-swarm-simulator.fandom.com%2Fwiki%2FBasic_Egg_Shop%3Fveaction%3Dedit%26section%3D2&uselang=en&metadata=article-registration-edit-article-section "Sign in to edit")]

  * The Basic Egg Shop and stacking the [Round Basic Bee sticker](/wiki/Sticker#Stickers "Sticker") are the only ways to obtain a ![Basic Egg](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)[Basic Egg](/wiki/Egg#Basic_Egg "Egg"), other than the one given to the player at the start of the game.
  * Just like the other machine lookalikes, the model of the machine is a modified version of the [Gumball Machine](https://create.roblox.com/store/asset/126202248/Gumball-Machine) model by @wonderful72pike.



Locations   
---  
[Fields](/wiki/Fields "Fields") | **[Sunflower Field](/wiki/Sunflower_Field "Sunflower Field") • [Dandelion Field](/wiki/Dandelion_Field "Dandelion Field") • [Mushroom Field](/wiki/Mushroom_Field "Mushroom Field") • [Blue Flower Field](/wiki/Blue_Flower_Field "Blue Flower Field") • [Clover Field](/wiki/Clover_Field "Clover Field") • [Spider Field](/wiki/Spider_Field "Spider Field") • [Bamboo Field](/wiki/Bamboo_Field "Bamboo Field") • [Strawberry Field](/wiki/Strawberry_Field "Strawberry Field") • [Pineapple Patch](/wiki/Pineapple_Patch "Pineapple Patch") • [Stump Field](/wiki/Stump_Field "Stump Field") • [Mixed Brick Field](/wiki/Mixed_Brick_Field "Mixed Brick Field") • [Blue Brick Field](/wiki/Blue_Brick_Field "Blue Brick Field") • [Red Brick Field](/wiki/Red_Brick_Field "Red Brick Field") • [White Brick Field](/wiki/White_Brick_Field "White Brick Field") • [Cactus Field](/wiki/Cactus_Field "Cactus Field") • [Pumpkin Patch](/wiki/Pumpkin_Patch "Pumpkin Patch") • [Pine Tree Forest](/wiki/Pine_Tree_Forest "Pine Tree Forest") • [Rose Field](/wiki/Rose_Field "Rose Field") • [Ant Field](/wiki/Ant_Field "Ant Field") • [Hub Field](/wiki/Hub_Field "Hub Field") • [Mountain Top Field](/wiki/Mountain_Top_Field "Mountain Top Field") • [Coconut Field](/wiki/Coconut_Field "Coconut Field") • [Pepper Patch](/wiki/Pepper_Patch "Pepper Patch")**  
[Shops](/wiki/Shops "Shops") | ****Basic Egg Shop** • [Boost Market](/wiki/Boost_Market "Boost Market") • [Treat Shop](/wiki/Treat_Shop "Treat Shop") • [Gumdrop Shop](/wiki/Gumdrop_Shop "Gumdrop Shop") • [Royal Jelly Shop](/wiki/Royal_Jelly_Shop "Royal Jelly Shop") • [Ticket Shop](/wiki/Ticket_Shop "Ticket Shop") • [Noob Shop](/wiki/Noob_Shop "Noob Shop") • [Pro Shop](/wiki/Pro_Shop "Pro Shop") • [Magic Bean Shop](/wiki/Magic_Bean_Shop "Magic Bean Shop") • [Badge Bearer's Guild](/wiki/Badge_Bearer%27s_Guild "Badge Bearer's Guild") • [Dapper Bear's Shop](/wiki/Dapper_Bear%27s_Shop "Dapper Bear's Shop") • [Stinger Shop](/wiki/Stinger_Shop "Stinger Shop") • [Mountain Top Shop](/wiki/Mountain_Top_Shop "Mountain Top Shop") • [Blue HQ](/wiki/Blue_HQ "Blue HQ") • [Red HQ](/wiki/Red_HQ "Red HQ") • [Hub Field Shop](/wiki/Hub_Field_Shop "Hub Field Shop") • [Robo Bear's Shop](/wiki/Robo_Bear%27s_Shop "Robo Bear's Shop") • [Petal Shop](/wiki/Petal_Shop "Petal Shop") • [Coconut Cave](/wiki/Coconut_Cave "Coconut Cave") • [Ticket Tent](/wiki/Ticket_Tent "Ticket Tent") • [Robux Shop](/wiki/Robux_Shop "Robux Shop")**  
[Gates](/wiki/Category:Gates "Category:Gates") | **[Basic Bee Gate](/wiki/Basic_Bee_Gate "Basic Bee Gate") • [Brave Bee Gate](/wiki/Brave_Bee_Gate "Brave Bee Gate") • [Honey Bee Gate](/wiki/Honey_Bee_Gate "Honey Bee Gate") • [Ant Gate](/wiki/Ant_Gate "Ant Gate") • [Lion Bee Gate](/wiki/Lion_Bee_Gate "Lion Bee Gate") • [Bear Gate](/wiki/Bear_Gate "Bear Gate") • [Windy Bee Gate](/wiki/Windy_Bee_Gate "Windy Bee Gate")**  
[Machines](/wiki/Machines "Machines") | **[Honey Dispenser](/wiki/Honey_Dispenser "Honey Dispenser") • [Royal Jelly Dispenser](/wiki/Royal_Jelly_Dispenser "Royal Jelly Dispenser") • [Treat Dispenser](/wiki/Treat_Dispenser "Treat Dispenser") • [Instant Converter](/wiki/Instant_Converter "Instant Converter") • [Wealth Clock](/wiki/Wealth_Clock "Wealth Clock") • [Moon Amulet Generator](/wiki/Moon_Amulet_Generator "Moon Amulet Generator") • [Memory Match](/wiki/Memory_Match "Memory Match") • [Blue Field Booster](/wiki/Blue_Field_Booster "Blue Field Booster") • [Red Field Booster](/wiki/Red_Field_Booster "Red Field Booster") • [Field Booster](/wiki/Field_Booster "Field Booster") • [Blueberry Dispenser](/wiki/Blueberry_Dispenser "Blueberry Dispenser") • [Strawberry Dispenser](/wiki/Strawberry_Dispenser "Strawberry Dispenser") • [Honeystorm](/wiki/Honeystorm "Honeystorm") • [Special Sprout Summoner](/wiki/Special_Sprout_Summoner "Special Sprout Summoner") • [Free Ant Pass Dispenser](/wiki/Free_Ant_Pass_Dispenser "Free Ant Pass Dispenser") • [Ant Pass Dispenser](/wiki/Ant_Pass_Dispenser "Ant Pass Dispenser") • [Glue Dispenser](/wiki/Glue_Dispenser "Glue Dispenser") • [Blender](/wiki/Blender "Blender") • [Coconut Dispenser](/wiki/Coconut_Dispenser "Coconut Dispenser") • [Mythic Meteor Shower](/wiki/Mythic_Meteor_Shower "Mythic Meteor Shower") • [Free Robo Pass Dispenser](/wiki/Free_Robo_Pass_Dispenser "Free Robo Pass Dispenser") • [Robo Pass Dispenser](/wiki/Robo_Pass_Dispenser "Robo Pass Dispenser") • [Sticker Stack](/wiki/Sticker_Stack "Sticker Stack") • [Sticker Printer](/wiki/Sticker_Printer "Sticker Printer") • [Nectar Condenser](/wiki/Nectar_Condenser "Nectar Condenser")**  
[Transportation](/wiki/Category:Transport "Category:Transport") | **[Slingshot](/wiki/Slingshot "Slingshot") • [Yellow Cannon](/wiki/Yellow_Cannon "Yellow Cannon") • [Blue Cannon](/wiki/Blue_Cannon "Blue Cannon") • [Red Cannon](/wiki/Red_Cannon "Red Cannon") • [Blue Teleporter](/wiki/Blue_Teleporter "Blue Teleporter") • [Red Teleporter](/wiki/Red_Teleporter "Red Teleporter")**  
[Leaderboards](/wiki/Leaderboards "Leaderboards") | **[Daily Top Honeymakers](/wiki/Daily_Top_Honeymakers "Daily Top Honeymakers") • [All-Time Top Honeymakers](/wiki/All-Time_Top_Honeymakers "All-Time Top Honeymakers") • [All-Time Top Battlers](/wiki/All-Time_Top_Battlers_\(Most_Battle_Points\) "All-Time Top Battlers \(Most Battle Points\)") • [Top Ant Exterminators](/wiki/Top_Ant_Exterminators "Top Ant Exterminators") • [Fastest Crab Slayers](/wiki/Fastest_Crab_Slayers "Fastest Crab Slayers") • [Top Stick Bug Fighters](/wiki/Top_Stick_Bug_Fighters "Top Stick Bug Fighters") • [Top Bucko Bee Helpers](/wiki/Top_Bucko_Bee_Helpers "Top Bucko Bee Helpers") • [Top Riley Bee Helpers](/wiki/Top_Riley_Bee_Helpers "Top Riley Bee Helpers") • [Most Commando Captures](/wiki/Most_Commando_Captures "Most Commando Captures") • [Top Brown Bear Helpers](/wiki/Top_Brown_Bear_Helpers "Top Brown Bear Helpers") • [All-Time Top Red Collectors](/wiki/All-Time_Top_Red_Collectors "All-Time Top Red Collectors") • [All-Time Top Blue Collectors](/wiki/All-Time_Top_Blue_Collectors "All-Time Top Blue Collectors") • [All-Time Top White Collectors](/wiki/All-Time_Top_White_Collectors "All-Time Top White Collectors") • [Daily Top Red Collectors](/wiki/Daily_Top_Red_Collectors "Daily Top Red Collectors") • [Daily Top Blue Collectors](/wiki/Daily_Top_Blue_Collectors "Daily Top Blue Collectors") • [Daily Top White Collectors](/wiki/Daily_Top_White_Collectors "Daily Top White Collectors") • [Highest Damage to a Single Puffshroom](/wiki/Highest_Damage_to_a_Single_Puffshroom "Highest Damage to a Single Puffshroom") • [Tallest Sticker Stack](/wiki/Tallest_Sticker_Stack "Tallest Sticker Stack") • [Highest Robo Bear Challenge Scores](/wiki/Highest_Robo_Bear_Challenge_Scores "Highest Robo Bear Challenge Scores") • [Highest Snowbear Level](/wiki/Highest_Snowbear_Level "Highest Snowbear Level") • [Highest Robo Party Cake Rank](/wiki/Highest_Robo_Party_Cake_Rank "Highest Robo Party Cake Rank")**  
Other  
Places  | **[Hive](/wiki/Hive "Hive") • [Obstacle Courses](/wiki/Obstacle_Courses "Obstacle Courses") • [King Beetle Lair](/wiki/King_Beetle_Lair "King Beetle Lair") • [White Tunnel](/wiki/White_Tunnel "White Tunnel") • [Werewolf's Cave](/wiki/Werewolf%27s_Cave "Werewolf's Cave") • [Ant Challenge](/wiki/Ant_Challenge "Ant Challenge") • [Star Hall](/wiki/Star_Hall "Star Hall") • [Gummy Bear's Lair](/wiki/Gummy_Bear%27s_Lair "Gummy Bear's Lair") • [Ant Challenge Info](/wiki/Ant_Challenge_Info "Ant Challenge Info") • [Vicious Bee Egg Claim](/wiki/Vicious_Bee_Egg_Claim "Vicious Bee Egg Claim") • [Gummy Bee Egg Claim](/wiki/Gummy_Bee_Egg_Claim "Gummy Bee Egg Claim") • [Wind Shrine](/wiki/Wind_Shrine "Wind Shrine") • [Mazes](/wiki/Mazes "Mazes") • [Hive Hub](/wiki/Hive_Hub "Hive Hub") • [Sticker-Seeker Quest Machine](/wiki/Sticker-Seeker_Quest_Machine "Sticker-Seeker Quest Machine")**  
Event  
Locations  | **[Beesmas Tree](/wiki/Beesmas_Tree "Beesmas Tree") • [Ornament Presents](/wiki/Ornament_Presents "Ornament Presents") • [Computer](/wiki/Computer "Computer") • [Gift Boxes](/wiki/Gift_Boxes "Gift Boxes") • [Honey Wreath](/wiki/Honey_Wreath "Honey Wreath") • [Stockings](/wiki/Stockings "Stockings") • [Gingerbread House](/wiki/Gingerbread_House "Gingerbread House") • [Snowbear Summoner](/wiki/Snowbear_Summoner "Snowbear Summoner") • [Beesmas Lights](/wiki/Beesmas_Lights "Beesmas Lights") • [Samovar](/wiki/Samovar "Samovar") • [Beesmas Feast](/wiki/Beesmas_Feast "Beesmas Feast") • [Onett's Lid Art](/wiki/Onett%27s_Lid_Art "Onett's Lid Art") • [Galentine Shrine](/wiki/Wind_Shrine#Galentine_Shrine "Wind Shrine") • [Winter Memory Match](/wiki/Memory_Match#Winter_Memory_Match "Memory Match") • [Snow Machine](/wiki/Snow_Machine "Snow Machine") • [Honeyday Candles](/wiki/Honeyday_Candles "Honeyday Candles") • [Robo Party Cake](/wiki/Robo_Party_Cake "Robo Party Cake") • [Gummy Beacon](/wiki/Gummy_Beacon "Gummy Beacon") • [Naughty List](/wiki/Naughty_List "Naughty List")**
