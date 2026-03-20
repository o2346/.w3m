#!/bin/sh
if echo "$W3M_CURRENT_LINK" | grep 'ch.io/test/read.cgi' > /dev/null; then
  W3M_CUSTOM_LINK="`echo $W3M_CURRENT_LINK | sed -e 's|read\.cgi|read\.cgi\/c|g' | sed -e 's/\-[0-9]*$//'`"
elif echo "$W3M_CURRENT_LINK" | grep 'http://jump5.ch/?' > /dev/null; then
  W3M_CUSTOM_LINK="`echo $W3M_CURRENT_LINK | sed -e 's|^http://jump5.ch/?||'`"
else
  W3M_CUSTOM_LINK="$W3M_CURRENT_LINK"
fi
cat << EOF
w3m-control: GOTO $W3M_CUSTOM_LINK
EOF
#file:/cgi-bin/customjump.cgi
