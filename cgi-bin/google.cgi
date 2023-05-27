#!/usr/bin/perl

$url = "https://www.google.com/search?safe=off&num=24&hl=en&access=a&q=";
# $url = "https://www.bing.com/search?sc=8-0&num=16&setmkt=en-us&setlang=en-us&q=";
# https://support.google.com/gsa/answer/6329265#4134d4ec-c7f1-4eff-ae65-b171e689ca5a
$noise = "&as_eq=naver%20cookpad%20rakuten%20weblio%20slideshare%20i-3-i%2Einfo";
$_ = $ENV{"QUERY_STRING"};
s@^s:@@ && s@^//@@ && s@/$@@;
if ($_) {
	s/\+/ /g;
	s/%([\da-f][\da-f])/pack('C', hex($1))/egi;
	s/[\000-\040\+:#?&%<>"\177-\377]/sprintf('%%%02X', unpack('C', $&))/eg;
	$url .= "$_$noise";
} else {
	$input = "w3m-control: GOTO_LINK";
}
print <<EOF;
w3m-control: GOTO $url
w3m-control: DELETE_PREVBUF
w3m-control: SEARCH \\[
w3m-control: MOVE_RIGHT
${input}

EOF
