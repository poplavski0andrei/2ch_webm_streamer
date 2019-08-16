#!/bin/bash
    

    #if [ $1 = '-h' -o $1 = '--help' ]; then echo "Usage: ./stream.sh [URL] -p [PLAYER]"; exit 1;fi 
    #if [ $# -ne 3 ]; then echo "Arguments error" >&2; exit 1; fi

   # curl $1 -o thread_copy || echo "URL error" >&2||exit 1
    
parse_b() {
    curl https://2ch.hk/b/catalog.json -o catalog.json 
    jq '[.threads[] | {num: .num, subject: .subject, files_count: .files_count} | select(.subject|test("([цшw][уэe][ибb][ьмm]|[мm][пp]4)"; "i"))]' catalog.json > parsed_b.json
}

print_threads() {
    THREAD_CNT=0
    for thread in $( grep -o 'subject' parsed_b.json)
    do
	    echo "Thread #${THREAD_CNT}"
	    jq ".[${THREAD_CNT}]" parsed_b.json
	    THREAD_CNT=$(( $THREAD_CNT + 1 ))
    done
}

download_thread() {
    echo 'Choose your thread (print a number):'
    read THREAD
    curl https://2ch.hk/b/res/`jq --raw-output ".[$THREAD][\"num\"]" parsed_b.json`.json | \
    jq '.threads | .[] | .posts | .[] | .files | .[] | {name: .fullname, path: .path, duration: .duration_secs}' > temp_playlist.json
}

create_playlist() {
    echo "#EXTM3U" > playlist.m3u || (echo "Creating playlist error" ; exit 1)
    COUNTER=1
    for i in $(seq 0 $(expr $(jq -s 'length' temp_playlist.json) - 1))
    do
      name=$(jq -s --raw-output ".[$i].name" temp_playlist.json)
      path="https://2ch.hk$(jq -s --raw-output ".[$i].path" temp_playlist.json)\n"
      duration=$(jq -s --raw-output ".[$i].duration" temp_playlist.json)
      echo -e "#EXTINF:$duration, $name\n$path" >> playlist.m3u
    done
    echo success
}

generateHtml() {
  if command -v python3 &> /dev/null; then
    python3 ./web/generateHtml.py
  else
    echo "python3 is not found"
  fi
}

clean() {
    rm -rf catalog.json pared_b.json temp_playlist.json
}
parse_b
print_threads
download_thread
create_playlist
generateHtml
