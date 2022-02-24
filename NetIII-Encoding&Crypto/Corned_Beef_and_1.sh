#!/usr/bin/env bash
matcher () { #matcher function to do the hashing no need to import hashlib since md5sum will do the hash encoding on the line
  mdhash="0a3a4cce269fee850e2ae01a1ca461f8" #variable to store the original md5 hash
  flag="FS{cabbage-wait_that's_not_right_" #variable to store the incomplete flag missing the last 3 digits
  for numbers in {000..999} #for-loop in bash syntax to loop from 000 to 999
  do #need do for bash syntax
    guess=$flag$numbers} #guess is equal to FS{cabbage-wait_that's_not_right_ + numbers so example: FS{cabbage-wait_that's_not_right_000 in first iteration
    guessHash=$( echo -n "$guess" | md5sum | awk '{print $1}' ) #md5sum outputs a filename after the calculated md5sum command, which in this case is - or stdin stream. To get rid of that part via any text processing utility commands that will let you cut away words, like awk: so awk "{print $1}" will print the first field there is two columns for the output normally -> "hash -" notice the - is in the second column, with awk we only grab the first column the column with the hash thereby removing the -
#for awk print $0 for whole line, $1 for first field, $2 for second field
    if [[ $guessHash = $mdhash ]]; #if-statement syntax , double square brackets [[ ]] so you no longer have to quote " " variables because [[ ]] handles empty strings and strings with whitespace more intuitively
    then echo $guess #print only the one that matches the original hash
    fi #signifies the end of the if-statement
  done #end of the for-loop terminates since we are done with the function
}
matcher #calling the matcher function no () needed since this is bash syntax
