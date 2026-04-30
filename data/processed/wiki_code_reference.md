# Wiki Code Reference Guide

This document serves as a comprehensive guide to wikitext syntax, formatting codes, and template usage within the Bee Swarm Simulator Wiki. It is intended for users with basic knowledge of wikis who wish to contribute or edit content effectively.

## Sample Wikitext Usage

The following example demonstrates how various elements—such as lists, internal links, bolding, and references—are used in a typical wiki article (taken from the Basic Bee page trivia section).

==Trivia==
* This is one of the only bees without an ability (the other being Brave Bee).
* This is the only bee that cannot be obtained from [[Royal Jelly]].
** Note: There was previously a "Basic Bee Jelly" obtainable via the expired code `DontUseThisJelly`.
* This is likely the first bee players discover.
* Basic Bee and [[Demo Bee]] share the same skin colors.
* Basic Bee is the only bee that can be obtained solely from a [[Basic Egg]].
* Basic Bee is categorized as a common bee.
* It is the most common colorless bee in the game.

{{BeeNav}}


### Note on Usage
This guide covers fundamental wikitext elements, including basic formatting, linking, tables, and templates.

## Formatting Codes

Basic formatting codes allow you to add structure and visual enhancements beyond plain text within a paragraph.

### Paragraphs and Indentation
*   **New Paragraph:** Simply leave an empty line between blocks of text. Removing this line will merge the paragraphs.
*   **Spacing:** Using two or more empty lines increases the vertical space between paragraphs.
*   **Indentation/Block Quotes:** A colon (`:`) at the start of a line creates an indented block paragraph.

### Lists
*   **Bullet Points:** Use an asterisk (`*`) at the beginning of a line (with no preceding space) to create a bulleted list.
    ```markdown
    * Bullet point one
    * Bullet point two
    ```
*   **Numbered Lists:** Use a hash/pound sign (`#`) for numbered lists.
    ```markdown
    # Item 1
    # Item 2
    ```
    *(Note: The wiki software may automatically convert this to standard numbering.)*

*   **Nesting and Combining Codes:** You can combine paragraph code, list code, and indentation:
    ```markdown
    * Main Title
        * Sub-title
    1. Primary Item
        1. Sub-item A
        2. Sub-item B
    ```

### Italics & Boldface
| Code | Result | Description |
| :--- | :--- | :--- |
| `''italics''` | *italics* | Single quotes for italics. |
| `'''bold'''` | **bold** | Triple single quotes for bold text. |
| `'''''bold and italicized'''''` | ***bold and italicized*** | Combining both styles. |

### Headings
Headings organize content and automatically generate a table of contents, aiding user navigation.

*   Normal Text (No heading)
*   `==Heading 2==` (Level 2 Heading)
*   `===Heading 3===` (Level 3 Heading)
*   `====Heading 4====` (Level 4 Heading)
*   `=====Heading 5=====` (Level 5 Heading)

The `<pre>` tag can also be used to display text in a preformatted block, preserving whitespace and line breaks exactly as typed.

### Links
#### Internal Links
Internal links direct users to other pages within the wiki. They use double square brackets (`[[Page Name]]`). The name inside the brackets must match the page title (case-sensitive).

*   **Basic Link:** `[[Basic Bee]]` results in: [Basic Bee](/wiki/Basic_Bee "Basic Bee")
*   **Custom Display Text:** You can change how the link appears using a pipe (`|`).
    `[[Basic Bee|Common Bee]]` results in: [Common Bee](/wiki/Basic_Bee "Basic Bee")

#### External Links (URLs)
External links require single square brackets (`[]`) for the URL, and often need additional syntax to display readable text.

*   **Simple Link:** `[https://www.roblox.com]` results in a numbered citation link: [[1]](https://www.roblox.com).
*   **Link with Display Name:** To provide a friendly name instead of the URL, add a space after the URL.
    `[https://www.roblox.com ROBLOX]` results in: [ROBLOX](https://www.roblox.com).

#### Wikipedia Links
To link directly to an external resource while maintaining wiki formatting (like citation tracking), use the `Wikipedia:` prefix within double brackets.
`[[Wikipedia:Bee]]` results in: [Wikipedia:Bee](https://en.wikipedia.org/wiki/Bee "wikipedia:Bee")

### Reference Code
This code gathers data from another page and displays citations.

*   **Adding a Citation:** `<ref>[[Basic Bee]] Basic Bee </ref>` adds the citation entry to the end of the article.
*   **Displaying Citations:** `<references />` generates the numbered list of all references used on the page (e.g., `1. ↑ [Basic Bee](/wiki/Basic_Bee "Basic Bee") Basic Bee`).

## Tables

Tables are used to organize and summarize large amounts of data efficiently.

The basic structure uses the following syntax:
```markdown
{| class="wikitable"
|-
! Header 1
! Header 2
! Header 3
|-
| Row 1, Cell 1
| Row 1, Cell 2
| Row 1, Cell 3
|-
| Row 2, Cell 1
| Row 2, Cell 2
| Row 2, Cell 3
|}
```

**Code Definitions:**
*   `{|` and `|}`: Start and end the table structure.
*   `|-`: Marks the beginning of a new row (a horizontal set of cells).
*   `!`: Marks the beginning of a header cell (titles).
*   `|`: Used at the start of a line to mark the beginning of a standard data cell. It can also be used within a cell for formatting, e.g., `| align="center" | centered contents`.

## Templates

Templates are reusable documents that ensure consistency across the wiki. They use curly brackets (`{{...}}`) to indicate where content should be inserted based on specific conditions (parameters).

### Tabbers
Wikia's "Tabber" extension allows for organized, tabbed content presentation.

#### Content Tabbers
These tabs require information to be written directly within the page structure and use section headers as navigation links.
```markdown
<tabber>
Colors=
Red, Blue, Colorless
|-|
Hats=
Helmet, Propeller Hat, Beekeeper's Mask
</tabber>
```
*Output:* Displays "Colors" and "Hats" as clickable sections containing the listed content.

#### Tab Viewers
Tab Viewers link to external pages, requiring less space in the current article. They consist of three parts: [Page Link] | Name Projected ||
```markdown
<tabview>
Scooper|Page 1||
Pouch|Page 2||
Backpack|Page 3||
</tabview>
```
*Output:* Displays external links like `[ Page 1 ](https://bee-swarm-simulator.fandom.com/wiki/Scooper)`.

### Specific Templates
*   **Bee Template:** `{{Template:Bee}}` (Used for bee overviews).
*   **Bear Template:** `{{Template:Bear}}` (Used for bear overviews).

#### Bear Template Parameters
The Bear Template provides a detailed overview of a bear, including location and color schemes. **All parameters are case sensitive.**

| Parameter | Accepted Inputs | Description |
| :--- | :--- | :--- |
| `image` | image file | Shows the profile image of the bear. |
| `type` | Quest Bear, Traveling Bear, Shop Bear | Defines the type of bear in the game. |
| `location` | game asset | Specifies the nearest location where the bear is found. |
| `bees` | number, None | Indicates how many bees are required to reach the bear (if gated). |
| `basecoloramount` | 1 or 2 | Counts the number of colors used for the base fur color. |
| `basecolor1` | color code | The first base fur color of the bear. |
| `basecolor2` | color code | The second base fur color (optional). |
| `shadecoloramount` | 1 or 2 | Counts the number of colors used for the shade fur color. |
| `shadecolor1` | color code | The first fur shade color of the bear. |
| `shadecolor2` | color code | The second fur shade color (optional). |
| `snoutcoloramount` | 1 or 2 | Counts the number of colors for the snout bridge part. |
| `snoutcolor1` | color code | The first snout color of the bear. |
| `snoutcolor2` | color code | The second snout color (optional). |
| `torsocoloramount` | 1 or 2 | Counts the number of colors for the torso. |
| `torsocolor1` | color code | The first torso color of the bear. |
| `torsocolor2` | color code | The second torso color (optional). |
| `armscolor` | color code | The color of the bear's arms. |
| `legscolor` | color code | The color of the bear's legs. |
| `enableother` | boolean | Enables or disables an additional color box for items (e.g., hats, glasses). |
| `othername` | text | Displays the name for the additional color box. |
| `othercoloramount` | 1 or 2 | Counts the number of "other" colors on the bear. |
| `othercolor1` | color code | The first "other" color (e.g., hat color). |
| `othercolor2` | color code | The second "other" color (optional). |

### Notice Templates
These templates are used to provide notices above page content and do not require specific parameters.

*   **Stub:** `{{Stub}}` - Used when a section of the page is incomplete or pending addition.
*   **Removed Content:** `{{RemovedContent}}` - Indicates that the subject page has been permanently removed from the game.
*   **Delete Warning:** `{{Delete}}` - Marks a warning that the page is about to be deleted.

### Navigation Templates (Navboxes)
These templates generate lists of related pages, typically located at the bottom of an article.

*   **BeeNav:** `{{BeeNav}}` - Lists all Bee-related pages and images.
*   **BearNav:** `{{BearNav}}` - Lists all Bear-related pages.
*   **MapNav:** `{{MapNav}}` - Lists all locations within the game.
*   **CurrencyNav:** `{{CurrencyNav}}` - Lists in-game currencies.
*   **Items:** `{{Items}}` - Lists all in-game items.

## List of Terms
| Term | Definition |
| :--- | :--- |
| Game Assets | Objects present within the game environment (e.g., fields, shops, cannons). |
| Color Code | A system used to represent computer display color (e.g., Hex `#000000`, RGB `rgb(0,0,0)`, HSL `hsl(0,0,0)`). |
| Boolean | A value that identifies a state as either yes or no, often represented by its initials (`y` or `n`). |