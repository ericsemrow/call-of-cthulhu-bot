# Call of Cthulhu Bot

## Invite bot to your server
1. Click or copy the following link: [https://discord.com/api/oauth2/authorize?client_id=914897470402740284&permissions=76864&scope=bot](https://discord.com/api/oauth2/authorize?client_id=914897470402740284&permissions=76864&scope=bot)
2. Select your server from the dropdown and select "Continue"
3. Agree to the pre-selected permissions
4. Click "Authorize"

## Current commands

### Skills:
#### `!skill [skill name (or portion of)]`
`-b` equals bonus die
`-p` are penalty die

CoC has a ton of skills plus write-in options. They're resolved by rolling 2 d10s and using one for the 10s slot and another for the ones. Bonus/penalty die modify the 10s slot. Normally 10 = 0 but that doesn't work well with the dice roller so we do d10-1.

Example skills include: Listen, Spot Hidden, Psychology, Persuade

Ex. `!skill drive -p 1`

TODO: Add character attibutes to this (Luck, San, Con, etc)
TODO: Using a skill should automatically check the is_used option for leveling up.


## Character Sheets

### Google Sheets
#### !gsheet [url]

**Make a copy** of this sheet (File -> Make a Copy): https://docs.google.com/spreadsheets/d/1We_wo5U5MQ9TW7PWdHN7JBovxB39WQIuNjL9JUUN_zA/edit?usp=sharing

Once you fill out the character sheet make sure its the first sheet (position it furthest to the left). Grab the public link and run `!gsheet [url]`. It must be a valid **public** (read-only is fine) url in google drive. This will transfer your character to the bot.

You can update your character by running this bot again. Doing so will overwrite all changes to your current character!

### Sheet
#### !sheet

Prints a copy of your transferred sheet to that channel.

TODO: make option to print skills as well (its long)

### san
#### !san [value]

Adds or deducts Sanity from you character. You can either deduct a set amount or use a dice string to calculate the value. 

Ex. !san -1
Ex. !san -1d3
Oops, took off too much too much
Ex. !san 1

### hp, mp, luck
#### !hp [value], !mp [value], !luck [value]

Adds or deducts from these characteristics. The value is an integer and can excede your max value listed on your sheet. So HP can be 9/9, 8/9, or even 11/9.