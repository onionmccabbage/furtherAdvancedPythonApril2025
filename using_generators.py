# the range object
r = range(0, 33, 2) # start, stop-before, step
print(r, type(r)) # a range does not persist its values in memory

f = (i*i for i in range(0,101,2))
print(f, type(f)) # a generator does not persist its values in memory - it yields them as needed
# iteration causes the generator to yield each member in turn
for i in f:
    print(i)

# comprehension
e = [i*i for i in range(0,101,2)]
print(e, type(e)) # a list comprehension persists all the members in memory

# we may write a custom generator
def tally(incr=1, maxi=False):
    '''this generator will yield sn endless tally of values'''
    score = 0
    try:
        while True:
            yield score # yield makes this function become a generator
            score += incr
            if maxi and score > maxi:
                raise StopIteration # the corrrect way to terminate a generator
    except StopIteration as e:
        pass

if __name__ == '__main__':
    game = tally(5, 40) # we now have a generator
    print(game, type(game))
    # we may access the next member of any generator
    print( game.__next__() ) # 0
    print( game.__next__() ) # 1
    print( game.__next__() ) # 2
    print( game.__next__() ) # 3
    for _ in game: # this will continue from where we got to
        print(_)
    print( game.__next__() ) # .....