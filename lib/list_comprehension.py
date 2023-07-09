#!/usr/bin/env python3

def return_evens(num_list):
    even_elements = [s for s in num_list if s % 2 == 0]
    return even_elements

def make_exclamation(sentence_list):
    add_exclamation = [s + '!' for s in sentence_list]
    return add_exclamation