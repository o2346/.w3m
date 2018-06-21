#!/bin/sh
cat << EOF
w3m-control: SETENV PREV_BUF=$W3M_URL
w3m-control: CLOSE_TAB
EOF
#file:/cgi-bin/deletebuf.cgi
