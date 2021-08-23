#!/bin/bash

for i in {1..50}
do
        s='{"startTimestamp":1620748800000,"deviceId":"'$i'_A0DCEC5C-C5F8-4CD4-94A9-605CE3856B77","id":"B0DCEC5C-C5F8-4CD4-94A9-605CE3856B77'$i'","uid":"'$i'264fe8e4328e848f_test","bannerShowsNum":'$[RANDOM%100]',"enterDuration":'$[RANDOM%100]',"enterNum":'$[RANDOM%100]',"exitNum":'$[RANDOM%100]',"recNum":'$[RANDOM%100]',"searchNum":'$[RANDOM%100]',"showsNum":'$[RANDOM%100]',"sharingNum":'$[RANDOM%100]',"staryDuration":'$[RANDOM%100]',"clicksNum":'$[RANDOM%100]',"productClicksNum":'$[RANDOM%100]',"cancelLikesNum":'$[RANDOM%100]',"bannerShowsNum":'$[RANDOM%100]',"sharingNum":'$[RANDOM%100]'}';
        echo $s >> mongo.json
done
echo 1620748800000