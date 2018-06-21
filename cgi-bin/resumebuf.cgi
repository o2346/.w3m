#!/bin/sh
[ "$W3M_URL" = 'file:///cgi-bin/resumebuf.cgi' ] && exit 1
cat << EOF
w3m-control: GOTO $PREV_BUF
EOF
#file:/cgi-bin/resumebuf.cgi

