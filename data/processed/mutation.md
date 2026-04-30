# Mutation

**Disclaimer:** This content contains information obtained through datamining. Due to the nature of this data, details may be inaccurate or outdated. Datamined information includes the probability of obtaining specific mutations and the probability distribution of a mutation's strength based on the bee's level. (Data last updated: December 19th, 2024).

An example of a mutated bee's hive slot is shown below.

**Mutations** are a game mechanic that buffs the stats of certain bees in the player’s hive. Mutated bees display a different colored Bond number in their hive slot and on their wings compared to standard white, with the color corresponding to the stat it is mutated with. A mutated bee can become temporarily radioactive, and this radiation can spread to neighboring bees in the hive.

### Mutation Acquisition Rates

*   **Bitterberry:** Feeding a bee a Bitterberry grants a 0.1% chance of obtaining a random mutation.
*   **Jellies:** Royal Jelly and Star Jelly grant a 0.02% chance of turning a bee into a mutated bee.
*   **Atomic Treats:** Atomic Treats guarantee a mutation when fed to a bee, regardless of whether the bee is radioactive or not.

### Radioactive Bee Effects

If a bee is radioactive:

*   The chance of a mutation when using a Bitterberry increases to 1%.
*   The chance of a mutation when using Royal Jelly or Star Jelly increases to 1%.
*   Using special treats (Sunflower Seed, Strawberry, Blueberry, Pineapple, Moon Charm) grants a 0.004% chance to mutate the bee, regardless of whether the bee likes the treat.

**Note:** Using Royal Jelly or an egg on a mutated bee will almost certainly cause the mutation to be lost, similar to how gifted bees lose their gifted status.

### Mutation Display
When a mutated bee is discovered, a pop-up appears to the left of the bee displaying the gained mutation: `☢️ {Bee type} gained a mutation! (+x% [Mutation Buff]) ☢️`

## Possible Bee Bonuses

Mutations are separate from all other modifiers in the game. This means:

*   If a mutation is given as a percentage, it is multiplied directly to the bee's base stats after every other modifier has been applied.
*   If a mutation is given as a whole number, it is added to the bee's base stats before multiplicative modifiers are applied.

| Stat | Chance | Range | Color |
| :--- | :--- | :--- | :--- |
| %Convert Amount | 17.2414% | 10%-30% Increments of 1% | Orange (#feca41) |
| +Convert Amount | 8.6207% | 20-80 Increments of 1 | Orange (#feca41) |
| %Attack | 17.2414% | 5%-20% Increments of 1% | Red (#e83a36) |
| +Attack | 4.3103% | 1-2 Increments of 1 | Red (#e83a36) |
| %Gather Amount | 17.2414% | 10%-30% Increments of 1% | Light Green (#ceff80) |
| +Gather Amount | 8.6207% | 2-10 Increments of 1 | Light Green (#ceff80) |
| %Energy | 17.2414% | 10%-40% Increments of 1% | Brown (#ac8c58) |
| +Instant Conversion | 4.3103% | 8%-20% Increments of 1% | Yellow (#f3fe1e) |
| +Movespeed | 1.7241% | 2-6 Increments of 1 | Dark Cyan (#4fb8f0) |
| +Critical Chance | 1.7241% | 1%-3% Increments of 1% | Green (#47cf72) |
| %Ability Rate | 1.7241% | 1%-5% Increments of 1% | Purple (#b8a5ed) |

The highest mutation value a bee can receive depends on its level. For detailed information, see the Mutation Strength section below.

## Mutation Strength

The upper bound of a mutation increases with the level of the mutated bee, allowing it to potentially receive better mutations. Specifically, let $lvl$ be the level of the mutated bee:

1.  **Level Percentage Calculation:**
    $$\text{lvlPercentage} = \frac{lvl-1}{25-1}$$
2.  **Upper Bound Scaling:** The upper bound is scaled between the minimum and maximum upper bound of the mutation, based on $\text{lvlPercentage}$:
    $$\text{upperBound} = \text{minUpperBound} + (\text{maxUpperBound} - \text{minUpperBound}) \times \text{lvlPercentage}$$
3.  **Lower Bound:** The lower bound follows a similar process, but since the minimum and maximum lower bounds for any mutation are identical, there is no change to the lower bound.

After this scaling, the `randomBias` function is invoked with parameters: `randomBias(lowerBound, upperBound, lowerBound, 0.5)`. This generates a random value between $\text{lowerBound}$ and $\text{upperBound}$, biased towards values near $\text{lowerBound}$. This result is then rounded to the nearest interval to determine the final mutation strength.

### Mutation Bounds Table

| Stat | Lower bound | Minimum upper bound | Maximum upper bound | Interval |
| :--- | :--- | :--- | :--- | :--- |
| %Convert Amount | 10% | 15% | 30% | 1% |
| +Convert Amount | 20 | 40 | 80 | 1 |
| %Attack | 5% | 10% | 20% | 1% |
| +Attack | 1 | 1 | 2 | 1 |
| %Gather Amount | 10% | 20% | 30% | 1% |
| +Gather Amount | 2 | 6 | 10 | 1 |
| %Energy | 10% | 30% | 40% | 1% |
| +Instant Conversion | 8% | 14% | 20% | 1% |
| +Movespeed | 2 | 4 | 6 | 1 |
| +Critical Chance | 1% | 1% | 3% | 1% |
| %Ability Rate | 1% | 2% | 5% | 1% |

### Probability Tables (Level-Dependent)

The following tables show the percentage of a mutation landing within a given stat range at specific bee levels. Results are rounded to the 3rd–5th decimal digits.

**%Convert Amount Probabilities**
| Level | Stat ranges | Average |
| :---: | :---: | :---: |
| 10%-13% | 14%-17% | 18%-21% | 22%-25% | 26%-29% | 30% |
| 1 | 89.934492% | 10.065508% | - | - | - | 11.8633% |
| 2 | 83.488104% | 16.511896% | - | - | - | 12.0996% |
| 3 | 76.939671% | 23.060329% | - | - | - | 12.3344% |
| 4 | 70.558556% | 29.441444% | - | - | - | 12.5691% |
| 5 | 64.693737% | 35.306263% | - | - | - | 12.8054% |
| 6 | 59.717296% | 39.675204% | 0.6075% | - | - | 13.0398% |
| 7 | 55.451774% | 42.402628% | 2.145598% | - | - | 13.2741% |
| 8 | 51.754989% | 43.947979% | 4.297032% | - | - | 13.51% |
| 9 | 48.520303% | 44.632008% | 6.847689% | - | - | 13.7442% |
| 10 | 45.666167% | 44.683013% | 9.65082% | - | - | 13.9785% |
| 11 | 43.129158% | 44.26619% | 12.604652% | - | - | 14.2139% |
| 12 | 40.859202% | 43.502776% | 15.537232% | 0.10079% | - | 14.4483% |
| 13 | 38.816242% | 42.482833% | 18.043141% | 0.657784% | - | 14.6827% |
| 14 | 36.96785% | 41.273955% | 20.157821% | 1.600375% | - | 14.9176% |
| 15 | 35.287493% | 39.927322% | 21.948175% | 2.83701% | - | 15.1521% |
| 16 | 33.753254% | 38.48197% | 23.467744% | 4.297032% | - | 15.3865% |
| 17 | 32.346868% | 36.96785% | 24.759767% | 5.925515% | - | 15.6211% |
| 18 | 31.052994% | 35.489136% | 25.778374% | 7.673079% | 0.006417% | 15.8557% |
| 19 | 29.858648% | 34.124169% | 26.491984% | 9.308827% | 0.216373% | 16.0902% |
| 20 | 28.752772% | 32.860311% | 26.950963% | 10.753226% | 0.682728% | 16.3246% |
| 21 | 27.725887% | 31.686728% | 27.196747% | 12.031704% | 1.358934% | 16.5593% |
| 22 | 26.769822% | 30.594082% | 27.26362% | 13.165675% | 2.2068% | 16.7937% |
| 23 | 25.877495% | 29.57428% | 27.18009% | 14.173286% | 3.19485% | 17.028% |
| 24 | 25.042737% | 28.620271% | 26.969975% | 15.069985% | 4.297032% | 17.2628% |
| 25 | 24.260151% | 27.725887% | 26.653264% | 15.868996% | 5.428674% | 0.063027% | 17.4971% |

**+Convert Amount Probabilities**
| Level | Stat ranges | Average |
| :---: | :---: | :---: |
| 20-31 | 32-43 | 44-55 | 56-67 | 68-79 | 80 |
| 1 | 78.639302% | 21.360698% | - | - | - | 27.497113 |
| 2 | 73.394659% | 26.605341% | - | - | - | 28.122354 |
| 3 | 68.324508% | 31.675492% | - | - | - | 28.747609 |
| 4 | 63.769541% | 35.863035% | 0.367424% | - | - | 29.372689 |
| 5 | 59.783944% | 38.74651% | 1.469546% | - | - | 29.997769 |
| 6 | 56.267242% | 40.641505% | 3.091253% | - | - | 30.62295 |
| 7 | 53.141284% | 41.782907% | 5.07581% | - | - | 31.248075 |
| 8 | 50.344374% | 42.345362% | 7.310264% | - | - | 31.873185 |
| 9 | 47.827155% | 42.460449% | 9.712396% | - | - | 32.498309 |
| 10 | 45.549672% | 42.22844% | 12.221888% | - | - | 33.123349 |
| 11 | 43.479232% | 41.726531% | 14.691906% | 0.102331% | - | 33.74839 |
| 12 | 41.588831% | 41.01468% | 16.836194% | 0.560294% | - | 34.373487 |
| 13 | 39.855963% | 40.139823% | 18.688263% | 1.315951% | - | 34.998556 |
| 14 | 38.261724% | 39.138952% | 20.292079% | 2.307245% | - | 35.623619 |
| 15 | 36.79012% | 38.041392% | 21.683839% | 3.484649% | - | 36.248692 |
| 16 | 35.427523% | 36.870516% | 22.893551% | 4.80841% | - | 36.873716 |
| 17 | 34.162254% | 35.645024% | 23.94626% | 6.246461% | - | 37.498741 |
| 18 | 32.984245% | 34.418343% | 24.824588% | 7.742925% | 0.029899% | 38.123801 |
| 19 | 31.88477% | 33.271065% | 25.477789% | 9.112102% | 0.254274% | 38.748845 |
| 20 | 30.856229% | 32.197805% | 25.936075% | 10.341303% | 0.668588% | 39.373886 |
| 21 | 29.891972% | 31.191623% | 26.227118% | 11.446829% | 1.242458% | 39.998933 |
| 22 | 28.986155% | 30.246422% | 26.374395% | 12.442719% | 1.950309% | 40.62395 |
| 23 | 28.133621% | 29.356822% | 26.397902% | 13.341117% | 2.770538% | 41.248966 |
| 24 | 27.329803% | 28.518055% | 26.31473% | 14.152573% | 3.684838% | 41.874007 |
| 25 | 26.570642% | 27.725887% | 26.139542% | 14.886281% | 4.670685% | 0.006964% | 42.499037 |

**%Attack Probabilities**
| Level | Stat ranges | Average |
| :---: | :---: | :---: |
| 5%-7% | 8%-10% | 11%-13% | 14%-16% | 17%-19% | 20% |
| 1 | 69.314718% | 30.685282% | - | - | - | 6.8633% |
| 2 | 63.982817% | 36.017183% | - | - | - | 7.022% |
| 3 | 59.412615% | 40.25445% | 0.332934% | - | - | 7.1777% |
| 4 | 55.451774% | 43.046899% | 1.501327% | - | - | 7.3344% |
| 5 | 51.986039% | 44.755324% | 3.258638% | - | - | 7.4903% |
| 6 | 48.928036% | 45.654952% | 5.417012% | - | - | 7.6484% |
| 7 | 46.209812% | 45.946244% | 7.843944% | - | - | 7.8054% |
| 8 | 43.777717% | 45.777361% | 10.444922% | - | - | 7.9615% |
| 9 | 41.588831% | 45.259208% | 13.151961% | - | - | 8.1179% |
| 10 | 39.60841% | 44.475723% | 15.833445% | 0.082421% | - | 8.2741% |
| 11 | 37.808028% | 43.491047% | 18.158689% | 0.542236% | - | 8.4316% |
| 12 | 36.164201% | 42.354595% | 20.152248% | 1.328956% | - | 8.5879% |
| 13 | 34.657359% | 41.104711% | 21.866148% | 2.371782% | - | 8.7442% |
| 14 | 33.271065% | 39.771325% | 23.342849% | 3.614761% | - | 8.9005% |
| 15 | 31.991408% | 38.377916% | 24.617271% | 5.013405% | - | 9.0569% |
| 16 | 30.806541% | 36.96785% | 25.693462% | 6.532147% | - | 9.2139% |
| 17 | 29.706308% | 35.647569% | 26.503695% | 8.121922% | 0.020506% | 9.3701% |
| 18 | 28.681952% | 34.418343% | 27.078484% | 9.584322% | 0.236899% | 9.5265% |
| 19 | 27.725887% | 33.271065% | 27.453146% | 10.892119% | 0.657784% | 9.6827% |
| 20 | 26.831504% | 32.197805% | 27.657317% | 12.0639% | 1.249474% | 9.8392% |
| 21 | 25.993019% | 31.191623% | 27.715985% | 13.115595% | 1.983778% | 9.9959% |
| 22 | 25.205352% | 30.246422% | 27.6503% | 14.060916% | 2.83701% | 10.1521% |
| 23 | 24.464018% | 29.356822% | 27.478235% | 14.91172% | 3.789205% | 10.3084% |
| 24 | 23.765046% | 28.518055% | 27.215118% | 15.678301% | 4.820207% | 0.003272% | 10.4646% |
| 25 | 23.104906% | 27.725887% | 26.874064% | 16.369628% | 5.813148% | 0.112367% | 10.6211% |

**+Critical Chance Probabilities**
| Level | Stat ranges | Average |
| :---: | :---: | :---: |
| 1% | 2% | 3% | - | 1% |
| 1 | 100% | - | 1 | 1% |
| 2 | 100% | - | 1 | 1% |
| 3 | 100% | - | 1 | 1% |
| 4 | 100% | - | 1 | 1% |
| 5 | 100% | - | 1 | 1% |
| 6 | 100% | - | 1 | 1% |
| 7 | 100% | - | 1 | 1% |
| 8 | 97.854402% | 2.145598% | - | 1.0215% |
| 9 | 93.152311% | 6.847689% | - | 1.0685% |
| 10 | 87.395348% | 12.604652% | - | 1.126% |
| 11 | 81.299075% | 18.700925% | - | 1.187% |
| 12 | 75.214815% | 24.785185% | - | 1.2479% |
| 13 | 69.314718% | 30.685282% | - | 1.3069% |
| 14 | 63.982817% | 36.017183% | - | 1.3602% |
| 15 | 59.412615% | 40.587385% | - | 1.4059% |
| 16 | 55.451774% | 44.548226% | - | 1.4455% |
| 17 | 51.986039% | 48.013961% | - | 1.4801% |
| 18 | 48.928036% | 51.071964% | - | 1.5107% |
| 19 | 46.209812% | 53.790188% | - | 1.5379% |
| 20 | 43.777717% | 55.940283% | 0.282% | 1.565% |
| 21 | 41.588831% | 57.376062% | 1.035107% | 1.5945% |
| 22 | 39.60841% | 58.245992% | 2.145598% | 1.6254% |
| 23 | 37.808028% | 58.665358% | 3.526613% | 1.6572% |
| 24 | 36.164201% | 58.724532% | 5.111267% | 1.6895% |
| 25 | 34.657359% | 58.494952% | 6.847689% | 1.7219% |

**%Ability Rate Probabilities**
| Level | Stat ranges | Average |
| :---: | :---: | :---: |
| 1% | 2% | 3% | 4% | 5% |
| 1 | 69.314718% | 30.685282% | - | - | - | 1.3069% |
| 2 | 61.613083% | 38.386917% | - | - | - | 1.3839% |
| 3 | 55.451774% | 44.548226% | - | - | - | 1.4455% |
| 4 | 50.410704% | 49.589296% | - | - | - | 1.4959% |
| 5 | 46.209812% | 53.790188% | - | - | - | 1.5379% |
| 6 | 42.655211% | 56.737289% | 0.6075% | - | - | 1.5795% |
| 7 | 39.60841% | 58.245992% | 2.145598% | - | - | 1.6254% |
| 8 | 36.96785% | 58.735119% | 4.297032% | - | - | 1.6733% |
| 9 | 34.657359% | 58.494952% | 6.847689% | - | - | 1.7219% |
| 10 | 32.618691% | 57.73049% | 9.65082% | - | - | 1.7703% |
| 11 | 30.806541% | 56.588806% | 12.604652% | - | - | 1.818% |
| 12 | 29.185144% | 55.176834% | 15.638022% | - | - | 1.8645% |
| 13 | 27.725887% | 53.573188% | 18.700925% | - | - | 1.9098% |
| 14 | 26.405607% | 51.836197% | 21.527751% | 0.230445% | - | 1.9558% |
| 15 | 25.205352% | 50.009463% | 23.93249% | 0.852695% | - | 2.0043% |
| 16 | 24.109467% | 48.125757% | 25.984244% | 1.780532% | - | 2.0544% |
| 17 | 23.104906% | 46.209812% | 27.738875% | 2.946407% | - | 2.1053% |
| 18 | 22.18071% | 44.36142% | 29.160839% | 4.297032% | - | 2.1557% |
| 19 | 21.327606% | 42.655211% | 30.22707% | 5.790113% | - | 2.2048% |
| 20 | 20.537694% | 41.075388% | 30.995005% | 7.391912% | - | 2.2524% |
| 21 | 19.804205% | 39.60841% | 31.51199% | 9.075395% | - | 2.2986% |
| 22 | 19.121302% | 38.242603% | 31.817276% | 10.698523% | 0.120297% | 2.3445% |
| 23 | 18.483925% | 36.96785% | 31.943573% | 12.149988% | 0.454664% | 2.3912% |
| 24 | 17.887669% | 35.775338% | 31.918274% | 13.450431% | 0.968287% | 2.4384% |
| 25 | 17.32868% | 34.657359% | 31.764415% | 14.61754% | 1.632006% | 2.4857% |

## Gallery
A collection of images illustrating various mutation types and effects:

*   [Bee Ability Rate mutation image](https://static.wikia.nocookie.net/bee-swarm-simulator/images/1/1f/0F9CB735-3DAA-4276-BF59-A2D19DA0B462.jpeg)
*   [Attack mutation image](https://static.wikia.nocookie.net/bee-swarm-simulator/images/8/85/5144FBB3-82C1-498E-A915-B13753EB3FDB.jpeg)
*   [Gather Amount mutation image](https://static.wikia.nocookie.net/bee-swarm-simulator/images/b/b0/BA3321E5-BF64-4C6E-9889-13901642009E.jpeg)
*   [Convert Amount mutation image](https://static.wikia.nocookie.net/bee-swarm-simulator/images/d/de/222F5FD9-DFC9-425A-B18A-013669335A6D.jpeg)
*   [Energy mutation image](https://static.wikia.nocookie.net/bee-swarm-simulator/images/b/b2/Do_i_cry.png/revision/latest/scale-to-width-down/185?cb=20191229185516)
*   [Instant Conversion mutation image](https://static.wikia.nocookie.net/bee-swarm-simulator/images/4/4c/IC_mutation.png/revision/latest/scale-to-width-down/185?cb=20240525115144)
*   [Critical Chance mutation image](https://static.wikia.nocookie.net/bee-swarm-simulator/images/2/21/Crit_Mutation.png/revision/latest/scale-to-width-down/185?cb=20240607053004)
*   [Movespeed mutation image](https://static.wikia.nocookie.net/bee-swarm-simulator/images/8/8f/Photon_movespeed.png/revision/latest/scale-to-width-down/185?cb=20250310130854)
*   [Radiation spread image](https://static.wikia.nocookie.net/bee-swarm-simulator/images/f/f6/Radiation.png/revision/latest/scale-to-width-down/185?cb=20200504013204)
*   [Bee mutation message image](https://static.wikia.nocookie.net/bee-swarm-simulator/images/1/15/F4F86DE8-FC17-45FE-A10D-85B594D3F201.jpeg/revision/latest/scale-to-width-down/185?cb=20200111171958)
*   [Radioactive bee with Attack mutation image](https://static.wikia.nocookie.net/bee-swarm-simulator/images/d/db/MutatedRadiation_GiftedViciousBee.png/revision/latest/scale-to-width-down/185?cb=20191225095504)
*   [Radioactive bee with Convert Amount mutation image](https://static.wikia.nocookie.net/bee-swarm-simulator/images/f/fc/Mutate1.png/revision/latest/scale-to-width-down/185?cb=20210929055617)
*   [Radioactive bee with Energy mutation image](https://static.wikia.nocookie.net/bee-swarm-simulator/images/4/49/EnergyMutation.png/revision/latest/scale-to-width-down/185?cb=20230515225324)
*   [Spicy Bee getting a mutation from treats image](https://static.wikia.nocookie.net/bee-swarm-simulator/images/a/a1/SpicyBeeTreatMutation.png/revision/latest/scale-to-width-down/185?cb=20230908133527)
*   [Precise Bee with a Gather Amount Mutation image](https://static.wikia.nocookie.net/bee-swarm-simulator/images/8/8c/PreciseGather.png/revision/latest/scale-to-width-down/185?cb=20240611213205)
*   [Wrong radiation emoji image](https://static.wikia.nocookie.net/bee-swarm-simulator/images/6/64/Wrong_radioactivity_emoji.png/revision/latest/scale-to-width-down/121?cb=20241014015032)

## Trivia
*   It is possible to obtain mutations that are almost entirely useless to certain bees:
    *   An Attack Mutation on a Baby Bee, since it cannot attack. However, the mutation still adds to the player's total attack, which can buff Star Saw.
    *   A Bee Ability Rate mutation on an ungifted Basic Bee or Brave Bee that does not have a Beequip adding an ability, as both bees lack abilities.
    *   An Energy mutation on a Photon Bee or Exhausted Bee, as both bees possess infinite energy. However, this still increases the amount of nectar they can sip from a Planter.
*   The Beesmas Tree Hat Beequip requires a bee to have a mutation to be equipped, making any mutation potentially useful for any bee.
*   The Bubble Light Beequip requires a bee to have an Energy mutation to be equipped.
*   When mutating a bee, any currently equipped Beequip is automatically unequipped and must be re-equipped by the player if they wish to continue using it.
*   Depending on the game's language, the radiation emoji may change.