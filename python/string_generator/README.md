# Simple String Generator

This script generates words of fixed length.  

Uses a-zA-Z0-9 characters to generate words of all comibinations.  
You can used it to generate word files which you can feed to [hashcat](https://hashcat.net/hashcat/) for carking passwords.  


## Usage

Run help to see usage.  
>     $ ./generator.py --help

## Examples
1. generate words of length 5. So specify output folder location with -o. file will be generate at output/1.txt
        
    >     $ mkdir -o output
    >     $ ./generator.py -l 5 -o output
1. genreate words of length 4, turn on filter to filter out words that had 2 occrences of the same chacater repeating one after another.
    >     $ ./generator.py -l 5 --filter -mr 3
1. genreate words of length 5, turn on filter to filter out words that had 3 occrences of the same chacater any where in the string.
    >     $ ./generator.py -l 5 --filter -mo 3
1. generate a 32 character string with repeat filter, and see some output while running. This is for experiment, don't let this run for long.
    >     $ ./generator.py -l 32 --filter -mr 28 -o output

## Notes
- This is a experiment to produce large strings with large combinations.
- Futher work need to optimize generation and filtering logic.

## Limitations
- If you generate a string of length 5, with 62 character set, then it will generate 32^5 = 916,132,832. Each string is 5 Bytes, so your file size will be around 4.6 GB. This exponentilly grows with each extra character.
Geneating all combinations 32 char string, Will generate 64^32 = 2.27 x e57. This is a  58 digit number. Storing all this requires 2.27 x e33 Yotta Bytes (10^24)
- Filtering on large numbers is also going to be slow, as each string generated need to be checked for occurrences, repeates, so you may not see any results for a while in the output file.

## TODO
- implement faster generation/filtering
- options to stop the program after generating, n strings.