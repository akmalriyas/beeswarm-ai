# Amulets

![Digital Bee](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D) | **This piece of content contains information obtained through datamining.** Due to the nature of the information, details may be inaccurate or outdated.  
Datamined information: How Amulets are generated.  
Date of datamined file: December 19th, 2024  
---|---  
[![The scheme for the Ant Amulet.](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](https://static.wikia.nocookie.net/bee-swarm-simulator/images/e/ec/Scheme-0.png/revision/latest?cb=20190111200708) [![The scheme for the Ant Amulet.](https://static.wikia.nocookie.net/bee-swarm-simulator/images/e/ec/Scheme-0.png/revision/latest/scale-to-width-down/246?cb=20190111200708)](https://static.wikia.nocookie.net/bee-swarm-simulator/images/e/ec/Scheme-0.png/revision/latest?cb=20190111200708) [](/wiki/File:Scheme-0.png)

The scheme for the Ant Amulet.

An **amulet** is an item introduced in the [2018-07-11 update](/wiki/Updates#2018-07-11 "Updates"). They grant several [buffs](/wiki/Buffs_%26_Debuffs "Buffs & Debuffs") to the player and/or their [bees](/wiki/Bees "Bees"), and can be obtained by completing certain special challenges. 

## Obtaining

Collecting an amulet will bring up a table with the old and new amulets' stats, and the option to keep the old amulet or replace it. The scheme on the left shows an example table, with the player's amulet type as well as other rewards. If the player has obtained the amulet from the Ant Challenge or Stick Bug Challenge, their score will be shown above the rewards. 

Clicking "**Keep Old** " will cause the player to keep their current amulet and clicking "**Replace** " will cause the player to receive a confirmation message asking if they want to replace it. If the player has agreed to replace their amulet after the confirmation message, the player's old amulet will be replaced with the new one. **This cannot be reversed**. Note that the drops will still be received even if the player didn't replace their amulet. If two or more tables are shown, the previous table(s) are closed, and the newest table is displayed. As of the [2020-06-06 update](/wiki/Updates#2020-06-06 "Updates"), a confirmation message will now pop up if the player tries to replace an amulet if they already had that type of amulet, and, as of the [2021-12-26 update](/wiki/Updates#2021-12-26 "Updates"), disconnecting while a recently generated amulet is undecided gives the player another chance to choose upon going back in a server. 

## Generation

Amulets are generated with a given quality, which changes based on doing certain actions (for example, different scores yield proportionally different qualities, with a limit). Increasing the quality of an amulet will improve the probability of getting a better amulet. Note that this does not entirely eliminate the possibility of getting a worse amulet. 

Details of how this works are provided below. For the raw data of every amulet, see [Module:Amulet Stats/data](/wiki/Module:Amulet_Stats/data "Module:Amulet Stats/data"). 

### Choosing Stats

An amulet's stats can be split into multiple stat groups. When an amulet is generated, it picks out a number of stats from each group to put on the amulet. Some stat groups will only appear with a certain probability. 

After a stat is picked, it checks if it has a probability of appearing (different from the probability of the stat group it's in); if it does, it may randomly remove itself from the amulet based on the probability. This is why some amulets may have a lower number of stats than expected. 

As of currently, this process is not influenced by the amulet's quality. 

### Getting Stat Strength

Picked stats on an amulet go through a process to determine its strength, before the amulet is given to the player. The strength of the stats are influenced by the amulet's quality, by placing a heavy bias at a certain value that increases with the amulet's quality, making it so the stat's strength are more likely to be near that bias. 

More specifically: 

  * Every stat have a _bias_ table, which consists of 2 values, dubbed _biasQuality_ and _biasDirect_ respectively. 
    * A higher _biasQuality_ makes it so the amulet's quality have a bigger effect on the stat's bias, and vice versa.
    * A higher _biasDirect_ directly affects the stat's bias, regardless of the amuelet's quality.
    * The default value for both variables (assuming one isn't assigned by the game) is 1.
  * The bias is calculated by the formula:  b i a s = m i n V a l u e + ( m a x V a l u e − m i n V a l u e ) × b i a s D i r e c t × q u a l i t y max ( 1 , b i a s Q u a l i t y × ( 1 − q u a l i t y ) ) {\displaystyle bias=minValue+(maxValue-minValue)\times biasDirect\times {\frac {quality}{\max(1,biasQuality\times (1-quality))}}} ![{\\displaystyle bias=minValue+\(maxValue-minValue\)\\times biasDirect\\times {\\frac {quality}{\\max\(1,biasQuality\\times \(1-quality\)\)}}}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/0df31a382ee83d54b361440745761c3899b5eb61), where _minValue_ and _maxValue_ are the minimum and maximum possible values of the stat's strength.



After that, the RandomBias function is called with the following paramenters, and the result is rounded to the stat's resolution interval to give the stat's strength:  
` randomBias(minValue, maxValue, bias, 1) `  
For more information on how this function works, [see the designated module page](/wiki/Module:RandomBias "Module:RandomBias"). 

## Amulets

_Certain features on articles may be non-functional due to FANDOM's discontinued support of TabViews. Please visit each article separately for a better experience._

  * [ King Beetle Amulet ](https://bee-swarm-simulator.fandom.com/wiki/King_Beetle_Amulet)
  * [ Star Amulet ](https://bee-swarm-simulator.fandom.com/wiki/Star_Amulet)
  * [ Ant Amulet ](https://bee-swarm-simulator.fandom.com/wiki/Ant_Amulet)
  * [ Moon Amulet ](https://bee-swarm-simulator.fandom.com/wiki/Moon_Amulet)
  * [ Shell Amulet ](https://bee-swarm-simulator.fandom.com/wiki/Shell_Amulet)
  * [ Stick Bug Amulet ](https://bee-swarm-simulator.fandom.com/wiki/Stick_Bug_Amulet)
  * [ Cog Amulet ](https://bee-swarm-simulator.fandom.com/wiki/Cog_Amulet)



  


## Gallery

[![The confirmation message that appears when the player wants to replace their amulet.](https://static.wikia.nocookie.net/bee-swarm-simulator/images/9/97/Equipnewamulet.png/revision/latest/scale-to-width-down/185?cb=20200606235614)![The confirmation message that appears when the player wants to replace their amulet.](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/File:Equipnewamulet.png "Equipnewamulet.png \(7 KB\)")

The confirmation message that appears when the player wants to replace their amulet.

[![The message that appears when a player joins a server after disconnecting with an undecided amulet.](https://static.wikia.nocookie.net/bee-swarm-simulator/images/d/df/Amulet_disconnection_message.png/revision/latest/scale-to-width-down/164?cb=20230409225159)![The message that appears when a player joins a server after disconnecting with an undecided amulet.](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/File:Amulet_disconnection_message.png "Amulet disconnection message.png \(58 KB\)")

The message that appears when a player joins a server after disconnecting with an undecided amulet.

[![A visual bug where the Supreme Star and Ant Amulets are colored black.](https://static.wikia.nocookie.net/bee-swarm-simulator/images/4/44/Black_Supreme_Amulets.png/revision/latest/scale-to-width-down/185?cb=20250711041654)![A visual bug where the Supreme Star and Ant Amulets are colored black.](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/File:Black_Supreme_Amulets.png "Black Supreme Amulets.png \(72 KB\)")

A visual bug where the Supreme Star and Ant Amulets are colored black.

## Trivia

  * Supreme amulets are the only amulets that change color slightly. 
    * Sometimes, a rare visual bug will cause a supreme amulet to appear black. There is currently no known cause of this.


