#!/usr/bin/perl

#$url = "https://www.google.com/search?safe=off&q=";
$url = "https://html.duckduckgo.com/html/?q=";
#$noise = "&as_eq=naver%20cookpad%20rakuten%20weblio%20slideshare";
$noise = "";
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
