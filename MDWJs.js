
var SPC = [" ","&nbsp;","&ensp;","&ensp;[SPACE]","&emsp;","&emsp;[SPACE]"]
function run() {
	var input = document.getElementById("userIn").value;
	input = input.replace("     ", SPC[5])
    input = input.replace("    ", SPC[4])
    input = input.replace("   ", SPC[3])
    input = input.replace("  ", SPC[2])
    input = input.replace("/n ", "/n" + SPC[1])
    // replace placeholder spaces with actual space
    input = input.replace("[SPACE]", SPC[0])
   	document.getElementById("userOut").value = input;
}
