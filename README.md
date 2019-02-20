# ips2map
A function that converts an input file with IPs into a map.

## Input file
A list of IPs. One IP per line.


## Example
```
python3 ips2map.py -f ips.txt -o map.eps -t "World Map" -m 'v' -c 'red'
```

where 

* `-m`/`--marker`
* `-t`/`--title`
* `-c`/`--color`
* `-f`/`--file`
* `-o`/`--output`