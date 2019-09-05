
var SPC = [" ","&nbsp;","&ensp;","&ensp;[SPACE]","&emsp;","&emsp;[SPACE]"]
function run() {
	// since the entire input block is taken in at once, line by line is unnessesary
	// note, replace only gets the first instance, use REGEX
	var input = document.getElementById("userIn").value;
	if (input[0] == " "){
        input = input.replace(" ", SPC[1])
	}
	input = input.replace(/     /g, SPC[5])
    input = input.replace(/    /g, SPC[4])
    input = input.replace(/   /g, SPC[3])
    input = input.replace(/  /g, SPC[2])
    input = input.replace(/\n /g, "\n" + SPC[1])
    // replace placeholder spaces with actual space
    input = input.replace(/\[SPACE\]/g, SPC[0])
   	document.getElementById("userOut").value = input;
}
