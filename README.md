# scrab_cheater
A command-line dictionary search tool based on regex

## Load the dictionary

```
Jon@Jons-MBP scrab_cheater % python3 cheat.py 
(3)>l dict.csv
(178691)>
```

## Specify tile-set 

```
(178691)>_ asfgrj
(178691)>
```

## Search the dictionary

```
(178691)>rx f__g       
(178691)>^f[asfgrj][asfgrj]g$(1)>p
frag
(178691)>^f[asfgrj][asfgrj]g$(1)>
```

