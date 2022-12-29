#!/bin/bash

<<INFO
Author: Christophe DUFOUR
INFO

# static version
#SECRET=85

# random version (between 1 and 10)
SECRET=$((RANDOM % 10))

# infinite loop
while true; do
  read -p "Devine mon chiffre secret: " answer
  
  if [ ${answer} == ${SECRET} ]; then
    # break the loop if correct answer given
    break
  fi

  if [ ${answer} -gt ${SECRET} ]; then
    echo "Mon chiffre est plus petit"
  else
    echo "Mon chiffre est plus grand"
  fi
done

# executed after loop breaking
echo "Bravo ! Le chiffre secret à deviner était bien ${SECRET}"