import hashlib
def matcher():
  md = 'a497453fe1eee3e0c4d44f2a74a1518744d247a1c6dd6c902a2b3367987f0e5d21fb1cbdd1af55ea78098be5a336ffaf06f19b8e5a5997e06d20ce00f9907424' #the sha hash from the cyberlabs problem
  p = "FS{hash-I_had_corned_beef_and_hash_" #the flag is the password used to generate the sha hash
  a = 0x000 #starting hex range 0
  b = 0xFFF #ending hex range 4096
  #a = 000 #same as saying 0x000 in decimal
  #b = 4095 #same as saying 0xFFF in decimal
  for x in range(a,b+1): #for loop to go through the entire from from 0x000 - 0xFFF, +1 so that in decimal its 4095 because range is 0-4094
    x = hex(x).upper() #uppercasing the hex code because it was look like this 0xabc uppercasing it does this 0xABC
    guess = p + x[-3:] + '}' #we only want to add in the last 3 digits so we slice from -3 index 3 third to last position 0xFFF so the first F to the end of the string
    #p = "FS{hash-I_had_corned_beef_and_hash_FFF}"
    hashGuess = hashlib.sha512(guess.encode()) #using sha512 to encode which is 128 bits
    if hashGuess.hexdigest() == md: #finding the match
      print(guess) #printing it out on the output the correct flag
matcher() #running the matcher
