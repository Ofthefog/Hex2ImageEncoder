#!/bin/bash

source config.sh

cringfunctionformyfailinput()
{
   echo ""
   echo "Usage: $0 -m mode -i file -o file.png"
   echo -e "\t-m Define which mode ( 'greyscale' or 'enhanced' )"
   echo -e "\t-i Define input file to transform to an image"
   echo -e "\t-o Define the name of the output png image"
   exit 1 # Something went wrong!!!1one 
}

while getopts "m:i:o:" opt
do
   case "$opt" in
      m ) M="$OPTARG" ;;
      i ) I="$OPTARG" ;;
      o ) O="$OPTARG" ;;
      ? ) cringfunctionformyfailinput ;;
   esac
done

# Check if we have all of the requirements
if [ -z "$M" ] || [ -z "$I" ] || [ -z "$O" ]
then
   echo "All 3 parameters are required";
   cringfunctionformyfailinput
fi

# Check if mode is valid

if [[ ! "$M" = "greyscale" ]] && [[ ! "$M" = "enhanced" ]]; then
   echo "valid modes are 'grayscale' and 'enhanced'"
   exit 1
fi

# Check if input file is there

if [[ ! -f $I ]]; then
   echo "Input file $I does not exist"
   exit 1
fi

# Now we will check if the reserved file names are being used
# Also give a prompt if the user wants to change config to ignore this check

if [[ $overwrite != true ]]; then
  if [[ -f hexin.txt ]] || [[ -f hexout.txt ]] || [[ -f out.png ]]; then
    echo "Reserved file name ( hexin.txt , hexout.txt , or out.png ) detected!"
    read -p "Overwrite(Y/N)?:" hmm
 
    if [[ $hmm != "Y" ]] && [[ $hmm != "y" ]]; then
 	echo "Aborting" 
	exit 0 # presumedly if you typed this in then you'd know what happened
    fi 

    echo "Ah, okay. Do you want to skip this check next time and just overwrite?"
    
    read -p "Yes, configure this to skip, or No just overwrite this one time (Y/N)?:" hmm

    if [[ $hmm != "Y" ]] && [[ $hmm != "y" ]]; then
 	
     echo "Just overwriting once, then"
    else

	echo "Changing config file" 
	sed -i 's/overwrite=false/overwrite=true/' config.sh
    

    fi 

  fi
fi 

# Now let's actually setup the input so we can run this python

xxd -p $I | tr -d "\n" > hexin.txt

if [[ $M = "grayscale" ]]; then
 python hex2image.py
 python image2hex.py
fi

#enhanced is not fully implemented at the moment ( endianess problem )

if [[ $M = "enhanced" ]]; then
 python ehex2image.py
 python eimage2hex.py
fi

if [[ $overwrite != true ]]; then
 
fi


echo "$M"
echo "$I"
echo "$O"

