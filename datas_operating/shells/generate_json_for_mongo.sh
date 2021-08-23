#!bin/bash

start_date=2021-07-01
end_date=2021-07-31
count=5000
first=true

run_start=$(date +%s)

while ! [[ $start_date > $end_date ]]; do
    startTimestamp=$(date -d "$start_date" "+%s000")
    for (( c=1; c<=$count; c++ )); do
        data='{"startTimestamp":'$startTimestamp','
        data=$data'"deviceId":"'$i'_A0DCEC5C-C5F8-4CD4-94A9-605CE3856B",'
        data=$data'"id":"'$i'B0DCEC5C-C5F8-4CD4-94A9-605CE3856B",'
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
        data=$data'"sharingNum":'$[RANDOM%100]'}'
	if [ $first = true ]; then
            echo $data > mongo.json
	else
	    echo $data >> mongo.json
	fi
	first=false
    done

    echo $start_date" "$startTimestamp
    start_date=$(date -d "$start_date + 1 day" +%F)
done

run_end=$(date +%s)
echo 'Ran '$(($run_end - $run_start))' s'