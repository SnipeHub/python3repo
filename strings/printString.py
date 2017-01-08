raw = r'this\t\n and that'      ## A "raw" string literal is prefixed by an 'r'
## and passes all the chars through without special treatment of backslashes, so r'x\nx'
## evaluates to the length-4 string 'x\nx'
print raw           ## this\t\n and that

multi = """It was the best of times.
It was the worst of times."""
print multi