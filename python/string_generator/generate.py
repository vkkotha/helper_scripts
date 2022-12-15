#!/usr/bin/env python

import logging, sys, os
import click
import functools

chars = 'abcdefghijklmnopqrstuvwxyz'
chars = chars + chars.upper() + '0123456789'
charsLen = len(chars)

ALG_BRUTE = 'BRUTE'
ALG_POS = 'POS'
out_file = None


@click.command()
@click.option('-l', '--len', default=0, required=True, type=click.IntRange(0, 64), help='string length to generate', show_default=True)
@click.option('-o', '--output', type=click.Path(exists=True), help='path location for generated files.', metavar='<dir>')
@click.option('-f', '--filter', is_flag=True, default=False, show_default=True, help='turn on filtering.')
@click.option('-mr', '--max-repeat', default=0, help='filter if character repeats more than this value. should be >0 to be active.')
@click.option('-mo', '--max-occurence', default=0, help='filter if chracter occurs anywhere in generated string, more than this value. should be > 0 to be active.')
@click.option('-alg', '--algorithm', default=ALG_BRUTE, show_default=True, type=click.Choice([ALG_BRUTE, ALG_POS]), help='choose algorithm to use to generate strings.')
def gen(len, output, filter, max_repeat, max_occurence, algorithm):
    """ 
    A all combination string generator.\n
    Generates string of given length, filtering out for repeats, occurences. 
    """
    logStartup(len, output, filter, max_repeat, max_occurence, algorithm)
    out_file = None

    if (output is not None):
        out_file = open(click.format_filename(output) + '/1.txt', 'w')

    processed_count = 0
    filtered_count = 0
    count = 0
    for s in generator(algorithm, len):
        if(s):
            processed_count += 1
            if (not filter or not filter_string(s, max_repeat, max_occurence)):
                count += 1
                write_string(s, out_file)
            else:
                filtered_count += 1

            if (processed_count % 1000000 == 0):
                print(". ", file=sys.stderr, end="")
                sys.stderr.flush()
                if (out_file is not None):
                    out_file.flush()

    if (out_file):
        out_file.close()
    
    logFinish(processed_count, filtered_count, count)

def logStartup(len, output, filter, max_repeat, max_occurence, algorithm):
    logging.info('Starging generation ...')
    logging.info('----------------------------------------------')
    logging.info(f'Python Version: {sys.version}')
    logging.info(f'CharCount: {charsLen}')
    logging.info(f'Length: {len}, Algorithm: {algorithm}')
    logging.info(f'Filter: {filter}, max-repeat: {max_repeat}, max-occurence: {max_occurence}')
    logging.info(f'Destination: {"stdout" if output is None else click.format_filename(output)}')
    logging.info('----------------------------------------------')

def logFinish(processed_count, filtered_count, count):
    logging.info(f'Finished: [processed: {processed_count} filtered: {filtered_count} generated: {count}]')

def generator(algorithm, n):
    if (algorithm == ALG_POS):
        yield from generator_pos(n)
    else:
        yield from generator_brute(n)

def generator_brute(len):
    if ( len < 1):
        return

    if (len == 1):
        for c in chars:
            yield c
    else:
        for cc in chars:
            for postStr in generator_brute(len-1):
                yield cc + postStr

def generator_pos(len):
    print(f'POS Generator {len}')
    yield None

def write_string(s, out_file):
    if (out_file is None):
        print(s)
    else:
        out_file.write(f'{s}\n')

def update_dictionary(dict, c):
    charCount = dict.setdefault(c, 0)
    dict[c] = charCount + 1

def value_over_threshold(dict, threshold):
    for v in dict.values():
        if (v > threshold):
            return True
    return False

def filter_string(str, max_repeat = 5, max_occurence = 12):
    if (max_repeat <=0 and max_occurence <=0 ):
        return False 
    
    strLen = len(str)
    if (strLen < 1):
        return True
    occrencesCountDict = {}
    
    pc = str[0]
    repeatCnt = 0

    for idx in range(0, strLen):
        c = str[idx]
        update_dictionary(occrencesCountDict, c)
        if (pc == c):
            repeatCnt += 1
        
        if (max_repeat > 0 and (repeatCnt > max_repeat) ):
            logging.debug(f'Filtering: {str} [RepeatCount Over Threshold {max_repeat}]')
            return True

        if (max_occurence > 0 and value_over_threshold(occrencesCountDict, max_occurence)):
            logging.debug(f'Filtering: {str} [OccurenceCount Over Threshold {max_occurence}')
            return True
        pc = c
        
    return False
    
def setupLogging():
    logLevel = logging.INFO
    if ('DEBUG' in os.environ and os.environ['DEBUG']):
        logLevel = logging.DEBUG
    logging.basicConfig(stream=sys.stderr, level=logLevel, format='%(message)s')

if __name__ == '__main__':
    setupLogging()
    gen()
