#!bin/bash

start_date=2021-07-01
end_date=2021-07-31
count=500000

first_line="startTimestamp,deviceId,id,uid,showsNum,recNum,likesNum,enterNum,sharingNum,clicksNum,productShowsNum,"
first_line="${first_line}productClicksNum,exitNum,cancelLikesNum,bannerClicksNum,bannerShowsNum,searchNum"
echo $first_line > mongo.csv

run_start=$(date +%s)

while ! [[ $start_date > $end_date ]]; do
    startTimestamp=$(date -d "$start_date" "+%s000")
    for (( c=1; c<=$count; c++ )); do
        line=$startTimestamp
        line="${line},A0DCEC5C-C5F8-4CD4-94A9-605CE3856B_${c}"
        line="${line},B0DCEC5C-C5F8-4CD4-94A9-605CE3856B_${c}"
        line="${line},${c}_264fe8e4328e848f_test"
        line="${line},$[RANDOM%100]"
        line="${line},$[RANDOM%100]"
        line="${line},$[RANDOM%100]"
        line="${line},$[RANDOM%100]"
        line="${line},$[RANDOM%100]"
        line="${line},$[RANDOM%100]"
        line="${line},$[RANDOM%100]"
        line="${line},$[RANDOM%100]"
        line="${line},$[RANDOM%100]"
        line="${line},$[RANDOM%100]"
        line="${line},$[RANDOM%100]"
        line="${line},$[RANDOM%100]"
        line="${line},$[RANDOM%100]"
        echo ${line} >> mongo.csv
    done
    echo "$start_date $startTimestamp"
    start_date=$(date -d "$start_date + 1 day" +%F)
done

run_end=$(date +%s)
echo "Ran "$(($run_end - $run_start))" s"