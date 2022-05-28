#!/usr/bin/awk -f
function getRandomId(){
    return sprintf("%005d%005d",rand()*99999,rand()*99999)
}

BEGIN {
    # Config
    ROW_NUM=200000
    FIRST_INPUT="l2-names/firstnames.txt"
    LAST_INPUT="l2-names/lastnames.txt"
    DELIM=","
    srand();

    # Read names
    f=0;
    while(getline < FIRST_INPUT){
        first[f++]=$0;
    }
    l=0;
    while(getline < LAST_INPUT){
        last[l++]=$0;
    }
    
    # Generate csv
    r=0;
    while(r++ < ROW_NUM){
        printf "%s %s%s%s%s%d\n",first[int(rand()*f)],last[int(rand()*l)],DELIM,getRandomId(),DELIM,int(rand()*100);
    }
}
