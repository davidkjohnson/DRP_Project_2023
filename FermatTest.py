import math
import random


class FermatTest:
    def sqam(self, base: object, exponent: object, modulus: object) -> object:
        res = 1
        while exponent > 1:
            if exponent > 1:
                res = (res * base) % modulus
            base = base ** 2 % modulus
            exponent >>= 1
        return (base * res) % modulus

    def fermat(self,b,n):
        return pow(b,n-1,n)==1

    def test(self,n):
        result = True
        i = 0
        while i <= 11:
            base = random.randint(1,n)
            while math.gcd(base,n)!=1:
                base=random.randint(1,n)
            result = self.fermat(base,n)
            i+=1
        return result


t = FermatTest()

inputNumber = input("Type an integer greater than 1: ")
foo = int(inputNumber)
isPrime = t.test(foo)

if isPrime == False:
    print("The integer is composite")
else:
    print("The integer is prime")

