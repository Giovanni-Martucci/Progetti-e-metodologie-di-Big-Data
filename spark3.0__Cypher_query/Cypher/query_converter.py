#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def translate_neo4j_to_cypher(query):
    
    # Check input format.
    try:  
        f_pattern, middle_pattern = query.split('*')
    except:
        return "[*] - ERROR INPUT!"

    # Add ']' for right sintax
    f_pattern += ']'
    
    # Cont the ':' occurences; used it for manipulate format string
    occor = [m.start() for m in re.finditer(':', f_pattern)]
    first_pattern = "{}{}{}".format(f_pattern[:occor[1]], 'r', f_pattern[occor[1]:])

    numbers, second_pattern = middle_pattern.split(']')
    num_1 = numbers[0]
    # Check number for iterate algorithm
    num_2 = numbers[len(numbers)-1]

    result = first_pattern + second_pattern
    sott = 0
    for i in range(int(num_2)-1):
        result += '\n\t\t  ' + first_pattern[:occor[1]+1] + str(i-sott) + first_pattern[occor[1]+1:]
        for j in range(i+1):
            occor = [m.start() for m in re.finditer(':', f_pattern)]
            pattern = "->(n" + str(i-sott+j) + ")-[r" + str(i-sott+j+1) + f_pattern[occor[1]:]
            result += pattern 
        result += second_pattern
        sott+=1


    return result


def main():
    while True:

        # Get input.
        while True:
            original_query = input('[*] - Inserisci query da convertire: ')
            confirm = input('- 1 <-- Conferma\n- 2 <-- Ricarica\n>> ')
            if confirm == '1':
                break
        
        # Input converting...
        result = translate_neo4j_to_cypher(original_query)
        print('\n\t###############################\n\t° INPUT: {}\n\n\t° OUTPUT: {} \n\t###############################'.format(original_query, result))
        
        another_query = input('\n- 1 <-- Convert again\n- 2 <-- Exit\n>> ')
        if another_query == '2':
            break

    return 0

if __name__ == "__main__":
    main()