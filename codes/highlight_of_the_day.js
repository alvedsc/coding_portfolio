/*
The objective of this script is to get a random highlight from a random book from a folder of book highlights imported 
using the "Kindle Highlights" plug-in. 
This is based on the principle of Spaced Repetition, where recurrently exposing oneself to a piece of knowledge (a highlight) 
can increase its retention
*/


// This function codes the date so that it becomes a random number between two numbers, low and high. 
function codeDate(date, low, high) {
    let seed = date.split("-").join("");
    let random = Math.sin(seed) * 10000;
    return Math.floor((random - Math.floor(random)) * (high - low + 1) + low);
}


/* 
This function takes a string as input extracts all substrings between a paragraph break and the character "^" and returns them as an array. 
This is necessary to 
*/
function getSubstrings(str) {
  let result = [];
  let re = /\n(.*?)\^/g;
  let match;
  while ((match = re.exec(str)) != null) {
    result.push(match[1]);
  }
  return result;
}

/* 
The function gets the metadata of the kindle book. All Kindle imports have the same format, so this can be exploited to turn each Kindle Highlight
file into an array of Highlights.
*/
function getMeta(str) {

	const extractedData = [];
	const lines = str.split("\n");
	
	let inDataBlock = false;
	let title, author;
	for (let i = 0; i < lines.length; i++) {
	  const line = lines[i];
	  if (line.trim() === "---") {
	    inDataBlock = !inDataBlock;
	    continue;
	  }
	  
	  if (!inDataBlock) {
	    if (line.startsWith("#")) {
	      extractedData.push(line.substring(1).trim());
	    }
	    continue;
	  }
	  
	  if (line.includes("title:")) {
	    title = line.split("title: ")[1].trim().replace(/'/g, "");
	  }
	  
	  if (line.includes("author:")) {
	    author = line.split("author: ")[1].trim();
	  }
	}
	
	extractedData.unshift(title, author);
	return extractedData; 
}


let date = dv.current().file.name

// Gets all files inside the Kindle folder
let books = app.vault.getFiles().filter(file => file.path.includes("Kindle")) 

// Selects a random book from the Kindle Folder
let bookList = books.map(file => dv.fileLink(file.path));
let randomBookIndex = codeDate(date, 0, bookList.length - 1); 
let randomBook = bookList[randomBookIndex];

// Selects a random highlight inside the random book
let content = await dv.io.load(randomBook.path);
let highlightList = getSubstrings(content);
let randomHighlightIndex = codeDate(date, 0, highlightList.length - 1); 
let randomHighlight = highlightList[randomHighlightIndex];

// The following lione of code prints the resulting highlight in the right format so that it displays as a quote on the Obsidian interface
dv.paragraph ("> [!quote] " + getMeta(content)[2] + "\n> " + randomHighlight + "\n> \n> " + "&mdash; <cite>" +getMeta(content)[1] + "</cite>")
