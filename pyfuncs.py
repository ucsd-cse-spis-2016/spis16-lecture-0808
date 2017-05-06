def Hamming(s1, s2):
     '''Takes two strings of the same length
     and returns the number of positions
     at which they differ or -1 if strings
     are of different lengths'''
     if len(s1) == 0:
          return 0
     if s1[0] ==s2[0]:
         return  Hamming(s1[1:],s2[1:])
     else:
          
          return 1+Hamming(s1[1:],s2[1:])


def isPal(s):
    ''' Assumes s is a str consisting of letters. Returns true if
    the letters in s form a palindrome, False otherwise.'''

    return 'stub'
