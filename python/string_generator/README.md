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

## Algorithms

**BRUTE**  
If the length is 2 and charset is [a,b,c], It need to generate aa, ab, ac, ba, bb, bc, ca, cb, cc  

So it starts at first left position for each character, and concatenates all generated combinations for length = 1, which are just a, b, c.  

So this aplies to any length, for length 3, for each it's a Cross join of [a,b, c] * [all combinates of length 2]

**MATH**  
This on uses a simple math. If the length of charset is 3, [a,b,c] and string length that need to be generate is 2. Then we have to generate 3^2 strings.  

So we will be generating these [0: aa, 1: ab, 2: ac, 3: ba, 4: bb, 5: bc, 6: ca, 7: cb, 8: cc] 

If we treat those as 0-8 strings, you can translate each of those numbers to base of 3.  
0 is converted to [0, 0]  
1 is converted to [0, 1]  
5 is converted to [1, 2]  = ( 1*3<sup>1</sup> + 2\*3<sup>0</sup>)  

All these are Index positions in charter set, so when you look up you will get  
For 0: [0, 0]: [a, a]  
For 5: [1, 2]: [b, c]  


## Notes
- This is a experiment to produce large strings with large combinations.
- Futher work need to optimize generation and filtering logic.

## Limitations
- If you generate a string of length 5, with 62 character set, then it will generate 32^5 = 916,132,832. Each string is 5 Bytes, so your file size will be around 4.6 GB. This exponentilly grows with each extra character.
Geneating all combinations 32 char string, Will generate 64^32 = 2.27 x e57. This is a  58 digit number. Storing all this requires 2.27 x e33 Yotta Bytes, where each Yotta Byte is  (10^12 TerraBytes, That's 1 Trillion 1TB Disks.)
- Filtering on large numbers is also going to be slow, as each string generated need to be checked for occurrences, repeates, so you may not see any results for a while in the output file.

## TODO
- implement faster generation/filtering
- options to stop the program after generating, n strings.
- Generate multiple files, with some parrallel processing.
- Generate all lenghts below the given length.
- Experment with writing first level strings to a file, and use it to generate nexte level.