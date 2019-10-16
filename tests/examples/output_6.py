def foo():
    def bar():
        if y == 5:
            # This comment is very nested, that nesting should be preserved, even if the comment is
            # too long and needs reformatting
            pass
