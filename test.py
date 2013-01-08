# == default python implementation ==

def default_fizzbuzz():
    for i in xrange(1, 101):
        if i % 15 == 0:
            "FizzBuzz"
        elif i % 3 == 0:
            "Fizz"
        elif i % 5 == 0:
            "Buzz"
        else:
            i


# == purely functional ==

def purely_functional():
    '\n'.join(''.join(''.join(['' if i%3 else 'Fizz',
                                      '' if i%5 else 'Buzz']) 
                             or str(i)) 
                     for i in range(1,101))


# == pyfnc ==

from pyfnc import patterned, pattern

@pattern(0, 0)
def fizzbuzz_fizzbuzz(n, m):
    return "FizzBuzz"

@pattern(0, int)
def fizzbuzz_fizz(n, m):
    return "Fizz"

@pattern(int, 0)
def fizzbuzz_buzz(n, m):
    return "Buzz"

@patterned
def fizzbuzz(n, m):
    pass

def do_fizzbuzz_pyfnc():
    for i in xrange(100):
        try:
            fizzbuzz(i % 3, i % 5)
        except:
            i

# == pyfpm ==

from pyfpm.matcher import Matcher

def pyfpm_fizzbuzz():
    myfizzbuzz = Matcher([
        ('[0, 0]', lambda: "FizzBuzz"),
        ('[0, _:int]', lambda: "Fizz"),
        ('[_:int, 0]', lambda: "Buzz"),
        ])
        
    for i in xrange(100):
        try:
            myfizzbuzz([i % 3, i % 5])
        except:
            i
    
if __name__ == '__main__':
    import timeit
    print timeit.timeit('do_fizzbuzz_pyfnc()', 'from __main__ import do_fizzbuzz_pyfnc',number=100)
    print timeit.timeit('default_fizzbuzz()', 'from __main__ import default_fizzbuzz',number=100)
    print timeit.timeit('purely_functional()', 'from __main__ import purely_functional',number=100)
    print timeit.timeit('pyfpm_fizzbuzz()', 'from __main__ import pyfpm_fizzbuzz',number=100)
    