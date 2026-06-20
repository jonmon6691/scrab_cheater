# scrab_cheater
A command-line dictionary search tool based on regex

## Load the dictionary

```
$ python3 cheat.py 
(0)>l dict.csv
(178691)>?    
Commands:
  r <regex> - Raw regex. '_' is replaced with the tile set.
    rs <regex> - "Starts with" -> ^regex_*$
    re <regex> - "Ends with" -> ^_*regex$
    rw <regex> - "Wrap" -> ^_*regex_*$
    rx <regex> - "Exact" -> ^regex$
  b - Go back to the most recent state
  p - Print set
  l <filename> - Load a dictionary file.
  _ [chars] - Print / reset tile set
  ? - Print this help message
  q - Quit
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
