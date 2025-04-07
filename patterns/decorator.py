# The decorator pattern is used widely within Python
# Anything that begins with '@' is a Python decorator

def squares(m ,n):
    '''return a list of the square integers between m and n'''
    s = []
    for i in range(m,n):
        s.append(i*i)
    return s

if __name__ == '__main__':
    # the following code only executes when we run this module directly (not via import)
    result = squares(1, 11)
    print(result)