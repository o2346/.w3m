#!/bin/bash

cd `dirname $0`
for f in ??*
do
    case $f in
      .git) continue;;
      .gitignore) continue;;
      .DS_Store) continue;;
      README.md) continue;;
      cgi-bin) continue;;
      $0) continue;;
    esac
    [ -f ~/$f ] && continue || echo create symlink $f

    ln -sv $(pwd)/$f ~/.w3m
done
