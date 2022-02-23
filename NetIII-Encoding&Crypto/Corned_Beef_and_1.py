#!/usr/bin/env python3
import hashlib
def matcher():
  md = '0a3a4cce269fee850e2ae01a1ca461f8'
  p = "FS{cabbage-wait_that's_not_right_"
  for h in range(0,10): #hundreds place digits from the range 0-9 since range is exlusive
    for t in range(0,10): #tens place digits
      for o in range(0,10): #first place digits
        guess = p + str(h) + str(t) + str(o) + '}' #variable to store the 3 XXX digits, p is the flag its + the last 3 digits
        hashGuess = hashlib.md5(guess.encode()) #hashGuess is the store the hash using the hashlib.md5
        if hashGuess.hexdigest() == md: #finding the comparison and returning True then print the guess
          print(guess)
matcher() #running the matcher
