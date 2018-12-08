#!/usr/bin/python -E
# Inspired by: https://www.youtube.com/watch?v=FyCYva9DhsI&t=1299s
# https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition

def fizzbuzz(numero):
    test = lambda d, ss, x:  x if numero % d != 0 else lambda _: ss +  x('')
    fizz = lambda x: test(3, 'Fizz', x)
    buzz = lambda x: test(5, 'Buzz', x)
    return fizz(buzz(lambda x : x))(str(numero))


