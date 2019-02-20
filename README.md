# ips2map
A function that converts an input file with IPs into a map.

## Input file
A list of IPs. One IP per line. For example

```
13.112.224.240
13.115.13.148
13.210.129.177
13.210.176.167
13.228.126.182
13.228.224.121
13.230.11.13
13.230.90.110
13.55.153.188
13.55.5.15
```

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