# FAQ/Wiki Code

  
  
  
<!--Codes-->

This document is intended to be a Quick Tutorial. Please amend this description to reflect purpose of this document. 

## Sample Code

See the following example, taken from the [Basic Bee](/wiki/Basic_Bee "Basic Bee") page's trivia section. (31 May 2018) 
    
    
    ==Trivia==
    * This is one of the only bees without an ability (the other one being Brave Bee).
    * This is the only bee that can't be obtained from [[Royal Jelly]].
    ** However, there used to be Basic Bee Jelly obtained by from a code called DontUseThisJelly.
    ** This code has expired, so you can't obtain Basic Bee Jelly anymore.
    ** This is most likely the first bee the player will get and discover.
    *Basic Bee and [[Demo Bee]] have the same skin colors.
    *Basic Bee is the only bee that can be obtained from only a [[Basic Egg]].
    *Basic Bee is the only common bee.
    *Basic Bee is the most common colorless bee in the game.
    {{BeeNav}}
    

We will be referring to this code segment in this document. 

  


### Note on Code Segment

This guide was originally written for mid-level players or that has a basic knowledge of wikitext. 

  


## Preface

Most of the codes are of a basic format. Either double "{" and closed with double "}" (curly brackets) or double "[" closed with double "]" (square brackets) or single straight quotes " ' ". Some codes from HTML 5 do support Wikia. such as **< center>**. 

## Basic Formatting Codes

Basic formatting codes are simple instructions that tell the wiki you want more than plain text in a single paragraph. =D 

  


### Paragraphs

The extra line between paragraphs creates a new paragraph. If the line is removed, the two paragraphs will join. _Two empty lines_ between paragraphs increases the space between paragraphs. 

A colon ":" means indent, like so: 

    Indent / block paragraph.

  


### Lists

The asterisk "*" at the beginning of a line (no space in front) means the wiki should insert a bullet like this: 

  * bullet



  
A "#" (hash/pound) sign means a numbered list, like so: 
    
    
    # Item 1
    # Item 2
    

  1. Item 1
  2. Item 2



  
You can combine paragraph code and list code thus: 
    
    
    ::* Sub level
    :::# Item 1, Sub 1
    

    

    

  * Sub level



    

  1. Item 1, Sub 1



or you can add indent by adding more list code: 
    
    
    * Title
    **Sub-title
    

  * Title 
    * Sub-title


    
    
    #Media
    ##Photo
    ##Video
    

  1. Media 
     1. Photo
     2. Video



Inserting a space (by pressing enter) before the start of your text is recommended and improves readability in the source code. 

### Italics & Boldface
    
    
    ''italics''

gives _italics_. 

  

    
    
    '''bold'''

gives **bold**. 

  

    
    
    '''''bold and italicized'''''

gives _**bold and italicized**_. 

### Heading

This code shows a main part of the topic such as a bee's history and trivia. Using this code creates a table of contents, which helps users to navigate throughout the page. 
    
    
    Normal text
    
    ==Heading 2==
    
    ===Heading 3===
    
    ====Heading 4====
    
    =====Heading 5=====
    
     preformatted 

The code `<pre>` can also preformat the text. 

### Links
    
    
    [[Basic Bee]]

gives [Basic Bee](/wiki/Basic_Bee "Basic Bee"). The square brackets mean you are trying to link to a page on the wiki (known as internal links). "Basic Bee" is the name of the page. 

Note: If it didn't work as you expected, check your spelling and the capitalization. 

You can also change the name of the link. But it will lead you to the same page: 
    
    
    [[Basic Bee|Common Bee]]

gives [Common Bee](/wiki/Basic_Bee "Basic Bee"). 

In order to add URLs (external links), single square brackets are required instead of two. 
    
    
    [https://www.roblox.com]

gives [[1]](https://www.roblox.com). 

As you can see that it gives out number instead of the actual link. In order to solve this, you need add a name of the link. But instead of using a pipe "|" to separate it, adding a space is at least required. 
    
    
    [https://www.roblox.com ROBLOX]

gives [ROBLOX](https://www.roblox.com). 

And one step closer if you want to add a Wikipedia Link: 
    
    
    [[Wikipedia:Bee]]

gives [Wikipedia:Bee](https://en.wikipedia.org/wiki/Bee "wikipedia:Bee")

These are the basics. As you edit other work, you will learn more from other people's "codes". 

### Reference Code

This code's purpose is to show what data is gathered from another external page. 
    
    
    <ref>[[Basic Bee]] Basic Bee </ref>
    

gives 

[1]

and to show all summary of reference quotes: 
    
    
    <references />
    

gives 

  1. ↑ [Basic Bee](/wiki/Basic_Bee "Basic Bee") Basic Bee 



  
NOTE: These two codes must be performed or else an error will occur. 

  


## Tables

Sometimes we use Tables to organize and summarize data, particularly when there is large amounts of it -- e.g., for Stick Bug hp. 

Code segment for Tables follow: 
    
    
    
     {| class="wikitable"
     |-
     ! Header 1
     ! Header 2
     ! Header 3
     |-
     | row 1, cell 1
     | row 1, cell 2
     | row 1, cell 3
     |-
     | row 2, cell 1
     | row 2, cell 2
     | row 2, cell 3
     |}
    
    

The preceding code produces: 

Header 1  | Header 2  | Header 3   
---|---|---  
row 1, cell 1  | row 1, cell 2  | row 1, cell 3   
row 2, cell 1  | row 2, cell 2  | row 2, cell 3   
  
### Code Definitions

**{|** and **|}** start and end tables respectively. 

**|-** marks the beginning of a new row (a set of cells arranged in a horizontal manner.) 

**!** marks the beginning of a new header cell (for titles - please do not use this as a lazy way to bold the contents of a cell)... Header cells may be assigned special functions, e.g., for sorting. 

**|** _at the beginning of a line_ is used to mark the beginning of a new cell. When this symbol is used _elsewhere_ , it may be used to separate the cell formatting from its contents. E.g., 
    
    
    | align="center" | centered contents

  
[Wikipedia's Help:Table](http://en.wikipedia.org/wiki/Help:Table) is a more complete in detail and includes advanced code &/ options if you need it. 

## Templates

Templates are documents written by (advanced) coders to allow Bee Swarm Simulator Wiki to have a consistent look throughout. The curly brackets really mean "insert this document here, with the following conditions." 

### Tabbers

Wikia has an extension called _"Tabber"_. They give content and title on every tab; the purpose is to make the wiki more organized and more designed. 

#### Content Tabbers

Content Tabbers are type of tabbers that require to write information inside the same page. The Content Tabber uses section headers as pseudo-links to open and navigate through the tabs. 
    
    
    <tabber>
    Colors=
    Red, Blue, Colorless
    |-|
    Hats=
    Helmet, Propeller Hat, Beekeeper's Mask
    </tabber>
    

gives 

  * Colors

  * Hats




Red, Blue, Colorless

Helmet, Propeller Hat, Beekeeper's Mask

#### Tab Viewers

Unlike Content Tabbers, Tab Viewers just view the page contents. They require less space to configure the tabber. In order to edit the content, you need to edit it to the page where it projects it. 
    
    
    <tabview>
    Scooper|Page 1||
    Pouch|Page 2||
    Backpack|Page 3||
    </tabview>

gives 

  * [ Page 1 ](https://bee-swarm-simulator.fandom.com/wiki/Scooper)
  * [ Page 2 ](https://bee-swarm-simulator.fandom.com/wiki/Pouch)
  * [ Page 3 ](https://bee-swarm-simulator.fandom.com/wiki/Backpack)



* * *

There are three parts of the tab viewer: 

  * The actual link of the page,
  * Name projected and,
  * The pipe.



The pipe separates the text. Add a pipe "|" to separate the link and the name, while two pipes "||" to separate the tabs. 

Like for example, if something is wrong about Page 2, you need to go to Tab View 2 page. 

### Template _"Bee"_

_Main Page:_[Template:Bee](/wiki/Template:Bee "Template:Bee")

### Template _"Bear"_

_Main Page:_[Template:Bear](/wiki/Template:Bear "Template:Bear")

## Purpose

Bear Template gives a simple overview information of the bear. That includes the proximate location, bees required and their color schemes. Remember, the parameters are **case sensitive**. 

## List of Terms

Terms  | Definition   
---|---  
Game Assets  | Things that are in the game. Such as fields, cannons, shops, etc.   
Color Code  | A system that makes computer display color. The coding can be hex [#000000], red-green-blue [rgb(000,000,000)], or hue-saturation-luminosity [hsl(000,000,000)]   
Boolean  | identifies by yes or no. It can be their initials (y or n)   
  
## Usage

Parameter  | Accepted Inputs  | Description   
---|---|---  
image  | image file  | shows image profile of a bear.   
type  | Quest Bear, Traveling Bear, Shop Bear  | shows what type of bear is on the game.   
location  | game asset  | shows the nearest place where the bear is located.   
bees  | number, None  | Due to some gates, it shows how many bees are required to go to the bear.   
basecoloramount  | 1 or 2  | counts the colors of the fur color.   
basecolor1  | color code  | first base fur color of the bear.   
basecolor2  | color code  | second base fur color of the bear. Inputting code is not required if the bear has one base color.   
shadecoloramount  | 1 or 2  | counts the colors of the fur color.   
shadecolor1  | color code  | first fur shade color of the bear.   
shadecolor2  | color code  | second fur shade color of the bear. Inputting code is not required if the bear has one shade color.   
snoutcoloramount  | 1 or 2  | counts the colors of the stout color (the nose bridge part of the bear).   
snoutcolor1  | color code  | first snout color of the bear.   
snoutcolor2  | color code  | second snout color of the bear. Inputting code is not required if the bear has one snout color.   
torsocoloramount  | 1 or 2  | counts the colors of the torso color.   
torsocolor1  | color code  | first torso color of the bear.   
torsocolor2  | color code  | second torso color of the bear. Inputting code is not required if the bear has one torso color.   
armscolor  | color code  | arms color of the bear.   
legscolor  | color code  | legs color of the bear.   
enableother  | boolean  | enables or disables additional color box. This is for bears that are wearing any item. Like hats or glasses.   
othername  | text  | displays the name for additional color box.   
othercoloramount  | 1 or 2  | counts the "other" colors of the bear.   
othercolor1  | color code  | first torso color of the bear.   
othercolor2  | color code  | second torso color of the bear. Inputting code is not required if the bear has one torso color.   
  
### Notice Templates

Templates are used for giving notices above the page content. These templates do not require to fill-up information. 

  * Template Stub



    Stubs are used when a section of the page is partially finished or not yet added.
    
    
    {{Stub}}
    

  * Template RemovedContent



    The following page is permanently removed in the game.
    
    
    {{RemovedContent}}
    

  * Template Delete



    This template's purpose is to mark a **warning** or a notice that the page is about to be deleted. Simply put the code
    
    
    {{Delete}}

to use the template. 

### Navigation Templates

Templates are used for giving list of pages that are related to the visited page. Navboxes are usually located at the bottom of the article page. 

  * BeeNav



    All Bee pages and their images are listed here.
    
    
    {{BeeNav}}
    

  * BearNav



    All Bear pages are listed here.
    
    
    {{BearNav}}
    

  * MapNav



    All locations of the game and their pages are listed here.
    
    
    {{MapNav}}
    

  * CurrencyNav



    In-game currencies are listed here.
    
    
    {{CurrencyNav}}
    

  * Items



    All In-game items are listed here.
    
    
    {{Items}}
    
