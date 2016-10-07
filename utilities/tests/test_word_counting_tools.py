#! /usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

from utilities.word_counting_tools import check_ascii, remove_punctuation, make_counter

def compare(expected, result):
    if expected != result:
        print "Expected: {}, got {}".format(expected, result)
    assert expected == result 
     
def test_check_ascii_true():
    expected = True
    result = check_ascii("cat")
    compare(expected, result)

def test_check_ascii_false():
    expected = False
    result = check_ascii("новой")
    compare(expected, result)

def test_remove_punctuation():
    expected = "Hi how are you"
    result = remove_punctuation("Hi, how are you?")
    compare(expected, result)

    expected = "Hi Hello Yes"
    result = remove_punctuation("Hi (Hello), Yes!!")
    compare(expected, result)

def test_make_counter():
    expected = Counter({"hi": 1, "how": 1, "are": 1, "you": 1})
    result = make_counter("Hi, how are you\n")
    compare(expected, result)

def test_make_counter_int():
    expected = Counter({"hi": 2})
    result = make_counter("HI, hi, 123\n")
    compare(expected, result)
    
def test_make_counter_float():
    expected = Counter({"hi": 2})
    result = make_counter("hi, Hi, 1.23\n")
    compare(expected, result)
