This utility does some simple text processing. In essence, extracting word counts.
It uses standard Python functions, no Pandas or Spark dataframes and such, so we're assuming
relatively small data sets. It assumes you are running Python v 3.9 or higher (as an `assert` statement)

### Usage ###
From the directory where you've copied this file and the list of words. 
By default, the code will run with `words.json` provided with this repo.
You can optionally pass a path to a word file.
```
./process_words.py [<path-to-word-file>]
```

NOTE: This process assumes each row in the input file is indexed by key `words`.

### Testing ###
First make sure you have pytest installed. You can do 
`pip3 install -r requirements.txt`. 
You might also need to add it to your `PATH`, so something like editing your `.bash_profile`
`PATH=...:$HOME/Library/Python/3.9/bin/pytest`

Just run `pytest` in this directory and it will run some simple tests on the functions. Tests like
* verifying there are some odd-lengths in the list of words
* verifying the list is sorted in non-descending order


