# Coding Portfolio

Hi, I'm Alvaro! As a GIS professional and Data Scientist, my team becomes much faster and more efficient when I automate repetitive tasks. In this repo, you will find some of the scripts that I used to automate tasks in GIS, Data Analysis, and other knowledge areas. 
I hold a Bachelor Degree in Agricultural Engineering and a Master of Science (M.S.) in Organizational Leadership with a concentration in Project Management. I have 9 years of experience in the field of geoscience, where I held roles such as GIS Analyst, Research Associate, Professor, Lecturer, Data Analyst, among others. 

I created this Repo to showcase my GIS data analyst coding skills, as well as other coding samples for that I deem relevant enough to showcase. 

## Index

- [Python](#python)
  - [GIS](#gis)
    - [Geonames data compilator](#geonames-data-compilator)
    - [Polyline statistics from raster](#polyline-statistics-from-raster)
- [Javascript](#javascript)
  - [Obsidian](#obsidian)
    - [Highlight of the day](#highlight-of-the-day)
    - [Day planner](#day-planner)
    
## Python

Here's a list of my .py scripts

### GIS

Here's a list of coding samples to assist my GIS practice 

#### Polyline statistics from raster

Purpose: The following code takes an indefinite number of rasters and multiplies them. These rasters correspond to probability distributions (Numbers between 0 and 1). It also takes a line shapefile. This corresponds to a route of a vehicle or person throughout the area delimited by the rasters. It graphs the values of the raster throughout the line. This is relevant to determine which parts of a route are more dangerous than others, if the probability rasters correspond to individual probabilities of a negative event to occur, like homicide probability or drug dealing probability.

Access the [Polyline statistics from raster script by clicking here](https://github.com/alvedsc/coding_portfolio/blob/main/codes/line_graph.py)

#### Geonames data compilator

Purpose: This script downloads all data from the [GeoNames data dump](http://download.geonames.org/export/dump/), extracts the information, converts 
it into the shapefile format and stores it in different folders corresponding to each country in the data dump. 

Access the [Geonames data compilator script by clicking here](https://github.com/alvedsc/coding_portfolio/blob/main/codes/geonames_compilator.py)

## Javascript

Here's a list of my Javascript coding samples

### Obsidian

Here's a list of my .js coding samples for the purpose of improving my personal experience of the Obsidian app

#### Highlight of the day

Purpose: The [Kindle Highlights plug-in](https://github.com/hadynz/obsidian-kindle-plugin) retrieves all highlights from a given Amazon account and stores them into a file in a given Obsidian Vault. The *Highlight of the day* script, extracts a random highlight from a random book and places it the daily note. The note's title (a date in the format YYYY-MM-DD) is used as a seed to ensure the random highlight stays constant throughout the day, regardless of refreshing or the device being used. A sine function is used since Obsidian does not allow the use of the "random-seed" Javascript library.

![Screenshot 2023-02-06 at 12 58 19 PM](https://user-images.githubusercontent.com/8411602/217086195-dea1a732-3981-4023-83ae-c9765d710815.png)
![Screenshot 2023-02-06 at 1 02 35 PM](https://user-images.githubusercontent.com/8411602/217086257-ebab004c-3bcd-41de-a611-a2bf4b666076.png)


Access [the Highlight of the Day script by clicking here](https://github.com/alvedsc/coding_portfolio/blob/main/codes/highlight_of_the_day.js)

#### Day Planner

Purpose: This script retrieves all tasks from all notes in the Obsidian Vault and organize them by their completion date, for every new daily note. Using this script, all daily notes will have a Day Planner section with tasks: 1. Overdue, 2. Today, 3. Upcoming, 4. Undated. It will also add the the "Today" list any tasks that have the #habit or #habit/weekly tags in the current note, or the weekly note. It will also add a link to the note where the task was originally written. This way, each task can easily be edited or marked as Complete using the Obsidian's [Hover Editor plug-in](https://github.com/nothingislost/obsidian-hover-editor)

Access [the Day Planner script by clicking here](https://github.com/alvedsc/coding_portfolio/blob/main/codes/day_planner.js)
