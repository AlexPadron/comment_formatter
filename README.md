# Comment Formatter for Python

[![Build Status](https://travis-ci.org/AlexPadron/comment_formatter.svg?branch=master)](https://travis-ci.org/AlexPadron/comment_formatter)

Comment formatter automatically restructures comments in your code to be compliant
with line length standards.

```python
def foo():
    def bar():
       # Here we have a very long block comment that is not evenly spaced. We see that some lines are very long,
       # while
       # others are
       # very short.
       #
       # We want to reformat this while preserving the comment structure
```
Converts to

```python
def foo():
    def bar():
       # Here we have a very long block comment that is not evenly spaced. We see that some lines are
       # very long, while others are very short.
       #
       # We want to reformat this while preserving the comment structure
```

## Installation

```
pip install comment-formatter
```


## Usage

```
python -m comment_formatter.run /path/to/my/files [--line-length X] [--check]
```

If the `check` flag is passed, the script will log an error and exit 1 instead of reformatting files.

## Why Comment Formatter

When I use multiline block comments in my code, I often go back and edit them later,
which means I'm left with lines of uneven length that may exceed linter line limits.

Since I use emacs which doesn't (to my knowledge) support reformatting comments to be compliant
with line length standards, I wrote comment formatter to do this for me.

## How it Works

Comment formatter starts by grouping together comments in a blocks like

```python
# This is a
# comment block
#
# This is a separate block to maintain formatting

if x == 5:
    pass
    # This comment
# is a separate block from this because of indentation
```

After computing the blocks, comment formatter makes a best effort attempt to squash
the blocks together given line length constraints.
Splitting is only done on spaces, so very long words that do not fit in a single line
will not be reformatter.
