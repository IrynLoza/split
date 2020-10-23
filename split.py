"""Split a string by splitter and return list of splits.

This should work like the built-in Python .split() method [*].
YOU MAY NOT USE the .split() method in your solution!
YOU MAY NOT USE regular expressions in your solution!

For example:

    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']

* Note: the actual Python split method has special behavior
  when it is not passed anything for the splitter -- you do
  not need to implement that.

"""


def split(astring, splitter):
    """Split a string by splitter and return list of splits."""
    result = []
    index = 0

    while index <= len(astring):

        curr_index = index
        #find indexes of first splitter char 
        index = astring.find(splitter, index)

        #check if found first char of splinter not last element in full string
        if index != -1:
            #append sliced string to result
            result.append(astring[curr_index:index])
            #update index to skip the full splenter
            index += len(splitter)

        else:
            # couldn't find any more instances of splitter in astring
            result.append(astring[curr_index:])
            break

    return result      


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. FINE SPLITTING!\n")
