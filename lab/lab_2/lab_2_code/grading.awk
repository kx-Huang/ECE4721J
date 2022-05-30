#!/usr/bin/awk -f

BEGIN {
    # Config
    ROW_NUM=10000
    FIRST_INPUT="data/firstnames.txt"
    LAST_INPUT="data/lastnames.txt"
    ID_INPUT="data/id.txt"
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
    i=0;
    while(getline < ID_INPUT){
        id[i++]=$0;
    }

    # Generate csv
    r=0;
    while(r++ < ROW_NUM){
        num = rand()
        printf "%s %s%s%s%s%d\n",first[int(num*f)],last[int(num*l)],DELIM,id[int(num*i)],DELIM,int(rand()*100);
    }
}
