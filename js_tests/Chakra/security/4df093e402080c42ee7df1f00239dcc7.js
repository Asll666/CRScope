function main() {
	RegExp.input = {toString: f};
	RegExp.lastMatch;
//  alert(RegExp.lastMatch);
}

var input = [Array(10000000).join("a"), Array(11).join("b"), Array(100).join("a")].join("");

function f() {
	String.prototype.match.call(input, "bbbbbbbbbb");
}

main();
