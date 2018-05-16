#!/usr/bin/perl

$url = "https://www.google.co.jp/search?safe=off&num=16&q=";
$noise = "+-matome.naver.jp+-cookpad.com+-nikkeibp.co.jp+-rakuten.co.jp+-weblio.jp+-slideshare.net+-japan.zdnet.com+-%E3%83%9F%E3%83%84%E3%82%A8%E3%83%BC%E3%83%AA%E3%83%B3%E3%82%AF%E3%82%B9+-news.mynavi.jp";
$_ = $ENV{"QUERY_STRING"};
s@^g(oogle)?:@@ && s@^//@@ && s@/$@@;
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
