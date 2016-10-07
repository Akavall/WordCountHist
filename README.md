# Word Count Hist

Allows user to create a histogram of word counts of all files and sub-directorys, including zipped directories in a given directory path.

Set up:

```
git clone https://github.com/Akavall/WordCountHist
```

Now you want to add the directory that contains `/utilities` to your PYTHONPATH,
For example:

```
export PYTHONPATH="${PYTHONPATH}:/your/directory/path"
```

And you have to create an executable:

```
chmod +x word_count_hist.py
```

How to use:

```
./word_count_hist.py /your/directory/data/path
```

Run tests:

In the folder that holds `/utilites` run:

```
nosetests
```

or 

```
nosetests -v
```
