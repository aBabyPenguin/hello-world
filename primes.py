#Fermat's Little Theorem to find primes written by aBabyPenguin
#a^p - a	Where 'a' is any integer greater than 2 and smaller than p. And p is the number being tested as prime. 

#If all a [1,p] are divisible by p, p is prime
#Carmichael numbers may falsely pass this test


def flt(p, a):						#Fermat's Little Theorem
	result = (a**p - a)%p			#Run flt for p and a
	return result

def isPrimeF(prime = 1):				#Repeat flt, updating 'a' for all numbers between 1 and 'p'.
	global primeList
	n=1
	while n<=prime:
		(n, result) = (n+1, flt(prime,n))
		if result != 0:				#If modulo returns non-zero, number is not prime.
		    return False
	if prime not in primeList:		#If number is prime, and not already in primeList, append number to primeList.
		primeList.append(prime)
	return True	

def isPrime(prime = 1):				#Repeat flt, updating 'a' for all numbers between 1 and 'p'.
	global primeList
	n=1
	while n<=prime:
		(n, result) = (n+1, flt(prime,n))
		if result != 0:				#If modulo returns non-zero, number is not prime.
		    return False
		elif  prime > 560:
			if carmichaelCheck(prime):
				return False
	if prime not in primeList:		#If number is prime, and not already in primeList, append number to primeList.
		primeList.append(prime)
	return True

def carmichaelCheck(n = 1, n2 = 3):
	result2 = n%2
	result3 = n%3
	result5 = n%5
	result7 = n%7
	result11 = n%11
	result13 = n%13
	result17 = n%17
	result19 = n%19
	result31 = n%31
	result37 = n%37
	result41 = n%41
	if (result2 == 0 or result3 == 0 or result5 == 0 or result7 == 0 or result11 == 0 or result13 == 0 or result17 == 0 or result19 == 0 or result31 == 0 or result37 == 0 or result41 == 0) and n >= 560:
		return True
	else:
		return False

def fermat(i='k'):					#Repeat isPrime, updating 'p' for all numbers between 1 and 'i'.
	global primeList
	primeList = []					#Clear primeList
	try:
		for n in range(1,i+1):
			isPrimeF(n)
		print (primeList)
	except TypeError:				#In case user inputs wrong type, print disclaimer.
		print("Not a valid input, please only use integers")
	
def primes(i='k'):					#Repeat isPrime, updating 'p' for all numbers between 1 and 'i'.
	global primeList
	primeList = []					#Clear primeList
	try:
		for n in range(1,i+1):
			isPrime(n)
		print (primeList)
	except TypeError:				#In case user inputs wrong type, print disclaimer.
		print("Not a valid input, please only use integers")
	
primeList = []						#Define primeList variable

print ("input fermat('int') to list fermat primes up to 'int'")
print ("input primes('int') to list all primes up to 'int'")
print ("input isPrimeF('int') to test if one integer is a Fermat prime")
print ("input isPrime('int') to test if one integer is prime")
