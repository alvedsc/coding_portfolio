# Coding Portfolio

I created this Repo to showcase my GIS data analyst coding skills, as well as other coding samples for that I deem relevant enough to showcase. 

## Index

- R
  - Polyline statistics from raster
- Python
  - Geonames data compilator
- Javascript
  - Obsidian
    - Highlight of the day
    - Day planner

## Javascript

Here's a list of my Javascript coding samples

### Obsidian

Here's a list of my js coding samples for the purpose of improving my personal experience of the Obsidian app

#### Highlight of the day

Purpose: The [Kindle Highlights plug-in](https://github.com/hadynz/obsidian-kindle-plugin) retrieves all highlights from a given Amazon account and stores them into a file in a given Obsidian Vault. The *Highlight of the day* script, extracts a random highlight from a random book and places it the daily note. The note's title (a date in the format YYYY-MM-DD) is used as a seed to ensure the random highlight stays constant throughout the day, regardless of refreshing or the device being used. A sine function is used since Obsidian does not allow the use of the "random-seed" Javascript library.

Access [the Highlight of the Day script by clicking here](https://github.com/alvedsc/coding_portfolio/blob/main/codes/highlight_of_the_day.js)

#### Day Planner

Purpose: This script retrieves all tasks from all notes in the Obsidian Vault and organize them by their completion date, for every new daily note. Using this script, all daily notes will have a Day Planner section with tasks: 1. Overdue, 2. Today, 3. Upcoming, 4. Undated. It will also add the the "Today" list any tasks that have the #habit or #habit/weekly tags in the current note, or the weekly note. It will also add a link to the note where the task was originally written. This way, each task can easily be edited or marked as Complete using the Obsidian's [Hover Editor plug-in](https://github.com/nothingislost/obsidian-hover-editor)

Access [the Day Planner script by clicking here](https://github.com/alvedsc/coding_portfolio/blob/main/codes/day_planner.js)
