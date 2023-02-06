/*
This script retrieves all tasks from all notes in the Obsidian Vault and organize them by their completion date, 
for every new daily note. Using this script, all daily notes will have a Day Planner section with tasks: 
1. Overdue, 2. Today, 3. Upcoming, 4. Undated. 
It will also add the the "Today" list any tasks that have the #habit or #habit/weekly tags in the current note, 
or the weekly note. It will also add a link to the note where the task was originally written. 
This way, each task can easily be edited or marked as Complete using the Obsidian's Hover Editor plug-in
*/

// function that gets the number of days between today and a date, and replaces it from a string in the original format
function howManyDays(inputString) {
  // Use a regular expression to match dates in the format [[YYYY-MM-DD]]
  const dateRegex = /\[\[([0-9]{4}-[0-9]{2}-[0-9]{2})\]\]/;

  // Find the first match of the regular expression in the input string
  const match = inputString.match(dateRegex);

  // If no match is found, return the original input string
  if (!match) {
    return inputString;
  }

  // Extract the matched date string
  const dateString = match[1];

  // Convert the date string to a JavaScript Date object
  const date = new Date(dateString);
  const fileDate = new Date(dv.current().file.name)

  // Get the current date
  const today = new Date();

  // Calculate the difference between the date in the string and today in days
  const diffDays = Math.floor((date - today) / (1000 * 60 * 60 * 24)) * -1 - 1;

  // Initialize a variable to store the label
  let label;

  // Check the value of diffDays to determine the label
  if (diffDays > 99) {
    label = `Long time ago (${date.toLocaleDateString("en-US",{weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'})})`;
  } else if (diffDays > 1) {
    label = `${diffDays} days ago (${date.toLocaleDateString("en-US",{weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'})})`;
  } else if (diffDays === 1) {
    label = `Yesterday`;
  } else if (diffDays === 0) {
    label = `Today`;
  } else if (diffDays === -1) {
    label = `Tomorrow`;
  } else if (diffDays > -99) {
    label = `in ${-diffDays} days (${date.toLocaleDateString("en-US",{weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'})})`;
  } else {
    label = `In a long time (${date.toLocaleDateString("en-US",{weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'})})`;
  }
  
  // Replace the matched date string with the date string and label
  let outputString = inputString.replace(dateRegex, `[[${dateString}|${label}]]`);
  let isToday = fileDate - date
  if (isToday === 0) {
	outputString = inputString.replace(dateRegex, ``);  
  }

  // Return the output string
  return outputString;
}

// find dates based on format [[YYYY-MM-DD]]
const findDated = (task)=>{
	if( !task.completed ) {
		task.header.display = "📝"
		task.text = task.text + " → " + task.header
		task.date="";
		const found = task.text.match(/\[\[([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))\]\]/);
		if(found) task.date = moment(found[1]);
		return true;
	}
}

// Builds the lists of tasks for each header
const myTasks = dv.pages("").file.tasks.where(t => findDated(t))

dv.table(["Overdue"],myTasks.filter(t=> moment(t.date).isBefore(dv.current().file.name,"day")).sort(t => t.text .replace(/^ */, "") .replace(/^([0-9]:)/, "0$1")).sort(t=>t.date).map(t=>[howManyDays(t.text)]),false );

// The tasks for the day take the tasks in the same daily note that contain the #habit tag
dv.table(["Today"],myTasks.filter(
	t => (moment(t.date).isSame(dv.current().file.name,"day"))
	||
	(
		(t.tags.includes("#habit"))
		&&
		(t.path.includes(dv.current().file.path) )
	)
)
.sort(t => t.text .replace(/^ */, "") .replace(/^([0-9]:)/, "0$1")).map(t=>[howManyDays(t.text)]), false);

dv.table(["Upcoming"],myTasks.filter(t=> moment(t.date).isAfter(dv.current().file.name,"day")).sort(t => t.text .replace(/^ */, "") .replace(/^([0-9]:)/, "0$1")).sort(t=>t.date).limit(10).map(t=>[howManyDays(t.text)]),false);

// This part takes all undated tasks 

dv.table(["Undated"],myTasks.filter(t=> (!t.date && !t.parent) && !(t.tags.includes("#habit")) && !(t.tags.includes("#habit/weekly")) ).sort(t=>t.text).map(t=>[t.text]), false);
