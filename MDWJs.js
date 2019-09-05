
var SPC = [" ","&nbsp;","&ensp;","&ensp;[SPACE]","&emsp;","&emsp;[SPACE]"]
function run() {
	// since the entire input block is taken in at once, line by line is unnessesary
	// note, replace only gets the first instance, use REGEX
	var input = document.getElementById("userIn").value;
	if ((input == "") && (document.getElementById("userOut").value != "")){
		document.getElementById("userIn").value = mdToTxt(document.getElementById("userOut").value);
	}
	else {
		document.getElementById("userOut").value = optMd(input);
	}
}

function optMd(input) {
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
    return(input);
}

function mdToTxt(input) {
	for (var i = 1; i < 5; i = i*2) {
		var re = new RegExp(SPC[i], "g");
	    input = input.replace(re, " ".repeat(i));
	}
    return(input);
}

function themeUpdate(type) {
	const root = document.documentElement;
	var colours = ["","","","",""];
	switch (type){
		case "day":
			colours = ['#F0EDE5', '#1F2833', '#A5DD96', '#1E9EB9', '#F0EDE5'];
			break;
		case "night":
			colours = ['#080135', '#F0EDE5', '#008393', '#602C50', '#080135'];
			break;
		case "pastel":
			colours = ["#76ADA8", '#CFD7C0', '#789561', '#E6A99F', '#76ADA8'];
			break;
		case "neon":
			colours = ['#b967ff', '#05ffa1', '#ff71ce', '#01cdfe', 'black'];
			break;
	}

	root.style.setProperty('--bg', colours[0]);
	root.style.setProperty('--textCol', colours[1]);
	root.style.setProperty('--buttonCol', colours[2]);
	root.style.setProperty('--borderCol', colours[3]);
	root.style.setProperty('--textBox', colours[4]);
}