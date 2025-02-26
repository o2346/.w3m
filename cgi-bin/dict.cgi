#!/usr/bin/perl

$url = "https://www.google.com/search?safe=off&num=24&hl=en&q=";
$_ = $ENV{"QUERY_STRING"};
$dict = "英和+";
if($_ =~ /[^a-zA-Z:]+/) {
  $dict = "和英+";
}
$noise = "+-weblio.jp";

if ($_) {
	s/\+/ /g;
	s/d://g;
	s/%([\da-f][\da-f])/pack('C', hex($1))/egi;
	s/[\000-\040\+:#?&%<>"\177-\377]/sprintf('%%%02X', unpack('C', $&))/eg;
	$url .= "$dict$_$noise";
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
