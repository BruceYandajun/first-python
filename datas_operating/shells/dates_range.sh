#!bin/bash

start=2021-08-01
end=2021-08-31
count=5
while ! [[ $start > $end ]]; do
    for (( c=1; c<=$count; c++ )); do
        startTimestamp=$(date -d "$start" "+%s000")
        data='{"startTimestamp":'$startTimestamp','
        data=$data'"deviceId:"'$i'_A0DCEC5C-C5F8-4CD4-94A9-605CE3856B77",'
        data=$data'"id":"'$i'B0DCEC5C-C5F8-4CD4-94A9-605CE3856B77",'
        data=$data'"uid":"'$i'264fe8e4328e848f_test",'
        data=$data'"bannerShowsNum":'$[RANDOM%100]','
        data=$data'"enterDuration":'$[RANDOM%100]','
        data=$data'"enterNum":'$[RANDOM%100]','
        data=$data'"exitNum":'$[RANDOM%100]','
        data=$data'"recNum":'$[RANDOM%100]','
        data=$data'"searchNum":'$[RANDOM%100]','
        data=$data'"showsNum":'$[RANDOM%100]','
        data=$data'"sharingNum":'$[RANDOM%100]','
        data=$data'"stayDuration":'$[RANDOM%100]','
        data=$data'"clicksNum":'$[RANDOM%100]','
        data=$data'"productClicksNum":'$[RANDOM%100]','
        data=$data'"cancelLikesNum":'$[RANDOM%100]','
        data=$data'"bannerShowsNum":'$[RANDOM%100]','
        data=$data'"sharingNum":'$[RANDOM%100]','
        echo $data
    done

    echo $start" "$startTimestamp
    start=$(date -d "$start + 1 day" +%F)
done