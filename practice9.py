import unittest
from useless_pack.useless.divisibility.functions import number_is_prime,extended_Euclid

aa=[2,3,5]
def industrial_grade_prime(n):
    f=True
    for a in aa:
        f=(f and a**(n-1)%n==1)or(n in aa)
    return f

extended_Euclid(111,432)

class MyTests(unittest.TestCase):
    
    def setUp(self):
        self.primes_to_1000 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,
            97,101,103,107,109,113,127,131,137,139,149,151,
            157,163,167,173,179,181,191,193,197,199,211,223,
            227,229,233,239,241,251,257,263,269,271,277,281,
            283,293,307,311,313,317,331,337,347,349,353,359,
            367,373,379,383,389,397,401,409,419,421,431,433,
            439,443,449,457,461,463,467,479,487,491,499,503,
            509,521,523,541,547,557,563,569,571,577,587,593,
            599,601,607,613,617,619,631,641,643,647,653,659,
            661,673,677,683,691,701,709,719,727,733,739,743,
            751,757,761,769,773,787,797,809,811,821,823,827,
            829,839,853,857,859,863,877,881,883,887,907,911,
            919,929,937,941,947,953,967,971,977,983,991,997]
        self.input_euclid = [(111, 432), (661, 113), (72, 96), (30, 18), (64, 48), (220, 600), (72, 96)]
        self.output_euclid = [(3, -35, 9), (1, -20, 117), (24, -1, 1), (6, -1, 2), (16, 1, -1), (20, 11, -4), (24, -1, 1)]
        
    def test_to_1000_number_is_prime(self):
        i=1
        while i<1000:
            if i in self.primes_to_1000:
                self.assertTrue(number_is_prime(i))
            else:
                self.assertFalse(number_is_prime(i))
            i+=1
     
    def test_to_1000_industrial_grade_prime(self):
        i=1
        while i<1000:
            if i in self.primes_to_1000:
                self.assertTrue(industrial_grade_prime(i))
            else:
                self.assertFalse(industrial_grade_prime(i))
            i+=1
            
    def test_euclid(self):
        i=0
        for inp in self.input_euclid:
            a,b=inp
            self.assertEqual(extended_Euclid(a,b),self.output_euclid[i])
            i+=1

unittest.main()
