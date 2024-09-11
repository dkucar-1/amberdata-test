This utility does some simple text processing. In essence, extracting word counts.
It uses standard Python functions, no Pandas or Spark dataframes and such, so we're assuming
relatively small data sets.

### Usage ###
From the directory where you've copied this file and the list of words. The path to file is optional.
If you do not give it, it will assume you are running from current working directory.

```
./process_words.py [<path-to-word-file>]
```

This process assumes each row in the input file is indexed by key `words`.

### Testing ###
Just run `pytest` and it will run some simple tests on the functions. Tests like
* verifying there are some odd-lengths in the list of words
* verifying the list is sorted in non-descending order


