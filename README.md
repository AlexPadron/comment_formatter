# Comment Formatter for Python

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
python -m comment_formatter.run /path/to/my/files [--line-length X]
```