#!/bin/zsh

start=2014-12-29
end=2015-01-03
while ! [[ $start > $end ]]; do
    echo $start
    start=$(date -d "$start + 1 day" + %F)
done


