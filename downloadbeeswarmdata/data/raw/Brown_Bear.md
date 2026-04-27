# Brown Bear

![Digital Bee](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D) | **This piece of content contains information obtained through datamining.** Due to the nature of the information, details may be inaccurate or outdated.  
  
---|---  
**Brown Bear**  
---  
[![Brown](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](https://static.wikia.nocookie.net/bee-swarm-simulator/images/0/06/Brown.png/revision/latest?cb=20190402221124)  
Overview   
Species  | Quest Bear   
Location  | Near the Clover Field and the Wealth Clock.   
Bee Prerequisites  | None   
Color Scheme   
|  Fur #634929 |  Fur Shade #554026  
---|---  
Snout #634929 #C8A77F |  Torso #785d3d  
Arms #94744e |  Legs #634b2f  
  
**Brown Bear** is a [quest giver](/wiki/Quest_Givers "Quest Givers") and one of eight permanent [bears](/wiki/Category:Bears "Category:Bears") that can be accessed in the game, the others being [Black Bear](/wiki/Black_Bear "Black Bear"), [Mother Bear](/wiki/Mother_Bear "Mother Bear"), [Panda Bear](/wiki/Panda_Bear "Panda Bear"), [Science Bear](/wiki/Science_Bear "Science Bear"), [Dapper Bear](/wiki/Dapper_Bear "Dapper Bear"), [Polar Bear](/wiki/Polar_Bear "Polar Bear"), and [Spirit Bear](/wiki/Spirit_Bear "Spirit Bear"). He is located behind the [Clover Field](/wiki/Clover_Field "Clover Field") and next to the [Wealth Clock](/wiki/Wealth_Clock "Wealth Clock") and the [Top Brown Bear Helpers](/wiki/Top_Brown_Bear_Helpers "Top Brown Bear Helpers") leaderboard. His [quests](/wiki/Quests "Quests") primarily focus on collecting [pollen](/wiki/Pollen "Pollen") from randomized [fields](/wiki/Fields "Fields"). After initiating a quest, a new one will be available in 1 hour. 

## Quests[[](https://auth.fandom.com/signin?redirect=https%3A%2F%2Fbee-swarm-simulator.fandom.com%2Fwiki%2FBrown_Bear%3Fveaction%3Dedit%26section%3D1&uselang=en&metadata=article-registration-edit-article-section "Sign in to edit")]

Brown Bear is an infinite quest giver. His quests requires collecting pollen from a selection of fields, scaling up in difficulty the more the player completes, with the reward also getting bigger the more difficult it gets. Certain quests are only given if the player has reached a minimum number of bees. 

### Scaling[[](https://auth.fandom.com/signin?redirect=https%3A%2F%2Fbee-swarm-simulator.fandom.com%2Fwiki%2FBrown_Bear%3Fveaction%3Dedit%26section%3D2&uselang=en&metadata=article-registration-edit-article-section "Sign in to edit")]

The amount of quests the player has to collect from a field is defined by the function  P ( x ) {\displaystyle P(x)} ![{\\displaystyle P\(x\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/42412df742cffad392f8e25688a40b292c073541), where  x {\displaystyle x} ![{\\displaystyle x}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/efc49430c87d6546728cf091f2a88afa7417e7a2) is a hard-coded number that is different for each quest. The value of  P ( x ) {\displaystyle P(x)} ![{\\displaystyle P\(x\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/42412df742cffad392f8e25688a40b292c073541) scales with the number of Brown Bear quests the player has done. 

The function  P ( x ) {\displaystyle P(x)} ![{\\displaystyle P\(x\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/42412df742cffad392f8e25688a40b292c073541) is defined as follows: 

  * Let  c n t {\displaystyle cnt} ![{\\displaystyle cnt}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/c581d0f222be27296fa4ea5ca8bf261f266ef07a) be the number of Brown Bear quests the player has done as of claiming the quest.
  * We define 3 variables: 
    * b a s e = ⌊ 2500 × x + 0.5 100 ⌋ × 100 {\displaystyle base=\left\lfloor {\frac {2500\times x+0.5}{100}}\right\rfloor \times 100} ![{\\displaystyle base=\\left\\lfloor {\\frac {2500\\times x+0.5}{100}}\\right\\rfloor \\times 100}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/78d2abc9dbc9ad14f07304e5abaab0f6daa7d0e2)
    * i n c = ⌊ 5000 × x + 0.5 100 ⌋ × 100 {\displaystyle inc=\left\lfloor {\frac {5000\times x+0.5}{100}}\right\rfloor \times 100} ![{\\displaystyle inc=\\left\\lfloor {\\frac {5000\\times x+0.5}{100}}\\right\\rfloor \\times 100}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/38fe705e30efe57b898a3919f906d79310b8add8)
    * m a x = ⌊ 10000000000000 × x + 0.5 100 ⌋ × 100 {\displaystyle max=\left\lfloor {\frac {10000000000000\times x+0.5}{100}}\right\rfloor \times 100} ![{\\displaystyle max=\\left\\lfloor {\\frac {10000000000000\\times x+0.5}{100}}\\right\\rfloor \\times 100}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/f62a8b0f0a8ee7f98d5fd0a9da2b6d4c6e0b2e9e)
  * Then, we take the following steps: 
    * b a s e P o l l e n = b a s e + c n t × i n c {\displaystyle basePollen=base+cnt\times inc} ![{\\displaystyle basePollen=base+cnt\\times inc}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/739acc2a506fdac88f3fa35736b797648cf51c70)
    * Let  s c a l i n g {\displaystyle scaling} ![{\\displaystyle scaling}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/51254891590c08edb9e69b666c84aeb591440cb9) be equal to: 
      * ( c n t 1000 ) 4 {\displaystyle {({\frac {cnt}{1000}})}^{4}} ![{\\displaystyle {\({\\frac {cnt}{1000}}\)}^{4}}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/daa61b60cb37206ba9b6942474986e854bf558d8) if  c n t 1000 < 1 {\displaystyle {\frac {cnt}{1000}}<1} ![{\\displaystyle {\\frac {cnt}{1000}}<1}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/933cd53a9c4fcf163263a0c6c6efc5f25306b098)
      * ( c n t 1000 ) 2 {\displaystyle {({\frac {cnt}{1000}})}^{2}} ![{\\displaystyle {\({\\frac {cnt}{1000}}\)}^{2}}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/67d9f122199fe6e67373745855e100eb494b3b0e) otherwise
    * r e q u i r e d P o l l e n = b a s e P o l l e n + ( m a x − b a s e P o l l e n ) × s c a l i n g {\displaystyle requiredPollen=basePollen+(max-basePollen)\times scaling} ![{\\displaystyle requiredPollen=basePollen+\(max-basePollen\)\\times scaling}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/71988d16e89e85a69c61ecdc4850a6bc3e1c69ec)
    * i n t e r v a l = 10 max ( ⌊ log 10 ⁡ ( r e q u i r e d P o l l e n ) ⌋ − 1 , 1 ) {\displaystyle interval=10^{\max(\left\lfloor \log _{10}(requiredPollen)\right\rfloor -1,1)}} ![{\\displaystyle interval=10^{\\max\(\\left\\lfloor \\log _{10}\(requiredPollen\)\\right\\rfloor -1,1\)}}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/6e6ef5e9998c0c97b7e7996f32d1a729644dddd9)
    * r o u n d e d P o l l e n = ⌊ r e q u i r e d P o l l e n i n t e r v a l + 0.5 ⌋ × i n t e r v a l {\displaystyle roundedPollen=\left\lfloor {\frac {requiredPollen}{interval}}+0.5\right\rfloor \times interval} ![{\\displaystyle roundedPollen=\\left\\lfloor {\\frac {requiredPollen}{interval}}+0.5\\right\\rfloor \\times interval}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/4105125b11ba08f17c00046cf1fc3ba46810c927)
    * The function returns  r o u n d e d P o l l e n {\displaystyle roundedPollen} ![{\\displaystyle roundedPollen}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/4c79b76cdfa776dead5d3068bed5dd1da76c756f).



### Possible quests[[](https://auth.fandom.com/signin?redirect=https%3A%2F%2Fbee-swarm-simulator.fandom.com%2Fwiki%2FBrown_Bear%3Fveaction%3Dedit%26section%3D3&uselang=en&metadata=article-registration-edit-article-section "Sign in to edit")]

There are a total of 41 different quests Brown Bear can give. 

Quest name  | Minimum number of  
bees required  | Requirements   
---|---|---  
Brown Bear: Sun-Dand  | 0  | 

  * Collect  P ( 0.3 ) {\displaystyle P(0.3)} ![{\\displaystyle P\(0.3\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/222d1ff266cc433446ebca6d84467ec05ff1f2cb) Pollen from Sunflower Field.
  * Collect  P ( 0.3 ) {\displaystyle P(0.3)} ![{\\displaystyle P\(0.3\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/222d1ff266cc433446ebca6d84467ec05ff1f2cb) Pollen from Dandelion Field.

  
Brown Bear: Mush-Clove  | 0  | 

  * Collect  P ( 0.5 ) {\displaystyle P(0.5)} ![{\\displaystyle P\(0.5\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/b2ff6c667c6d2846ce8800e42ac39e673d61e854) Pollen from Clover Field.
  * Collect  P ( 0.3 ) {\displaystyle P(0.3)} ![{\\displaystyle P\(0.3\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/222d1ff266cc433446ebca6d84467ec05ff1f2cb) Pollen from Mushroom Field.

  
Brown Bear: Bluf-Clove  | 0  | 

  * Collect  P ( 0.6 ) {\displaystyle P(0.6)} ![{\\displaystyle P\(0.6\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/6039e7276aeb72db79c0ed11c5a7f6aa3aa84601) Pollen from Clover Field.
  * Collect  P ( 0.3 ) {\displaystyle P(0.3)} ![{\\displaystyle P\(0.3\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/222d1ff266cc433446ebca6d84467ec05ff1f2cb) Pollen from Blue Flower Field.

  
Brown Bear: White-Mush  | 0  | 

  * Collect  P ( 0.6 ) {\displaystyle P(0.6)} ![{\\displaystyle P\(0.6\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/6039e7276aeb72db79c0ed11c5a7f6aa3aa84601) White Pollen.
  * Collect  P ( 0.3 ) {\displaystyle P(0.3)} ![{\\displaystyle P\(0.3\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/222d1ff266cc433446ebca6d84467ec05ff1f2cb) Pollen from Mushroom Field.

  
Brown Bear: White-Bluf  | 0  | 

  * Collect  P ( 0.6 ) {\displaystyle P(0.6)} ![{\\displaystyle P\(0.6\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/6039e7276aeb72db79c0ed11c5a7f6aa3aa84601) White Pollen.
  * Collect  P ( 0.3 ) {\displaystyle P(0.3)} ![{\\displaystyle P\(0.3\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/222d1ff266cc433446ebca6d84467ec05ff1f2cb) Pollen from Blue Flower Field.

  
Brown Bear: Solo-Clove  | 15  | 

  * Collect  P ( 1 ) {\displaystyle P(1)} ![{\\displaystyle P\(1\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/760e8360ee3f9646a43da6349e2e38abb58690dc) Pollen from Clover Field.

  
Brown Bear: Straw-Spide  | 5  | 

  * Collect  P ( 0.5 ) {\displaystyle P(0.5)} ![{\\displaystyle P\(0.5\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/b2ff6c667c6d2846ce8800e42ac39e673d61e854) Pollen from Strawberry Field.
  * Collect  P ( 0.5 ) {\displaystyle P(0.5)} ![{\\displaystyle P\(0.5\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/b2ff6c667c6d2846ce8800e42ac39e673d61e854) Pollen from Spider Field.

  
Brown Bear: Bamb-Spide  | 5  | 

  * Collect  P ( 0.5 ) {\displaystyle P(0.5)} ![{\\displaystyle P\(0.5\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/b2ff6c667c6d2846ce8800e42ac39e673d61e854) Pollen from Bamboo Field.
  * Collect  P ( 0.5 ) {\displaystyle P(0.5)} ![{\\displaystyle P\(0.5\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/b2ff6c667c6d2846ce8800e42ac39e673d61e854) Pollen from Spider Field.

  
Brown Bear: White-Bamb-Mush  | 5  | 

  * Collect  P ( 0.6 ) {\displaystyle P(0.6)} ![{\\displaystyle P\(0.6\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/6039e7276aeb72db79c0ed11c5a7f6aa3aa84601) White Pollen.
  * Collect  P ( 0.4 ) {\displaystyle P(0.4)} ![{\\displaystyle P\(0.4\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/aa31d5f5badf86512fbf2c98d253057c419d5013) Pollen from Bamboo Field.
  * Collect  P ( 0.3 ) {\displaystyle P(0.3)} ![{\\displaystyle P\(0.3\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/222d1ff266cc433446ebca6d84467ec05ff1f2cb) Pollen from Mushroom Field.

  
Brown Bear: Red-Straw-Sun  | 5  | 

  * Collect  P ( 0.6 ) {\displaystyle P(0.6)} ![{\\displaystyle P\(0.6\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/6039e7276aeb72db79c0ed11c5a7f6aa3aa84601) Red Pollen.
  * Collect  P ( 0.3 ) {\displaystyle P(0.3)} ![{\\displaystyle P\(0.3\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/222d1ff266cc433446ebca6d84467ec05ff1f2cb) Pollen from Strawberry Field.
  * Collect  P ( 0.2 ) {\displaystyle P(0.2)} ![{\\displaystyle P\(0.2\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/46eb7a811af613a1f4b0e3b749eed2c2e4368f7c) Pollen from Sunflower Field.

  
Brown Bear: Blue-Clov-Spide  | 5  | 

  * Collect  P ( 0.6 ) {\displaystyle P(0.6)} ![{\\displaystyle P\(0.6\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/6039e7276aeb72db79c0ed11c5a7f6aa3aa84601) Blue Pollen.
  * Collect  P ( 0.3 ) {\displaystyle P(0.3)} ![{\\displaystyle P\(0.3\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/222d1ff266cc433446ebca6d84467ec05ff1f2cb) Pollen from Clover Field.
  * Collect  P ( 0.2 ) {\displaystyle P(0.2)} ![{\\displaystyle P\(0.2\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/46eb7a811af613a1f4b0e3b749eed2c2e4368f7c) Pollen from Spider Field.

  
Brown Bear: Solo-Spide  | 5  | 

  * Collect  P ( 1.1 ) {\displaystyle P(1.1)} ![{\\displaystyle P\(1.1\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/a310fc8af44fc6198ff718f030bb9dc36abcfdca) Pollen from Spider Field.

  
Brown Bear: Solo-Straw  | 5  | 

  * Collect  P ( 1.1 ) {\displaystyle P(1.1)} ![{\\displaystyle P\(1.1\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/a310fc8af44fc6198ff718f030bb9dc36abcfdca) Pollen from Strawberry Field.

  
Brown Bear: Solo-Bamb  | 5  | 

  * Collect  P ( 1.1 ) {\displaystyle P(1.1)} ![{\\displaystyle P\(1.1\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/a310fc8af44fc6198ff718f030bb9dc36abcfdca) Pollen from Bamboo Field.

  
Brown Bear: Blue-Pinap-Clov  | 10  | 

  * Collect  P ( 0.8 ) {\displaystyle P(0.8)} ![{\\displaystyle P\(0.8\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/97e247d88e213f76649a482a3a1adaada18dcd3c) Blue Pollen.
  * Collect  P ( 0.6 ) {\displaystyle P(0.6)} ![{\\displaystyle P\(0.6\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/6039e7276aeb72db79c0ed11c5a7f6aa3aa84601) Pollen from Pineapple Patch.
  * Collect  P ( 0.3 ) {\displaystyle P(0.3)} ![{\\displaystyle P\(0.3\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/222d1ff266cc433446ebca6d84467ec05ff1f2cb) Pollen from Clover Field.

  
Brown Bear: Red-Pinap-Dand  | 10  | 

  * Collect  P ( 0.8 ) {\displaystyle P(0.8)} ![{\\displaystyle P\(0.8\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/97e247d88e213f76649a482a3a1adaada18dcd3c) Red Pollen.
  * Collect  P ( 0.6 ) {\displaystyle P(0.6)} ![{\\displaystyle P\(0.6\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/6039e7276aeb72db79c0ed11c5a7f6aa3aa84601) Pollen from Pineapple Patch.
  * Collect  P ( 0.2 ) {\displaystyle P(0.2)} ![{\\displaystyle P\(0.2\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/46eb7a811af613a1f4b0e3b749eed2c2e4368f7c) Pollen from Dandelion Field.

  
Brown Bear: Pinap-Bamb  | 10  | 

  * Collect  P ( 0.6 ) {\displaystyle P(0.6)} ![{\\displaystyle P\(0.6\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/6039e7276aeb72db79c0ed11c5a7f6aa3aa84601) Pollen from Pineapple Patch.
  * Collect  P ( 0.5 ) {\displaystyle P(0.5)} ![{\\displaystyle P\(0.5\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/b2ff6c667c6d2846ce8800e42ac39e673d61e854) Pollen from Bamboo Field.

  
Brown Bear: Pinap-Straw  | 10  | 

  * Collect  P ( 0.6 ) {\displaystyle P(0.6)} ![{\\displaystyle P\(0.6\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/6039e7276aeb72db79c0ed11c5a7f6aa3aa84601) Pollen from Pineapple Patch.
  * Collect  P ( 0.5 ) {\displaystyle P(0.5)} ![{\\displaystyle P\(0.5\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/b2ff6c667c6d2846ce8800e42ac39e673d61e854) Pollen from Strawberry Field.

  
Brown Bear: Solo-Cact  | 15  | 

  * Collect  P ( 1.1 ) {\displaystyle P(1.1)} ![{\\displaystyle P\(1.1\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/a310fc8af44fc6198ff718f030bb9dc36abcfdca) Pollen from Cactus Field.

  
Brown Bear: White-Cact-Sun  | 15  | 

  * Collect  P ( 0.8 ) {\displaystyle P(0.8)} ![{\\displaystyle P\(0.8\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/97e247d88e213f76649a482a3a1adaada18dcd3c) White Pollen.
  * Collect  P ( 0.6 ) {\displaystyle P(0.6)} ![{\\displaystyle P\(0.6\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/6039e7276aeb72db79c0ed11c5a7f6aa3aa84601) Pollen from Cactus Field.
  * Collect  P ( 0.3 ) {\displaystyle P(0.3)} ![{\\displaystyle P\(0.3\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/222d1ff266cc433446ebca6d84467ec05ff1f2cb) Pollen from Sunflower Field.

  
Brown Bear: Blue-Pump-Bluf  | 15  | 

  * Collect  P ( 0.8 ) {\displaystyle P(0.8)} ![{\\displaystyle P\(0.8\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/97e247d88e213f76649a482a3a1adaada18dcd3c) Blue Pollen.
  * Collect  P ( 0.6 ) {\displaystyle P(0.6)} ![{\\displaystyle P\(0.6\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/6039e7276aeb72db79c0ed11c5a7f6aa3aa84601) Pollen from Pumpkin Patch.
  * Collect  P ( 0.3 ) {\displaystyle P(0.3)} ![{\\displaystyle P\(0.3\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/222d1ff266cc433446ebca6d84467ec05ff1f2cb) Pollen from Blue Flower Field.

  
Brown Bear: Red-Cact-Rose  | 15  | 

  * Collect  P ( 0.8 ) {\displaystyle P(0.8)} ![{\\displaystyle P\(0.8\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/97e247d88e213f76649a482a3a1adaada18dcd3c) Red Pollen.
  * Collect  P ( 0.5 ) {\displaystyle P(0.5)} ![{\\displaystyle P\(0.5\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/b2ff6c667c6d2846ce8800e42ac39e673d61e854) Pollen from Cactus Field.
  * Collect  P ( 0.5 ) {\displaystyle P(0.5)} ![{\\displaystyle P\(0.5\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/b2ff6c667c6d2846ce8800e42ac39e673d61e854) Pollen from Rose Field.

  
Brown Bear: Blue-Pine-Mush  | 15  | 

  * Collect  P ( 0.8 ) {\displaystyle P(0.8)} ![{\\displaystyle P\(0.8\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/97e247d88e213f76649a482a3a1adaada18dcd3c) Blue Pollen.
  * Collect  P ( 0.6 ) {\displaystyle P(0.6)} ![{\\displaystyle P\(0.6\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/6039e7276aeb72db79c0ed11c5a7f6aa3aa84601) Pollen from Pine Tree Forest.
  * Collect  P ( 0.4 ) {\displaystyle P(0.4)} ![{\\displaystyle P\(0.4\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/aa31d5f5badf86512fbf2c98d253057c419d5013) Pollen from Mushroom Field.

  
Brown Bear: White-Pine-Straw  | 15  | 

  * Collect  P ( 0.8 ) {\displaystyle P(0.8)} ![{\\displaystyle P\(0.8\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/97e247d88e213f76649a482a3a1adaada18dcd3c) White Pollen.
  * Collect  P ( 0.6 ) {\displaystyle P(0.6)} ![{\\displaystyle P\(0.6\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/6039e7276aeb72db79c0ed11c5a7f6aa3aa84601) Pollen from Pine Tree Forest.
  * Collect  P ( 0.4 ) {\displaystyle P(0.4)} ![{\\displaystyle P\(0.4\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/aa31d5f5badf86512fbf2c98d253057c419d5013) Pollen from Strawberry Field.

  
Brown Bear: White-Rose-Bamb  | 15  | 

  * Collect  P ( 0.8 ) {\displaystyle P(0.8)} ![{\\displaystyle P\(0.8\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/97e247d88e213f76649a482a3a1adaada18dcd3c) White Pollen.
  * Collect  P ( 0.6 ) {\displaystyle P(0.6)} ![{\\displaystyle P\(0.6\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/6039e7276aeb72db79c0ed11c5a7f6aa3aa84601) Pollen from Rose Field.
  * Collect  P ( 0.4 ) {\displaystyle P(0.4)} ![{\\displaystyle P\(0.4\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/aa31d5f5badf86512fbf2c98d253057c419d5013) Pollen from Bamboo Field.

  
Brown Bear: Red-Pump-Dand  | 15  | 

  * Collect  P ( 0.8 ) {\displaystyle P(0.8)} ![{\\displaystyle P\(0.8\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/97e247d88e213f76649a482a3a1adaada18dcd3c) Red Pollen.
  * Collect  P ( 0.6 ) {\displaystyle P(0.6)} ![{\\displaystyle P\(0.6\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/6039e7276aeb72db79c0ed11c5a7f6aa3aa84601) Pollen from Pumpkin Patch.
  * Collect  P ( 0.4 ) {\displaystyle P(0.4)} ![{\\displaystyle P\(0.4\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/aa31d5f5badf86512fbf2c98d253057c419d5013) Pollen from Dandelion Field.

  
Brown Bear: Red-Mount-Mush  | 25  | 

  * Collect  P ( 0.8 ) {\displaystyle P(0.8)} ![{\\displaystyle P\(0.8\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/97e247d88e213f76649a482a3a1adaada18dcd3c) Red Pollen.
  * Collect  P ( 0.7 ) {\displaystyle P(0.7)} ![{\\displaystyle P\(0.7\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/a92eb2607902646941cb45f409fb8d3c38233448) Pollen from Mountain Top Field.
  * Collect  P ( 0.4 ) {\displaystyle P(0.4)} ![{\\displaystyle P\(0.4\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/aa31d5f5badf86512fbf2c98d253057c419d5013) Pollen from Mushroom Field.

  
Brown Bear: Blue-Mount-Bluf  | 25  | 

  * Collect  P ( 0.8 ) {\displaystyle P(0.8)} ![{\\displaystyle P\(0.8\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/97e247d88e213f76649a482a3a1adaada18dcd3c) Blue Pollen.
  * Collect  P ( 0.7 ) {\displaystyle P(0.7)} ![{\\displaystyle P\(0.7\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/a92eb2607902646941cb45f409fb8d3c38233448) Pollen from Mountain Top Field.
  * Collect  P ( 0.4 ) {\displaystyle P(0.4)} ![{\\displaystyle P\(0.4\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/aa31d5f5badf86512fbf2c98d253057c419d5013) Pollen from Blue Flower Field.

  
Brown Bear: Solo-Mount  | 25  | 

  * Collect  P ( 1.2 ) {\displaystyle P(1.2)} ![{\\displaystyle P\(1.2\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/89ab29aae504c27ba0d304fcb9db3aac81d098c4) Pollen from Mountain Top Field.

  
Brown Bear: Mount-Spide-Rose-Pinap  | 25  | 

  * Collect  P ( 0.4 ) {\displaystyle P(0.4)} ![{\\displaystyle P\(0.4\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/aa31d5f5badf86512fbf2c98d253057c419d5013) Pollen from Mountain Top Field.
  * Collect  P ( 0.2 ) {\displaystyle P(0.2)} ![{\\displaystyle P\(0.2\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/46eb7a811af613a1f4b0e3b749eed2c2e4368f7c) Pollen from Spider Field.
  * Collect  P ( 0.2 ) {\displaystyle P(0.2)} ![{\\displaystyle P\(0.2\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/46eb7a811af613a1f4b0e3b749eed2c2e4368f7c) Pollen from Rose Field.
  * Collect  P ( 0.2 ) {\displaystyle P(0.2)} ![{\\displaystyle P\(0.2\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/46eb7a811af613a1f4b0e3b749eed2c2e4368f7c) Pollen from Pineapple Patch.

  
Brown Bear: Mount-Bamb-Pump-Sun  | 25  | 

  * Collect  P ( 0.4 ) {\displaystyle P(0.4)} ![{\\displaystyle P\(0.4\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/aa31d5f5badf86512fbf2c98d253057c419d5013) Pollen from Mountain Top Field.
  * Collect  P ( 0.2 ) {\displaystyle P(0.2)} ![{\\displaystyle P\(0.2\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/46eb7a811af613a1f4b0e3b749eed2c2e4368f7c) Pollen from Bamboo Field.
  * Collect  P ( 0.2 ) {\displaystyle P(0.2)} ![{\\displaystyle P\(0.2\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/46eb7a811af613a1f4b0e3b749eed2c2e4368f7c) Pollen from Pumpkin Patch.
  * Collect  P ( 0.2 ) {\displaystyle P(0.2)} ![{\\displaystyle P\(0.2\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/46eb7a811af613a1f4b0e3b749eed2c2e4368f7c) Pollen from Sunflower Field.

  
Brown Bear: Blue-Coco-Bluf  | 35  | 

  * Collect  P ( 0.8 ) {\displaystyle P(0.8)} ![{\\displaystyle P\(0.8\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/97e247d88e213f76649a482a3a1adaada18dcd3c) Blue Pollen.
  * Collect  P ( 0.7 ) {\displaystyle P(0.7)} ![{\\displaystyle P\(0.7\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/a92eb2607902646941cb45f409fb8d3c38233448) Pollen from Coconut Field.
  * Collect  P ( 0.4 ) {\displaystyle P(0.4)} ![{\\displaystyle P\(0.4\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/aa31d5f5badf86512fbf2c98d253057c419d5013) Pollen from Blue Flower Field.

  
Brown Bear: Red-Coco-Mush  | 35  | 

  * Collect  P ( 0.8 ) {\displaystyle P(0.8)} ![{\\displaystyle P\(0.8\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/97e247d88e213f76649a482a3a1adaada18dcd3c) Red Pollen.
  * Collect  P ( 0.7 ) {\displaystyle P(0.7)} ![{\\displaystyle P\(0.7\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/a92eb2607902646941cb45f409fb8d3c38233448) Pollen from Coconut Field.
  * Collect  P ( 0.4 ) {\displaystyle P(0.4)} ![{\\displaystyle P\(0.4\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/aa31d5f5badf86512fbf2c98d253057c419d5013) Pollen from Mushroom Field.

  
Brown Bear: White-Pepp-Pinap  | 35  | 

  * Collect  P ( 0.8 ) {\displaystyle P(0.8)} ![{\\displaystyle P\(0.8\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/97e247d88e213f76649a482a3a1adaada18dcd3c) White Pollen.
  * Collect  P ( 0.7 ) {\displaystyle P(0.7)} ![{\\displaystyle P\(0.7\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/a92eb2607902646941cb45f409fb8d3c38233448) Pollen from Pepper Patch.
  * Collect  P ( 0.4 ) {\displaystyle P(0.4)} ![{\\displaystyle P\(0.4\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/aa31d5f5badf86512fbf2c98d253057c419d5013) Pollen from Pineapple Patch.

  
Brown Bear: White-Pepp-Bamb  | 35  | 

  * Collect  P ( 0.8 ) {\displaystyle P(0.8)} ![{\\displaystyle P\(0.8\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/97e247d88e213f76649a482a3a1adaada18dcd3c) White Pollen.
  * Collect  P ( 0.7 ) {\displaystyle P(0.7)} ![{\\displaystyle P\(0.7\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/a92eb2607902646941cb45f409fb8d3c38233448) Pollen from Pepper Patch.
  * Collect  P ( 0.4 ) {\displaystyle P(0.4)} ![{\\displaystyle P\(0.4\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/aa31d5f5badf86512fbf2c98d253057c419d5013) Pollen from Bamboo Field.

  
Brown Bear: Coco-Pepp-Clove-Pine  | 35  | 

  * Collect  P ( 0.3 ) {\displaystyle P(0.3)} ![{\\displaystyle P\(0.3\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/222d1ff266cc433446ebca6d84467ec05ff1f2cb) Pollen from Coconut Field.
  * Collect  P ( 0.3 ) {\displaystyle P(0.3)} ![{\\displaystyle P\(0.3\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/222d1ff266cc433446ebca6d84467ec05ff1f2cb) Pollen from Pepper Patch.
  * Collect  P ( 0.3 ) {\displaystyle P(0.3)} ![{\\displaystyle P\(0.3\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/222d1ff266cc433446ebca6d84467ec05ff1f2cb) Pollen from Clover Field.
  * Collect  P ( 0.3 ) {\displaystyle P(0.3)} ![{\\displaystyle P\(0.3\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/222d1ff266cc433446ebca6d84467ec05ff1f2cb) Pollen from Pine Tree Forest.

  
Brown Bear: Coco-Mount-Cact-Rose  | 35  | 

  * Collect  P ( 0.3 ) {\displaystyle P(0.3)} ![{\\displaystyle P\(0.3\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/222d1ff266cc433446ebca6d84467ec05ff1f2cb) Pollen from Coconut Field.
  * Collect  P ( 0.3 ) {\displaystyle P(0.3)} ![{\\displaystyle P\(0.3\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/222d1ff266cc433446ebca6d84467ec05ff1f2cb) Pollen from Mountain Top Field.
  * Collect  P ( 0.3 ) {\displaystyle P(0.3)} ![{\\displaystyle P\(0.3\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/222d1ff266cc433446ebca6d84467ec05ff1f2cb) Pollen from Cactus Field.
  * Collect  P ( 0.3 ) {\displaystyle P(0.3)} ![{\\displaystyle P\(0.3\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/222d1ff266cc433446ebca6d84467ec05ff1f2cb) Pollen from Rose Field.

  
Brown Bear: Solo-Coco  | 35  | 

  * Collect  P ( 1.2 ) {\displaystyle P(1.2)} ![{\\displaystyle P\(1.2\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/89ab29aae504c27ba0d304fcb9db3aac81d098c4) Pollen from Coconut Field.

  
Brown Bear: Solo-Stump  | 40  | 

  * Collect  P ( 1.2 ) {\displaystyle P(1.2)} ![{\\displaystyle P\(1.2\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/89ab29aae504c27ba0d304fcb9db3aac81d098c4) Pollen from Stump Field.

  
Brown Bear: Red-Stump-Mush  | 40  | 

  * Collect  P ( 0.8 ) {\displaystyle P(0.8)} ![{\\displaystyle P\(0.8\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/97e247d88e213f76649a482a3a1adaada18dcd3c) Red Pollen.
  * Collect  P ( 0.7 ) {\displaystyle P(0.7)} ![{\\displaystyle P\(0.7\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/a92eb2607902646941cb45f409fb8d3c38233448) Pollen from Stump Field.
  * Collect  P ( 0.3 ) {\displaystyle P(0.3)} ![{\\displaystyle P\(0.3\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/222d1ff266cc433446ebca6d84467ec05ff1f2cb) Pollen from Mushroom Field.

  
Brown Bear: Blue-Stump-Rose  | 40  | 

  * Collect  P ( 0.8 ) {\displaystyle P(0.8)} ![{\\displaystyle P\(0.8\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/97e247d88e213f76649a482a3a1adaada18dcd3c) Red Pollen.
  * Collect  P ( 0.7 ) {\displaystyle P(0.7)} ![{\\displaystyle P\(0.7\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/a92eb2607902646941cb45f409fb8d3c38233448) Pollen from Stump Field.
  * Collect  P ( 0.3 ) {\displaystyle P(0.3)} ![{\\displaystyle P\(0.3\)}](https://services.fandom.com/mathoid-facade/v1/media/math/render/svg/222d1ff266cc433446ebca6d84467ec05ff1f2cb) Pollen from Rose Field.

  
  
## Rewards[[](https://auth.fandom.com/signin?redirect=https%3A%2F%2Fbee-swarm-simulator.fandom.com%2Fwiki%2FBrown_Bear%3Fveaction%3Dedit%26section%3D4&uselang=en&metadata=article-registration-edit-article-section "Sign in to edit")]

Each quest always rewards ![Ticket](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Ticket](/wiki/Ticket "Ticket"), and increasing amounts of ![Royal Jelly](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)[Royal Jellies](/wiki/Royal_Jelly "Royal Jelly") and ![Honey](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)[Honey](/wiki/Honey "Honey") depending on the difficulty of the current quest. Every 3 quests, the player is also rewarded ![Jelly Beans](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)3 [Jelly Beans](/wiki/Jelly_Beans "Jelly Beans"). Certain thresholds may reward other items as well. 

The amount of ![Royal Jelly](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)[Royal Jellies](/wiki/Royal_Jelly "Royal Jelly") rewarded can be found using the below table. 

Number of quests completed  | ![Royal Jelly](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)[Royal Jelly](/wiki/Royal_Jelly "Royal Jelly") amount   
---|---  
0-5 | 1   
6-15 | 2   
16-25 | 3   
26-30 | 5   
31-40 | 10   
41-50 | 20   
51-60 | 30   
61-75 | 50   
76-100 | 100   
101-110 | 125   
111-120 | 150   
121-125 | 250   
126-150 | 500   
151-200 | 750   
201-225 | 1,000   
226-250 | 1,500   
251-300 | 2,000   
301-350 | 3,000   
351-400 | 5,000   
401-450 | 7,500   
451-500 | 10,000   
501-525 | 12,500   
526-550 | 15,000   
551-575 | 25,000   
576-600 | 50,000   
601-700 | 100,000   
701-800 | 250,000   
801-900 | 500,000   
901-1,000 | 1,000,000   
1,001-1,250 | 1,250,000   
1,251-1,500 | 1,500,000   
1,501-2,000 | 2,000,000   
2,001-2,250 | 2,250,000   
2,251-2,500 | 2,500,000   
  
Every known milestone is listed below. Bolded quest numbers are special milestones that Brown Bear notifies the player about in their dialogue. 

Quest Number  | Reward   
---|---  
5  | ![Field Dice](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)3 [Field Dice](/wiki/Field_Dice "Field Dice")  
10  | ![Micro-Converter](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Micro-Converters](/wiki/Micro-Converter "Micro-Converter")  
15  | ![Field Dice](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Field Dice](/wiki/Field_Dice "Field Dice")  
20  | ![Bitterberry](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)25 [Bitterberries](/wiki/Bitterberry "Bitterberry")  
**25** | ![Silver Egg](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Silver Egg](/wiki/Egg#Silver_Egg "Egg")  
30  | ![Micro-Converter](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Micro-Converters](/wiki/Micro-Converter "Micro-Converter")  
35  | ![Oil](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Oil](/wiki/Oil "Oil")  
40  | ![Bitterberry](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)50 [Bitterberries](/wiki/Bitterberry "Bitterberry")  
45  | ![Enzymes](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Enzymes](/wiki/Enzymes "Enzymes")  
**50** | ![Gold Egg](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Gold Egg](/wiki/Egg#Gold_Egg "Egg")  
55  | ![Magic Bean](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Magic Bean](/wiki/Magic_Bean "Magic Bean")  
60  | ![Bitterberry](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)50 [Bitterberries](/wiki/Bitterberry "Bitterberry")  
65  | ![Field Dice](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Field Dice](/wiki/Field_Dice "Field Dice")  
70  | ![Micro-Converter](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Micro-Converters](/wiki/Micro-Converter "Micro-Converter")  
**75** | ![Diamond Egg](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Diamond Egg](/wiki/Egg#Diamond_Egg "Egg")  
80  | ![Micro-Converter](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)10 [Micro-Converters](/wiki/Micro-Converter "Micro-Converter")  
85  | ![Tropical Drink](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Tropical Drink](/wiki/Tropical_Drink "Tropical Drink")  
90  | ![Star Jelly](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Star Jelly](/wiki/Royal_Jelly#Star_Jelly "Royal Jelly")  
95  | ![Gumdrops](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)100 [Gumdrops](/wiki/Gumdrops "Gumdrops")  
**100** | ![Mythic Egg](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Mythic Egg](/wiki/Egg#Mythic_Egg "Egg")  
105  | ![Oil](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Oil](/wiki/Oil "Oil")  
111  | ![Box-O-Frogs](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Boxes-O-Frogs](/wiki/Box-O-Frogs "Box-O-Frogs")  
115  | ![Enzymes](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Enzymes](/wiki/Enzymes "Enzymes")  
120  | ![Magic Bean](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Magic Bean](/wiki/Magic_Bean "Magic Bean")  
123  | ![Hivesticker shy brown bear](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 **Shy Brown Bear Sticker**  
125  | ![Atomic Treat](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Atomic Treat](/wiki/Atomic_Treat "Atomic Treat")  
130  | ![Enzymes](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Enzymes](/wiki/Enzymes "Enzymes")  
135  | ![Bitterberry](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)50 [Bitterberries](/wiki/Bitterberry "Bitterberry")  
140  | ![Glue](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Glue](/wiki/Glue "Glue")  
145  | ![Field Dice](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Field Dice](/wiki/Field_Dice "Field Dice")  
**150** | ![Ticket](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)100 [Tickets](/wiki/Ticket "Ticket")  
155  | ![Micro-Converter](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Micro-Converters](/wiki/Micro-Converter "Micro-Converter")  
160  | ![Oil](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)3 [Oils](/wiki/Oil "Oil")  
165  | ![Enzymes](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Enzymes](/wiki/Enzymes "Enzymes")  
170  | ![Micro-Converter](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Micro-Converters](/wiki/Micro-Converter "Micro-Converter")  
175  | ![Gumdrops](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)100 [Gumdrops](/wiki/Gumdrops "Gumdrops")  
180  | ![Bitterberry](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)50 [Bitterberries](/wiki/Bitterberry "Bitterberry")  
185  | ![Oil](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Oil](/wiki/Oil "Oil")  
190  | ![Magic Bean](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Magic Bean](/wiki/Magic_Bean "Magic Bean")  
195  | ![Star Jelly](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Star Jelly](/wiki/Royal_Jelly#Star_Jelly "Royal Jelly")  
**200** | ![Mythic Egg](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Mythic Egg](/wiki/Egg#Mythic_Egg "Egg")  
205  | ![Field Dice](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Field Dice](/wiki/Field_Dice "Field Dice")  
210  | ![Bitterberry](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)50 [Bitterberries](/wiki/Bitterberry "Bitterberry")  
215  | ![Micro-Converter](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Micro-Converters](/wiki/Micro-Converter "Micro-Converter")  
220  | ![Magic Bean](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Magic Bean](/wiki/Magic_Bean "Magic Bean")  
225  | ![Atomic Treat](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Atomic Treat](/wiki/Atomic_Treat "Atomic Treat")  
230  | ![Enzymes](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)3 [Enzymes](/wiki/Enzymes "Enzymes")  
235  | ![Glue](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Glue](/wiki/Glue "Glue")  
240  | ![Gumdrops](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)100 [Gumdrops](/wiki/Gumdrops "Gumdrops")  
245  | ![Bitterberry](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)50 [Bitterberries](/wiki/Bitterberry "Bitterberry")  
**250** | ![Ticket](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)250 [Tickets](/wiki/Ticket "Ticket")  
255  | ![Oil](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)3 [Oils](/wiki/Oil "Oil")  
260  | ![Box-O-Frogs](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Boxes-O-Frogs](/wiki/Box-O-Frogs "Box-O-Frogs")  
265  | ![Field Dice](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Field Dice](/wiki/Field_Dice "Field Dice")  
270  | ![Micro-Converter](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Micro-Converters](/wiki/Micro-Converter "Micro-Converter")  
**275** | ![Gifted Gold Egg](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Gifted Gold Egg](/wiki/Egg#Gifted_Gold_Egg "Egg")  
280  | ![Magic Bean](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Magic Bean](/wiki/Magic_Bean "Magic Bean")  
285  | ![Oil](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)3 [Oils](/wiki/Oil "Oil")  
290  | ![Gumdrops](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)100 [Gumdrops](/wiki/Gumdrops "Gumdrops")  
295  | ![Bitterberry](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)50 [Bitterberries](/wiki/Bitterberry "Bitterberry")  
**300** | ![Brown Cub](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Brown Cub](/wiki/Cub_Buddy#Skins "Cub Buddy")  
305  | ![Enzymes](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)3 [Enzymes](/wiki/Enzymes "Enzymes")  
310  | ![Glue](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)3 [Glues](/wiki/Glue "Glue")  
315  | ![Star Jelly](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)3 [Star Jellies](/wiki/Royal_Jelly#Star_Jelly "Royal Jelly")  
320  | ![Field Dice](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Field Dice](/wiki/Field_Dice "Field Dice")  
325  | ![Micro-Converter](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)10 [Micro-Converters](/wiki/Micro-Converter "Micro-Converter")  
330  | ![Bitterberry](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)75 [Bitterberries](/wiki/Bitterberry "Bitterberry")  
333  | ![Box-O-Frogs](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)3 [Boxes-O-Frogs](/wiki/Box-O-Frogs "Box-O-Frogs")  
335  | ![Gumdrops](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)150 [Gumdrops](/wiki/Gumdrops "Gumdrops")  
340  | ![Gold Egg](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Gold Egg](/wiki/Egg#Gold_Egg "Egg")  
345  | ![Magic Bean](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)3 [Magic Beans](/wiki/Magic_Bean "Magic Bean")  
**350** | ![Ticket](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)250 [Tickets](/wiki/Ticket "Ticket")  
355  | ![Enzymes](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Enzymes](/wiki/Enzymes "Enzymes")  
360  | ![Oil](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Oils](/wiki/Oil "Oil")  
365  | ![Field Dice](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Field Dice](/wiki/Field_Dice "Field Dice")  
370  | ![Bitterberry](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)75 [Bitterberries](/wiki/Bitterberry "Bitterberry")  
375  | ![Atomic Treat](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Atomic Treat](/wiki/Atomic_Treat "Atomic Treat")  
380  | ![Micro-Converter](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Micro-Converters](/wiki/Micro-Converter "Micro-Converter")  
385  | ![Micro-Converter](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)10 [Micro-Converters](/wiki/Micro-Converter "Micro-Converter")  
390  | ![Gold Egg](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Gold Egg](/wiki/Egg#Gold_Egg "Egg")  
395  | ![Glue](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Glues](/wiki/Glue "Glue")  
**400** | ![Mythic Egg](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Mythic Egg](/wiki/Egg#Mythic_Egg "Egg")  
405  | ![Gumdrops](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)50 [Gumdrops](/wiki/Gumdrops "Gumdrops")  
410  | ![Oil](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)10 [Oils](/wiki/Oil "Oil")  
415  | ![Field Dice](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Field Dice](/wiki/Field_Dice "Field Dice")  
420  | ![Neonberry](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)4 [Neonberries](/wiki/Neonberry "Neonberry")  
**425** | ![Gifted Diamond Egg](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Gifted Diamond Egg](/wiki/Egg#Gifted_Diamond_Egg "Egg")  
430  | ![Micro-Converter](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)10 [Micro-Converters](/wiki/Micro-Converter "Micro-Converter")  
435  | ![Enzymes](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)10 [Enzymes](/wiki/Enzymes "Enzymes")  
440  | ![Gifted Silver Egg](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Gifted Silver Egg](/wiki/Egg#Gifted_Silver_Egg "Egg")  
444  | ![Box-O-Frogs](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)4 [Boxes-O-Frogs](/wiki/Box-O-Frogs "Box-O-Frogs")  
445  | ![Magic Bean](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)3 [Magic Beans](/wiki/Magic_Bean "Magic Bean")  
**450** | ![Ticket](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)250 [Tickets](/wiki/Ticket "Ticket")  
455  | ![Magic Bean](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Magic Beans](/wiki/Magic_Bean "Magic Bean")  
460  | ![Field Dice](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)7 [Field Dice](/wiki/Field_Dice "Field Dice")  
465  | ![Star Jelly](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Star Jellies](/wiki/Royal_Jelly#Star_Jelly "Royal Jelly")  
470  | ![Glue](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Glues](/wiki/Glue "Glue")  
475  | ![Box-O-Frogs](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Boxes-O-Frogs](/wiki/Box-O-Frogs "Box-O-Frogs")  
480  | ![Oil](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)15 [Oils](/wiki/Oil "Oil")  
485  | ![Bitterberry](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)75 [Bitterberries](/wiki/Bitterberry "Bitterberry")  
490  | ![Micro-Converter](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)15 [Micro-Converters](/wiki/Micro-Converter "Micro-Converter")  
495  | ![Gold Egg](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Gold Egg](/wiki/Egg#Gold_Egg "Egg")  
**500** | ![Star Treat](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Star Treat](/wiki/Star_Treat "Star Treat")  
505  | ![Enzymes](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)15 [Enzymes](/wiki/Enzymes "Enzymes")  
510  | ![Glue](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Glues](/wiki/Glue "Glue")  
515  | ![Field Dice](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)8 [Field Dice](/wiki/Field_Dice "Field Dice")  
520  | ![Tropical Drink](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)10 [Tropical Drinks](/wiki/Tropical_Drink "Tropical Drink")  
525  | ![Diamond Egg](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Diamond Egg](/wiki/Egg#Diamond_Egg "Egg")  
530  | ![Oil](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)25 [Oils](/wiki/Oil "Oil")  
535  | ![Magic Bean](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Magic Beans](/wiki/Magic_Bean "Magic Bean")  
540  | ![Bitterberry](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)75 [Bitterberries](/wiki/Bitterberry "Bitterberry")  
545  | ![Micro-Converter](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)15 [Micro-Converters](/wiki/Micro-Converter "Micro-Converter")  
**550** | ![Ticket](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)250 [Tickets](/wiki/Ticket "Ticket")  
555  | ![Box-O-Frogs](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Boxes-O-Frogs](/wiki/Box-O-Frogs "Box-O-Frogs")  
560  | ![Gumdrops](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)200 [Gumdrops](/wiki/Gumdrops "Gumdrops")  
565  | ![Enzymes](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)25 [Enzymes](/wiki/Enzymes "Enzymes")  
570  | ![Oil](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)25 [Oils](/wiki/Oil "Oil")  
575  | ![Magic Bean](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)7 [Magic Beans](/wiki/Magic_Bean "Magic Bean")  
580  | ![Star Jelly](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)10 [Star Jellies](/wiki/Royal_Jelly#Star_Jelly "Royal Jelly")  
585  | ![Tropical Drink](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)15 [Tropical Drinks](/wiki/Tropical_Drink "Tropical Drink")  
590  | ![Bitterberry](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)100 [Bitterberries](/wiki/Bitterberry "Bitterberry")  
595  | ![Atomic Treat](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)3 [Atomic Treats](/wiki/Atomic_Treat "Atomic Treat")  
**600** | ![Mythic Egg](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Mythic Egg](/wiki/Egg#Mythic_Egg "Egg")  
**650** | ![Ticket](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)250 [Tickets](/wiki/Ticket "Ticket")  
**700** | ![Mythic Egg](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Mythic Egg](/wiki/Egg#Mythic_Egg "Egg")  
**750** | ![Ticket](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)500 [Tickets](/wiki/Ticket "Ticket")  
**800** | ![Mythic Egg](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Mythic Egg](/wiki/Egg#Mythic_Egg "Egg")  
**1000** | ![Star Treat](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Star Treats](/wiki/Star_Treat "Star Treat")  
  
## Dialogue[[](https://auth.fandom.com/signin?redirect=https%3A%2F%2Fbee-swarm-simulator.fandom.com%2Fwiki%2FBrown_Bear%3Fveaction%3Dedit%26section%3D5&uselang=en&metadata=article-registration-edit-article-section "Sign in to edit")]

Quest  | Dialogue   
---|---  
First quest  | Hey there bud! Ready to get started? The road to an awesome hive is paved by [Royal Jelly]! If you want to unlock Epic, Legendary, and even Mythic Bees, you'll need [Royal Jelly] for sure. I've got plenty to share, and not just [Royal Jelly]... After certain milestones, I'll give all sorts of cool rewards, including Gold, Diamond, and even Mythic [Eggs]! But those'll _[sic]_ come way down the road. For now, let's keep it simple. Check out the quest I've put in your Quest Menu, and report back when you've collected all the pollen. _-During-_ Looks like you haven't quite finished my quest yet. Check the quest menu, then collect all of the requested pollen. Come back when the meters are filled all the way up, and I'll give you your prize! _-Completion-_ Great job bud! Here's some [Royal Jelly]. You've completed [# of Brown Bear quests] of my quests so far. Complete [#] more, and I'll give you [milestone reward]. And if you complete [#] more, I'll give you a [major milestone reward]! I haven't quite finished preparing the next quest for you. Come back to me in [time left], and we'll be ready to roll.   
Repeatable Quests  | Welcome back! You ready for a new quest? Complete it and I'll give you some [Royal Jelly] - and a [Ticket]! You've completed [# of Brown Bear quests] of my quests so far. And every new quest becomes a bit more challenging. Check your Quest Menu to see what's up next! _-During-_ Looks like you haven't quite finished my quest yet. Check the quest menu, then collect all of the requested pollen. Come back when the meters are filled all the way up, and I'll give you your prize! _-Completion-_ Great job bud! Here's some [Royal Jelly]. You've completed [# of Brown Bear quests] of my quests so far. Complete [#] more, and I'll give you [milestone reward]. And if you complete [#] more, I'll give you a [major milestone reward]!  
_Past Cooldown_  
Looks like it's been over an hour since I gave you your last quest. Talk to me again when you're ready for the next one. _Cooldown_ I haven't quite finished preparing the next quest for you. Come back to me in [time left], and we'll be ready to roll.   
Reaching Major Milestone  | _Completion_ Great job bud! Here's some [Royal Jelly]. And, more importantly, a [milestone reward]! You've completed [# of Brown Bear quests] of my quests so far. Complete [#] more, and I'll give you [milestone reward]. And if you complete [#] more, I'll give you a [major milestone reward]!   
Reaching Minor Milestone  | _Completion_ Great job bud! Here's some [Royal Jelly]. And, as a bonus: [milestone reward]! You've completed [# of Brown Bear quests] of my quests so far. Complete [#] more, and I'll give you [milestone reward]. And if you complete [#] more, I'll give you a [major milestone reward]!   
Cooldown  | Remember, I can only give one quest once an hour. I need a bit more time to finish preparing your next reward. Check back with me in [time left], and we'll be ready to go!   
Exclusive Beesmas Dialogue 2018  | What's up, bud? **You are given a choice to give a present to Brown Bear or continue talking like normal. You choose to give him a present.** Ah, of course! Time to exchange some Beemas gifts. Let me see what you got me this year... Whoa! A 1-year subscription to Bearmazon Prime! I'll get so much out of this, you have NO idea! Thanks buddy. Here's a little something I know you're gonna love as well.   
Exclusive Beesmas Dialogue 2020  | Man, it's cold! **You are given a choice to give a present to Brown Bear or continue talking like normal. You choose to give him a present.** But not too cold for us to exchange gifts! SO what is it, huh? What'd you get ol' Brown Bear? Whoa! A 1-year subscription to Bearmazon Prime! I'll get so much out of this, you have NO idea! Thanks bud. Now look at what I got you, including the [Royal Jelly Ornament]! With this on the Beesmas Tree, you'll receive the following boosts: +25% Convert Rate; +25% Capacity in the Clover Field; and +20% Pollen from "Bomb" abilities! Happy Beesmas!   
Exclusive Beesmas Dialogue 2021  | Man, it's cold! **You are given a choice to give a present to Brown Bear or continue talking like normal. You choose to give him a present.** But not too cold for us to exchange gifts! So what is it, huh? What'd you get ol' Brown Bear? Whoa! A 1 year subscription to Bearmazon Prime! I'll get so much out of this, you have NO idea! Thanks bud. Now look at what I got you, including the [Royal Jelly Ornament]! With that on the Beesmas Tree, you'll receive the following boosts: +25% Convert Rate; +25% Capacity in the Clover Field; And +20% Pollen from "Bomb" abilities! Happy Beesmas!   
Exclusive Beesmas Dialogue 2022  | Man, it's cold! **You are given a choice to give a present to Brown Bear or continue talking like normal. You choose to give him a present.** Maybe your present will help warm me up! Can't wait to find out. ...(krumple krumple)... Whoa! A 25$ Ubear Eats gift card! I'm ordering some warm soup and hot cocoa right away. I hope they deliver to ROBLOX games... Thanks bud. Now check out what I got you, some [Royal Jelly], a [Glue]... And the [Royal Jelly Ornament]! With that on the Beesmas Tree, you'll receive the following boosts: +25% Convert Rate +25% Capacity in the Clover Field And +20% Pollen from "Bomb" abilities! Happy Beesmas!   
Exclusive Beesmas Dialogue 2024 Summer  | Man, it's REALLY cold this summer! **You are given a choice to give a present to Brown Bear or continue talking like normal. You choose to give him a present.** You got something in that [Present] that could warm me up? ...(krumple krumple)... Whoa! It's a 90 day membership to Beequinox, the bougiest bee-themed gym around! I think they've even got a steam room! That'll warm me up for sure. Is this you hinting that I need to work out more? Haha! Just playing. Thanks bud! Now check out what I got YOU: the [Royal Jelly Ornament]! With that on the Beesmas Tree, you'll receive the following boosts: +25% Convert Rate, +25% Capacity in the Clover Field And +20% Pollen from "Bomb" abilities! Happy Beesmas!   
Exclusive Beesmas Dialogue 2024 Winter  | Brrrr, it's cold! **You are given a choice to give a present to Brown Bear or continue talking like normal. You choose to give him a present.** But not too cold for us to exchange gifts! So what is it, huh? What'd you get ol' Brown Bear? ...(krumple krumple)... Whoa! A 12 month subscription to ChatGPBee! Not sure exactly how I'll use this, but I'll try it out! Maybe it can come up with quests to give you. Or maybe it can just keep me company. Thanks bud! Now look at what I got you, including the [Royal Jelly Ornament]! With that on the Beesmas Tree, you'll receive the following boosts: +25% Convert Rate +25% Capacity in the Clover Field And +20% Pollen from "Bomb" abilities! Happy Beesmas!   
  
## Beesmas Quest - Brown Bear's Stockings[[](https://auth.fandom.com/signin?redirect=https%3A%2F%2Fbee-swarm-simulator.fandom.com%2Fwiki%2FBrown_Bear%3Fveaction%3Dedit%26section%3D6&uselang=en&metadata=article-registration-edit-article-section "Sign in to edit")]

  * 2025

  * 2024 (Winter)

  * 2024 (Summer)

  * 2022

  * 2021

  * 2020




Requirements  | Rewards   
---|---  
  
  * Collect 2,500,000 [Pollen](/wiki/Pollen "Pollen") from the [Clover Field](/wiki/Clover_Field "Clover Field").
  * Pop 10 [Blooms](/wiki/Blooms "Blooms") in the Clover Field.
  * Complete 10 Rounds in the [Retro Swarm Challenge](/wiki/Retro_Swarm_Challenge "Retro Swarm Challenge").
  * Collect 250 [Brick](/wiki/Brick "Brick") Tokens.
  * Collect 5 [Field Dice](/wiki/Field_Dice "Field Dice")
  * Defeat 25 [Ladybugs](/wiki/Ladybug "Ladybug")
  * Defeat 25 [Rhino Beetles](/wiki/Rhino_Beetle "Rhino Beetle")

| ![Honey](https://static.wikia.nocookie.net/bee-swarm-simulator/images/c/c6/Honey.png/revision/latest/scale-to-width-down/25?cb=20230410071605)5,000,000 [Honey](/wiki/Honey "Honey")  
![Ticket](https://static.wikia.nocookie.net/bee-swarm-simulator/images/1/1e/Ticket.png/revision/latest/scale-to-width-down/25?cb=20230404015820)10 [Tickets](/wiki/Ticket "Ticket")  
![Star Jelly](https://static.wikia.nocookie.net/bee-swarm-simulator/images/e/e7/Star_Jelly.png/revision/latest/scale-to-width-down/25?cb=20230404020706)1 [Star Jelly](/wiki/Royal_Jelly#Star_Jelly "Royal Jelly")  
![Smooth Dice](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Smooth Dice](/wiki/Smooth_Dice "Smooth Dice")  
![Snowflake](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)25 [Snowflakes](/wiki/Snowflake "Snowflake")  
Access to the [Stockings](/wiki/Stockings "Stockings")  
Quest  | Dialogue   
---|---  
Brown Bear's Stockings  |  Hey there bud! Merry Beesmas! You know, [Presents] are great and all, but there's something even better. Usually, they'd be hanging right on those hooks! That's right. I'm talking about stockings, stuffed full of goodies! But I've ran out of stuff to stuff them with. Hey... Could you help me gather more stuff? Just as a heads up, it won't be easy... To do this quest, you'll need to participate in the Retro Swarm Challenge. A minigame where you and your bees defend your hive from Zombies and Slimes! That means you'll need at least 10 bees! You can find the portal to the Retro Swarm Challenge beyond the 10 Bee Gate. Here's everything we'll need: Collect 2,500,00 Pollen from the Clover Field... Pop 10 Blooms in the Clover Field... Complete 10 Rounds in the Retro Swarm Challenge... Collect 250 [Brick] Tokens... Collect 5 [Field Dice]... And defeat 25 Ladybugs and Rhino Beetles! _\- During -_  
N/A _\- Completion -_  
That's all we need. Lets [sic] stuff these stockings right up! We're putting a little bit of everything in here... Alright! Those are some well-stuffed Stockings! Double-stuffed with Beesmas fluff! Now that there [sic] up there, you can use the Stockings once every hour. You'll get 3 suprises [sic] each time, and you never know what they'll be! But I can guarantee at least 1 will be a Beequip for your bees to enjoy. Once you obtain a [Beequip Case], that is. Thanks for the help bud! Happy Honeydays!   
  
![Hivesticker eviction](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D) | **This piece of content goes bye bye.** The following content has been removed from the game. The contents below may be archival, but feel free to edit below.  
---|---  
Requirements  | Rewards   
---|---  
  
  * Collect 750,000 Red [Pollen](/wiki/Pollen "Pollen")
  * Collect 250,000 Pollen from the [Clover Field](/wiki/Clover_Field "Clover Field")
  * Defeat 10 [Ladybugs](/wiki/Ladybug "Ladybug")
  * Collect 50 [Bomb](/wiki/Ability_Tokens#Bomb "Ability Tokens") Tokens
  * Collect 3 [Field Dice](/wiki/Field_Dice "Field Dice")
  * Collect 3 [Stickers](/wiki/Sticker "Sticker") without [Trading](/wiki/Trading "Trading")

| ![Honey](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)4,000,000 [Honey](/wiki/Honey "Honey")  
![Ticket](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)5 [Tickets](/wiki/Ticket "Ticket")  
![Smooth Dice](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Smooth Dice](/wiki/Smooth_Dice "Smooth Dice")  
![Hard Wax](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Hard Wax](/wiki/Hard_Wax "Hard Wax")  
![Gingerbread Bear](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Gingerbread Bear](/wiki/Gingerbread_Bear "Gingerbread Bear")  
Quest  | Dialogue   
---|---  
Brown Bear's Stockings  | Hey there bud! Happy Honeydays! I’m trying to make things cozy around the Clover Field by setting up a fireplace. But there’s something missing… We need some Stockings to hang on those hooks! Will you help me stuff some up? Here’s what we’ll need: Collect 750,000 Red Pollen… Collect 250,000 Pollen from the Clover Field… Defeat 10 Ladybugs… Collect 50 Bomb Tokens… Collect 3 Field Dice… And collect 3 Stickers! You can find hidden Stickers stuck on walls around the map, and from many other sources. Check the Sticker Index in your Egg Menu for more information. _\- During -_  
N/A _\- Completion -_  
That's all we need. Let's stuff those Stockings! ...(crump crump)... Alright! Now that's a cozy fireplace! And now let's hang em up! There's a little bit of everything in those Stockings. Now that there [sic] up there, you can use them once every hour. You'll get 3 suprises [sic] each time, and you never know what they'll be! But 1 will almost always be a Beequip for your bees to enjoy. Thanks for the help bud! Happy Honeydays!   
  
![Hivesticker eviction](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D) | **This piece of content goes bye bye.** The following content has been removed from the game. The contents below may be archival, but feel free to edit below.  
---|---  
Requirements  | Rewards   
---|---  
  
  * Collect 200,000 [Pollen](/wiki/Pollen "Pollen") from the [Clover Field](/wiki/Clover_Field "Clover Field").
  * Collect 200,000 [Pollen](/wiki/Pollen "Pollen") with [Rare Bees](/wiki/Bees/Rare "Bees/Rare").
  * Defeat 10 [Ladybugs](/wiki/Ladybug "Ladybug").
  * Collect 50 [Brick](/wiki/Brick "Brick") tokens.
  * Obtain 3 [Field Dice](/wiki/Field_Dice "Field Dice") to give to Brown Bear.
  * Obtain 1 Green Plus Sign [Sticker](/wiki/Sticker "Sticker") to give to Brown Bear.

| 1,000,000 [Honey](/wiki/Honey "Honey")  
10x [Tickets](/wiki/Ticket "Ticket")  
3x [Royal Jelly](/wiki/Royal_Jelly "Royal Jelly")  
3x [Whirligigs](/wiki/Whirligig "Whirligig")  
1x [Red Extract](/wiki/Red_Extract "Red Extract")  
1x [Blue Extract](/wiki/Blue_Extract "Blue Extract")  
25x [Snowflakes](/wiki/Snowflake "Snowflake")  
Access to the [Stockings](/wiki/Stockings "Stockings")  
Quest  | Dialogue   
---|---  
Brown Bear's Stockings  | Hey there bud! Merry Beesmas! Or is it Summermas? Things are weird this year. Look at all this snow! Wouldn't it be great if we could warm up around a fire? That's why I've up this fireplace! But it's just not Beesmas without Stocking [sic] on the mantle... If you help me stuff some Stockings, I'll have some special rewards for you! It'll be fun! Sound like a deal? For this quest, you'll need to collect [Brick] tokens. Those can only be found through the portal near the Stump Field. HEY! You're paying attention, right? This is important, don't want you to get lost. The portal to the Retro Swarm Challenge is past the Stump Field, behind the Pineapple Patch in the 10 Bee Zone. Once you're in there, join a team and defeat some Brick Blooms! You'll also need to find me a specific Sticker. Look up the Sticker in the Sticker Index to see where it can be found. Lets _[sic]_ stuff those Stockings and get that fireplace rolling! Good luck! _-During-_ N/A _-Completion-_ That's all we need. Let's stuff those Stockings! ...(crump crump)... And now let's hang em up! Alright! Now that's what I call a fireplace! There's a little bit of everything in those Stockings. Now that there _[sic]_ up there, you can use them once every hour. You'll get 3 suprises _[sic]_ each time, and you never know what they'll be! But I can guarantee at least 1 will be a Beequip for your bees to enjoy. Thanks for the help bud! Happy Honeydays!   
  
![Hivesticker eviction](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D) | **This piece of content goes bye bye.** The following content has been removed from the game. The contents below may be archival, but feel free to edit below.  
---|---  
Requirements  | Rewards   
---|---  
  
  * Collect 8,000 [Pollen](/wiki/Pollen "Pollen") from the [Mushroom Field](/wiki/Mushroom_Field "Mushroom Field").
  * Collect 8,000 [Pollen](/wiki/Pollen "Pollen") from the [Blue Flower Field](/wiki/Blue_Flower_Field "Blue Flower Field").
  * Collect 25 Tokens from [Ladybugs](/wiki/Ladybug "Ladybug").
  * Collect 25 Tokens from [Rhino Beetles](/wiki/Rhino_Beetle "Rhino Beetle").
  * Use 1 [Field Dice](/wiki/Field_Dice "Field Dice").
  * Use 1 [Micro-Converter](/wiki/Micro-Converter "Micro-Converter").

| 30,000 [Honey](/wiki/Honey "Honey")  
1× [Royal Jelly](/wiki/Royal_Jelly "Royal Jelly")  
1× [Atomic Treat](/wiki/Atomic_Treat "Atomic Treat")  
5× [Whirligigs](/wiki/Whirligig "Whirligig")  
1× [Gingerbread Bear](/wiki/Gingerbread_Bear "Gingerbread Bear")  
Quest  | Dialogue   
---|---  
Brown Bear's Stockings  |  Hey there bud! Merry Beesmas! I've been working overtime to try to put together something special for you beekeepers... But I'm falling a bit behind, heh. See, those hooks are made for Stockings, and that's just what we'll do. Help me stuff those Stockings, and some [Royal Jelly] I'll give to you. Here's what we'll need: Collect 8,000 pollen from the Mushroom Field... Collect 8,000 pollen from the Blue Flower Field... Collect 25 Tokens from Ladybugs... Collect 25 Tokens from Rhino Beetles... Use 1 [Field Dice]... And use 1 [Micro-Converter]! _-During-_ N/A _-Completion-_ That's all we need. Lets just stuff em[sic] right up! We're putting a little bit of everything in these... Alright! Those are some well-stuffed Stockings! Double-stuffed with Beesmas fluff! Now that there up there, you can use the Stockings once every hour. You'll get 3 suprises[sic] each time, and you never know what they'll be! But I can guarantee at least 1 will be a Beequip for your bees to enjoy. Thanks for the help bud! Happy Honeydays!   
  
![Hivesticker eviction](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D) | **This piece of content goes bye bye.** The following content has been removed from the game. The contents below may be archival, but feel free to edit below.  
---|---  
Requirements  | Rewards   
---|---  
  
  * Collect 10,000 [Pollen](/wiki/Pollen "Pollen") from the [Clover Field](/wiki/Clover_Field "Clover Field").
  * Collect 7,500 [Red Pollen](/wiki/Pollen "Pollen").
  * Collect 7,500 [Blue Pollen](/wiki/Pollen "Pollen").
  * Defeat 3 [Ladybugs](/wiki/Ladybug "Ladybug").
  * Defeat 3 [Rhino Beetles](/wiki/Rhino_Beetle "Rhino Beetle").
  * Collect 25 [Ability Tokens](/wiki/Ability_Tokens "Ability Tokens").

| 30,000 [Honey](/wiki/Honey "Honey")  
3x [Tickets](/wiki/Ticket "Ticket")  
1x [Royal Jelly](/wiki/Royal_Jelly "Royal Jelly")  
1x [Magic Bean](/wiki/Magic_Bean "Magic Bean")  
3x [Micro-Converters](/wiki/Micro-Converter "Micro-Converter")  
10x [Snowflakes](/wiki/Snowflake "Snowflake")  
Access to the [Stockings](/wiki/Stockings "Stockings")  
Quest  | Dialogue   
---|---  
Brown Bear's Stockings  | Hey there bud! Merry Beesmas! I've been working overtime to try to put something special together for you beekeepers... But I'm falling a bit behind, heh. See, those hooks are made for Stockings, and that's just what we'll do. Help me stuff those Stockings, and some [Royal Jelly] I'll give to you. Here's what we'll need: Collect 10,000 Pollen from the Blue Flower Field... Collect 10,000 Pollen from the Clover Field... Collect 7,500 Red pollen... Collect 7,500 Red pollen... Defeat 3 Ladybugs and 3 Rhino Beetles... And collect 25 Ability Tokens! _[sic see note below]_ _-During-_ N/A _-Completion-_ That's all we need. Lets just stuff em right up! We're putting a little bit of everything in these... Alright! Those are some well-stuffed Stockings! Double-stuffed with Beesmas fluff! Now that there up there _[sic]_ , you can use the Stockings once every hour. You'll get 3 surprises each time, and you never know what they'll be! But I can guarantee at least 1 will be a Beequip for your bees to enjoy. Thanks for the help bud! Happy Honeydays!   
NOTE: Just like last year, the dialogue for Brown Bear does not match up with the requirements. The requirements are correct.

![Hivesticker eviction](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D) | **This piece of content goes bye bye.** The following content has been removed from the game. The contents below may be archival, but feel free to edit below.  
---|---  
Requirements  | Rewards   
---|---  
  
  * Collect 10,000 [Red Pollen](/wiki/Pollen "Pollen")
  * Collect 10,000 [Pollen](/wiki/Pollen "Pollen") from the [Dandelion Field](/wiki/Dandelion_Field "Dandelion Field")
  * Collect 20 Tokens from [Ladybugs](/wiki/Ladybug "Ladybug")
  * Collect 30 [Ability Tokens](/wiki/Ability_Tokens "Ability Tokens")

| 25,000 [Honey](/wiki/Honey "Honey")  
10x [Snowflake](/wiki/Snowflake "Snowflake")  
3x [Micro-Converter](/wiki/Micro-Converter "Micro-Converter")  
1x [Royal Jelly](/wiki/Royal_Jelly "Royal Jelly")  
Access to the [Stockings](/wiki/Stockings "Stockings")  
Quest  | Dialogue   
---|---  
Brown Bear's Stockings  | Hey there bud! Happy Honeydays! I've been working overtime to try to put something special together for you beekeepers... But I'm falling a bit behind, heh. See, those hooks are made for Stockings, and that's just what we'll do. Help me stuff those Stockings, and some [Royal Jelly] I'll give to you. Here's what we'll need: Collect 10,000 Pollen from the Blue Flower Field... Collect 10,000 Pollen from the Mushroom Field... Collect 15 Tokens from Ladybugs and collect 30 Ability Tokens! _[sic see note below]_ _-During-_ N/A _-Completion-_ That's all we need. Lets just stuff em right up! We're putting a little bit of everything in these... Alright! Those are some well-stuffed Stockings! Double-stuffed with Beesmas fluff! Now that there up there _[sic]_ , you can use the Stockings once every hour. You'll get 3 surprises each time, and you never know what they'll be! But I can guarantee at least 1 will be a Beequip for your bees to enjoy. Thanks for the help bud! Happy Honeydays!   
NOTE: The dialogue for Brown Bear does not match up with the requirements. The requirements are correct.

## Other Quests[[](https://auth.fandom.com/signin?redirect=https%3A%2F%2Fbee-swarm-simulator.fandom.com%2Fwiki%2FBrown_Bear%3Fveaction%3Dedit%26section%3D7&uselang=en&metadata=article-registration-edit-article-section "Sign in to edit")]

  * Bee Swarm Fall 2024 Quest

  * Egg Hunt (2020)

  * 2019 Ornament Quest

  * Egg Hunt (2019)




![Hivesticker eviction](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D) | **This piece of content goes bye bye.** The following content has been removed from the game. The contents below may be archival, but feel free to edit below.  
---|---  
Quest  | Requirements  | Rewards   
---|---|---  
⌛Waiting With Sun Bear (3/6): And Brown Bear  | 

  * Earn 3 Clover Badges.
  * Use 25 [Royal Jellies](/wiki/Royal_Jelly "Royal Jelly")
  * Collect 12,500,000 Pollen from the [Clover Field](/wiki/Clover_Field "Clover Field").
  * Collect 5,000,000 Pollen with the [Vacuum](/wiki/Vacuum "Vacuum").
  * Collect 250 Tokens from [Honeystorms](/wiki/Honeystorm "Honeystorm").
  * Collect 10 [Stingers](/wiki/Stinger "Stinger").
  * Collect 5 [Hard Waxes](/wiki/Hard_Wax "Hard Wax").
  * Collect 5 [Red Extracts](/wiki/Red_Extract "Red Extract").
  * Collect 5 [Blue Extracts](/wiki/Blue_Extract "Blue Extract").
  * Apply 10 Stacks of [Clover Field](/wiki/Clover_Field "Clover Field") Boost
  * Defeat 25 [Rhino Beetles](/wiki/Rhino_Beetle "Rhino Beetle")
  * Defeat 10 [Giant Ants](/wiki/Giant_Ant "Giant Ant")

| 50,000,000 [Honey](/wiki/Honey "Honey")  
20x [Tickets](/wiki/Ticket "Ticket")  
5x [Enzymes](/wiki/Enzymes "Enzymes")  
1x [Red Balloon](/wiki/Red_Balloon "Red Balloon")  
1x Star Jelly  |   
Quest  | Dialogue   
---|---  
⌛Waiting With Sun Bear (3/6): And Brown Bear  | Hey there bud! Mother Bear sent you, right? No need to explain. Sun Bear told me the whole spiel. Us bears are giving you quests to buy more time for the developer of this game. Well, let's get right into it! I'm not gonna ask questions. This quest out to keep you busy for a while! _-During-_ N/A _-Completion-_ Guess that quest was too easy! Either that, or Onett is just WAY slower than we thought. Nah. He's always been slow! He's been trying to open some lid up there for over 6 years. Everything lines up! Three more quests to go to earn that [Stranded Sun Bear Sticker]. I think Polar Bear's got the next one for you.   
  
![Hivesticker eviction](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D) | **This piece of content goes bye bye.** The following content has been removed from the game. The contents below may be archival, but feel free to edit below.  
---|---  
Quest  | Requirements  | Rewards   
---|---|---  
Commando Chick's Hideout  | 

  * Cut the vines
  * Capture 1 [Commando Chick](/wiki/Commando_Chick "Commando Chick")

| 

  * 1x [Rage Bee Jelly](/wiki/Royal_Jelly#Royal_Jelly_Variants "Royal Jelly") (Upon receiving quest)
  * 5x [Stinger](/wiki/Stinger "Stinger") (Upon receiving quest)



* * *

  * 10,000 [honey](/wiki/Honey "Honey")
  * 5x [Ticket](/wiki/Ticket "Ticket")
  * 1x [Royal Jelly](/wiki/Royal_Jelly "Royal Jelly")
  * 1x [Field Dice](/wiki/Field_Dice "Field Dice")
  * 25x [Gumdrops](/wiki/Gumdrops "Gumdrops")

  
Quest  | Dialogue   
---|---  
Commando Chick's Hideout  | These Chicks🐣 are really getting out of hand... The longer we wait, the more dangerous they become! I saw one that look _[sic]_ totally mad! It had glowing red eyes, and looked up to no good. Tried to catch it, but it was too fast. It ran away behind the vines near the Wealth Clock. We've got to catch it, but be careful. This is no ordinary Chick🐣... I think it could be armed and dangerous. Here, I'll give you a [Rage Bee Jelly] and some [Stingers] to help in the fight. _-During-_ The strange Chick🐣 is hiding behind the vines near the Wealth Clock. You'll need to equip a certain tool to cut through... I think a pair of Clippers should do the trick. You can buy them for 2200 Honey in Noob Bear's Shop. _-Completion-_ Phew, that looked intense! Thanks to you, that crazy Chick🐣 is back in a basket where it belongs. I think we just might be able to get this Chick🐣 infestation under control after all. Great job bud! Here's some rewards for your effort!   
  
![Hivesticker eviction](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D) | **This piece of content goes bye bye.** The following content has been removed from the game. The contents below may be archival, but feel free to edit below.  
---|---  
Quest  | Requirements  | Rewards   
---|---|---  
Brown Bear's Ornament  | 

  * Collect 25,000 [Pollen](/wiki/Pollen "Pollen") from the [Clover Field](/wiki/Clover_Field "Clover Field")
  * Collect 50 [Ability Tokens](/wiki/Ability_Tokens "Ability Tokens")
  * Defeat 5 [Ladybugs](/wiki/Ladybug "Ladybug")

| 30,000 [Honey](/wiki/Honey "Honey")  
5x [Ticket](/wiki/Ticket "Ticket")  
1x [Royal Jelly](/wiki/Royal_Jelly "Royal Jelly")  
[Royal Jelly Ornament](/wiki/Ornaments "Ornaments")  
Quest  | Dialogue   
---|---  
Brown Bear's Ornament  | Ho ho ho! Merry Beesmas bud! Can you believe another year has gone by already? They seem to be getting faster and faster. But the year's not complete until the Beesmas Tree is decorated! And I've got a royal idea for an [Ornament]... I'll start working on it while you finish these tasks: Collect 25,000 Pollen from the Clover Field... Collect 50 Ability Tokens... And defeat 5 Ladybugs! _-During-_ N/A _-Completion-_ That was fast! Ok then, let me just finish up. ...(Snip snip snip)... ...(Glue glue glue)... Oh... didn't quite turn out as I expected. But it'll work! It's a [Royal Jelly Ornament]! It represents the thousand of [Royal Jellies] I give out everyday! See, I even drew my face on it. With this on the Beesmas Tree, you'll receive the following boosts: +10% Capacity; x1.15 Pollen from "Bomb" Bee Abilities; And x1.25 Pollen from the Clover Field! Don't forget to keep an eye out for gift boxes hidden around the map. Once you've put enough [Ornaments] on the tree, they're yours to open! Good luck, and Happy Honeydays!   
  
![Hivesticker eviction](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D) | **This piece of content goes bye bye.** The following content has been removed from the game. The contents below may be archival, but feel free to edit below.  
---|---  
Quest  | Requirements  | Rewards   
---|---|---  
Egg Hunt: Brown Bear  | 

  * Obtain 3 [Plastic Eggs](/wiki/Plastic_Egg "Plastic Egg")

| 1,500 [Honey](/wiki/Honey "Honey")  
1x [Marshmallow Bee](/wiki/Marshmallow_Bee "Marshmallow Bee")  
3x [Micro-Converters](/wiki/Micro-Converter "Micro-Converter")  
1x [Royal Jelly](/wiki/Royal_Jelly "Royal Jelly")  
Quest  | Dialogue   
---|---  
Egg Hunt: Brown Bear  | Hey there bud! You here for the Egg Hunt? Well then, let's get right into it! When it comes to Egg Hunts, I like to keep things traditional. I've gone ahead and hidden 3 [Plastic Eggs] around the map for you to hunt down! Snoop around and check all the nooks and crannys _[sic]_. Some of them are pretty sneaky. Return all 3 to me, and I'll give you a tasty [Marshmallow Bee]. You'll need 3 of those if you want to earn Bee Swarm's Egg Hunt Egg! Got it? Great! Happy hunting. _-During-_ Having trouble? Here's a hint. All 3 of the [Plastic Eggs] are hidden right here in the starting zone! No need to search behind any of the bee gates. That should save you time. _-Completion-_ Great work! I thought I had you with the one in the maze. I'll just take those [Plastic Eggs] and reuse them next year. And in return - here's one delicious [Marshmallow Bee]! But don't eat it!! You'll need to turn in 3 for the Egg Hunt Egg.   
  
## Old Repeatable Quests[[](https://auth.fandom.com/signin?redirect=https%3A%2F%2Fbee-swarm-simulator.fandom.com%2Fwiki%2FBrown_Bear%3Fveaction%3Dedit%26section%3D8&uselang=en&metadata=article-registration-edit-article-section "Sign in to edit")]

![Hivesticker eviction](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D) | **This piece of content goes bye bye.** The following content has been removed from the game. The contents below may be archival, but feel free to edit below.  
---|---  
  
The quests required you to collect pollen from 1 field in a certain zone, with the pollen requirement changing depending on the number of bees in the player's [hive](/wiki/Hive "Hive"), and the zone the field is in. 

These quests had a 4-hour cooldown in between quests, as opposed to the current 1-hour cooldown. 

Number of bees (tier)  | Pollen requirement  | Rewards   
---|---|---  
[Sunflower Field](/wiki/Sunflower_Field "Sunflower Field"), [Dandelion Field](/wiki/Dandelion_Field "Dandelion Field"), [Clover Field](/wiki/Clover_Field "Clover Field"), [Mushroom Field](/wiki/Mushroom_Field "Mushroom Field"), [Blue Flower Field](/wiki/Blue_Flower_Field "Blue Flower Field") | [Strawberry Field](/wiki/Strawberry_Field "Strawberry Field"), [Bamboo Field](/wiki/Bamboo_Field "Bamboo Field"), [Spider Field](/wiki/Spider_Field "Spider Field"), [Pineapple Patch](/wiki/Pineapple_Patch "Pineapple Patch") | [Pumpkin Patch](/wiki/Pumpkin_Patch "Pumpkin Patch"), [Cactus Field](/wiki/Cactus_Field "Cactus Field"), [Pine Tree Forest](/wiki/Pine_Tree_Forest "Pine Tree Forest"), [Rose Field](/wiki/Rose_Field "Rose Field")  
<5 Bees (tier 1)  | 5,000 | N/A | N/A  | ![Royal Jelly](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Royal Jelly](/wiki/Royal_Jelly "Royal Jelly")  
![Ticket](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Ticket](/wiki/Ticket "Ticket")  
  
5-14 Bees (tier 2)  | 8,500 | 17,000 | N/A  | ![Royal Jelly](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Royal Jelly](/wiki/Royal_Jelly "Royal Jelly")  
![Ticket](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Ticket](/wiki/Ticket "Ticket")  
![Honey](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)10,000 [Honey](/wiki/Honey "Honey")  
![Treat](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)10 [Treats](/wiki/Treat "Treat") (20% chance)   
15-24 Bees (tier 3)  | 15,000 | 30,000 | 45,000  | ![Royal Jelly](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Royal Jelly](/wiki/Royal_Jelly "Royal Jelly")  
![Ticket](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Ticket](/wiki/Ticket "Ticket")  
![Honey](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)20,000 [Honey](/wiki/Honey "Honey")  
![Treat](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)25 [Treats](/wiki/Treat "Treat") (20% chance)  
![Magic Bean](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Magic Bean](/wiki/Magic_Bean "Magic Bean") (10% chance)   
25-29 Bees (tier 4)  | 100,000 | 200,000 | 300,000  | ![Royal Jelly](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Royal Jelly](/wiki/Royal_Jelly "Royal Jelly")  
![Ticket](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)2 [Tickets](/wiki/Ticket "Ticket")  
![Honey](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)50,000 [Honey](/wiki/Honey "Honey")  
![Treat](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)50 [Treats](/wiki/Treat "Treat") (20% chance)  
![Magic Bean](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Magic Bean](/wiki/Magic_Bean "Magic Bean") (20% chance)   
30+ Bees (tier 5)  | 250,000 | 500,000 | 750,000  | ![Royal Jelly](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Royal Jelly](/wiki/Royal_Jelly "Royal Jelly")  
![Ticket](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)2 [Tickets](/wiki/Ticket "Ticket")  
![Honey](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)200,000 [Honey](/wiki/Honey "Honey")  
![Treat](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)100 [Treats](/wiki/Treat "Treat") (20% chance)  
![Magic Bean](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Magic Bean](/wiki/Magic_Bean "Magic Bean") (20% chance)  
![Star Jelly](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)1 [Star Jelly](/wiki/Royal_Jelly#Star_Jelly "Royal Jelly") (2% chance)   
Type  | Dialogue   
---|---  
Initial (First Talk)  | Hey there! I'm Brown Bear. You ever heard of [Royal Jelly]? It's a special food that changes a bee's type! Apply it to a bee's honeycomb cell, and it'll instantly transform! The great thing is the new type will always be Rare, Epic, or Legendary. Well, I happen to have a LOT of [Royal Jelly]. Don't ask me how I got it. And if you complete my quests I'll give you some. I'll only give you 1 quest every 4 hours, though. Come talk to me again whenever you're ready for a quest!   
Quests  | Welcome back! You ready for a new quest? Complete it and I'll give you a jar of [Royal Jelly] and a [Ticket]! Check your Quest menu to see your next task. _-During-_ Looks like you haven't quite finished my quest. Check the quest menu, then collect pollen from the field I've written down. Come back when the meter is filled all the way up. _-Completion-_ Great job bud! Here's a [Royal Jelly]! Apply it to a bee's honeycomb cell and the bee will transform into a new type. In 4 hours, I'll have another quest ready for you. _-Cooldown-_ Remember, I'll only give you 1 quest every 4 hours. I need some time to prepare your next rewards!   
  
## Gallery[[](https://auth.fandom.com/signin?redirect=https%3A%2F%2Fbee-swarm-simulator.fandom.com%2Fwiki%2FBrown_Bear%3Fveaction%3Dedit%26section%3D9&uselang=en&metadata=article-registration-edit-article-section "Sign in to edit")]

[![Brown Bear.](https://static.wikia.nocookie.net/bee-swarm-simulator/images/8/85/Brown_Bear.PNG/revision/latest/scale-to-width-down/185?cb=20190203200044)![Brown Bear.](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/File:Brown_Bear.PNG "Brown Bear.PNG \(45 KB\)")

Brown Bear.

[![Brown Bear's perspective view.](https://static.wikia.nocookie.net/bee-swarm-simulator/images/6/6f/BrownBear.png/revision/latest/scale-to-width-down/272?cb=20180421054951)![Brown Bear's perspective view.](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/File:BrownBear.png "BrownBear.png \(106 KB\)")

Brown Bear's perspective view.

[![Brown Bear's beta face.](https://static.wikia.nocookie.net/bee-swarm-simulator/images/b/b7/Brownbearbeta.png/revision/latest/scale-to-width-down/185?cb=20210516010752)![Brown Bear's beta face.](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/File:Brownbearbeta.png "Brownbearbeta.png \(18 KB\)")

Brown Bear's beta face.

[![The Top Brown Bear Helpers Leaderboard.](https://static.wikia.nocookie.net/bee-swarm-simulator/images/2/21/Screen_Shot_2020-04-20_at_10.38.56_PM.png/revision/latest/scale-to-width-down/186?cb=20200421024024)![The Top Brown Bear Helpers Leaderboard.](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/File:Screen_Shot_2020-04-20_at_10.38.56_PM.png "Screen Shot 2020-04-20 at 10.38.56 PM.png \(96 KB\)")

The Top Brown Bear Helpers Leaderboard.

[![A newer version of the leaderboard.](https://static.wikia.nocookie.net/bee-swarm-simulator/images/d/d2/Brown_2.png/revision/latest?cb=20210322170051)![A newer version of the leaderboard.](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/File:Brown_2.png "Brown 2.png \(40 KB\)")

A newer version of the leaderboard.

[![A newer version of the leaderboard in 2025.](https://static.wikia.nocookie.net/bee-swarm-simulator/images/0/06/Brown_bear_leaderboard_2025.png/revision/latest/scale-to-width-down/218?cb=20250226211010)![A newer version of the leaderboard in 2025.](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/File:Brown_bear_leaderboard_2025.png "Brown bear leaderboard 2025.png \(133 KB\)")

A newer version of the leaderboard in 2025.

[![The Brown Cub skin.](https://static.wikia.nocookie.net/bee-swarm-simulator/images/9/9d/Brown_Cub.png/revision/latest?cb=20230404050339)![The Brown Cub skin.](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/File:Brown_Cub.png "Brown Cub.png \(14 KB\)")

The Brown Cub skin.

[![The Shy Brown Bear Sticker.](https://static.wikia.nocookie.net/bee-swarm-simulator/images/f/f6/Hivesticker_shy_brown_bear.png/revision/latest?cb=20240114151452)![The Shy Brown Bear Sticker.](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/File:Hivesticker_shy_brown_bear.png "Hivesticker shy brown bear.png \(15 KB\)")

The Shy Brown Bear [Sticker](/wiki/Sticker "Sticker").

## Trivia[[](https://auth.fandom.com/signin?redirect=https%3A%2F%2Fbee-swarm-simulator.fandom.com%2Fwiki%2FBrown_Bear%3Fveaction%3Dedit%26section%3D10&uselang=en&metadata=article-registration-edit-article-section "Sign in to edit")]

  * Before the [2020-04-19 Update](/wiki/Updates#2020-04-06 "Updates"), Brown Bear's quests only focused on a single [Field](/wiki/Fields "Fields") and were scaled relative to the number of bees in the player's hive.
  * Prior to the [2018-09-10 update](/wiki/Updates#2018-09-10 "Updates"), Brown Bear gave a "daily" quest every 16 hours. However, after the 2018-09-10 update, it changed to 4 hours. After the [2020-04-19](/wiki/Updates#2020-04-06 "Updates") update, he gave a quest every hour.
  * There is a ![Royal Jelly](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)[Royal Jellies](/wiki/Royal_Jelly "Royal Jelly") token on a hill behind Brown Bear. The player can reach it by having high [Jump Power](/wiki/System_Page#Jump_Power "System Page") or by using the [Parachute](/wiki/Parachute "Parachute") or [Glider](/wiki/Glider "Glider") and glide down to it from the top of the [Blue HQ](/wiki/Blue_HQ "Blue HQ") roof.
  * He is one of the three permanent [Bears](/wiki/Category:Bears "Category:Bears") that can be found in the [Starter Zone](/wiki/Starter_Zone "Starter Zone"), the others being [Black Bear](/wiki/Black_Bear "Black Bear") and [Mother Bear](/wiki/Mother_Bear "Mother Bear").
  * Brown Bear, [Polar Bear](/wiki/Polar_Bear "Polar Bear"), and Black Bear are the only three bears with infinite quests. 
    * Brown Bear is typically the first bear to start giving endless quests for new players. He is also one of the six quest givers that give repeating quests.
  * Brown Bear is the only bear that guarantees royal jelly and tickets for the completion of each quest.
  * Brown Bear uses the [Knight Animation Package](https://www.roblox.com/bundles/68/Knight-Animation-Package), the same as [Sun Bear](/wiki/Sun_Bear "Sun Bear").
  * He, Black Bear, and Mother Bear were "Nice" in 2018, as stated by [Bee Bear](/wiki/Bee_Bear "Bee Bear") during the [Beesmas 2018 Event](/wiki/Category:Beesmas "Category:Beesmas").
  * If the player gave Brown Bear a [Present](/wiki/Present "Present") during the Beesmas 2018 Event, he would give a star jelly and [Clover Field](/wiki/Clover_Field "Clover Field") [Boost](/wiki/Field_Boost "Field Boost") x4.
  * The Brown Cub rewarded for completing 300 of Brown Bear's quests is one of the six [Cub Buddy](/wiki/Cub_Buddy "Cub Buddy") skins. 
    * Lipsisas was the first player to get a Brown Cub Buddy skin.
  * The Beesmas 2020 present dialogue is a merge of Beesmas 2018 and 2019.
  * Brown Bear is the only NPC that you can give presents to that could receive the same present twice.
  * Brown Bear is the only infinite quest bear whose quests scale in difficulty.
  * Excluding event quests, Black Bear & Brown Bear are the only bears that _only_ require pollen to be collected.
  * If someone somehow gets the Brown Cub Buddy from Brown Bear without owning a Cub Buddy first, they will need to obtain the Black Cub as it only acts as "equipment" for the Cub Buddy.
  * Brown Bear is stated to have known [Spirit Bear](/wiki/Spirit_Bear "Spirit Bear") since he was a cub.
  * Brown Bear is also stated by [Spirit Bear](/wiki/Spirit_Bear "Spirit Bear") to be very reserved - meaning he does not let on much to others.
  * Brown Bear is one of the 3 Bears along with Robo Bear and Bee Bear to give out a cub buddy
  * Brown Bear visited the Wind Shrine as revealed by [Spirit Bear](/wiki/Spirit_Bear "Spirit Bear"). It is unknown what he was doing, but he was not donating.
  * Brown Bear is stated by [Black Bear](/wiki/Black_Bear "Black Bear") to spend most of his time near the [Clover Field](/wiki/Clover_Field "Clover Field"). Coincidentally, the same field that is above [King Beetle’s Lair](/wiki/King_Beetle%27s_Lair "King Beetle's Lair"). Black Bear also states that it could have something to do with his [Royal Jelly](/wiki/Royal_Jelly "Royal Jelly") stockpile.



Quest Givers   
---  
Permanent Bears  | [![Blackcloseup](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/Black_Bear "Black Bear") **[Black Bear](/wiki/Black_Bear "Black Bear")** • [![Mothercloseup](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/Mother_Bear "Mother Bear") **[Mother Bear](/wiki/Mother_Bear "Mother Bear")** • [![Browncloseup](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/Brown_Bear "Brown Bear") ****Brown Bear**** • [![Pandacloseup](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/Panda_Bear "Panda Bear") **[Panda Bear](/wiki/Panda_Bear "Panda Bear")** • [![Sciencecloseup](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/Science_Bear "Science Bear") **[Science Bear](/wiki/Science_Bear "Science Bear")** [![Dapperbearface](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/Dapper_Bear "Dapper Bear") **[Dapper Bear](/wiki/Dapper_Bear "Dapper Bear")** • [![Polarcloseup](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/Polar_Bear "Polar Bear") **[Polar Bear](/wiki/Polar_Bear "Polar Bear")** • [![RoboBearFace](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/Robo_Bear "Robo Bear") **[Robo Bear](/wiki/Robo_Bear "Robo Bear")** •[![Spiritcloseup](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/Spirit_Bear "Spirit Bear") **[Spirit Bear](/wiki/Spirit_Bear "Spirit Bear")**  
Traveling Bears  | [![Suncloseup](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/Sun_Bear "Sun Bear") **[Sun Bear](/wiki/Sun_Bear "Sun Bear")** • [![Gummycloseup](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/Gummy_Bear "Gummy Bear") **[Gummy Bear](/wiki/Gummy_Bear "Gummy Bear")** • [![Beecloseup](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/Bee_Bear "Bee Bear") **[Bee Bear](/wiki/Bee_Bear "Bee Bear")**  
Other  | [![BuckoGiftedIcon](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/Gifted_Bucko_Bee "Gifted Bucko Bee") **[Gifted Bucko Bee](/wiki/Gifted_Bucko_Bee "Gifted Bucko Bee")** • [![RileyGiftedIcon](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/Gifted_Riley_Bee "Gifted Riley Bee") **[Gifted Riley Bee](/wiki/Gifted_Riley_Bee "Gifted Riley Bee")** • [![HoneyIcon](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/Honey_Bee_\(NPC\) "Honey Bee \(NPC\)") **[Honey Bee](/wiki/Honey_Bee_\(NPC\) "Honey Bee \(NPC\)")** [![Beekeeper's Mask](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/Onett "Onett") **[Onett](/wiki/Onett "Onett")** • [![BBMThumb](data:image/gif;base64,R0lGODlhAQABAIABAAAAAP///yH5BAEAAAEALAAAAAABAAEAQAICTAEAOw%3D%3D)](/wiki/Bubble_Bee_Man "Bubble Bee Man") **[Bubble Bee Man](/wiki/Bubble_Bee_Man "Bubble Bee Man")**
