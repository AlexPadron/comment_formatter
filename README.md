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
