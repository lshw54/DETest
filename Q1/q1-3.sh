#!/bin/sh
 
$(touch ip.txt)
for i in $(cut -d '' -f 1 NASA_access_log_Aug95 | sort | uniq -c | sort -r | awk '{print $2}'); do
 
    ip=$(curl ipinfo.io/$i | grep country | cut -d ':' -f 2)
 
    echo $ip >>ip.txt
 
done
 
sort ip.txt | uniq -c | sort -r | head -1