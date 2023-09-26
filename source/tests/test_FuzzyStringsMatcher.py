import pytest
from searching.FuzzyStringsMatcher import FuzzyStringsMatcher

@pytest.fixture
def not_ignore_cases_matcher():
    return FuzzyStringsMatcher(ratio=0.5, ignore_cases=False)


@pytest.fixture
def ignore_cases_matcher():
    return FuzzyStringsMatcher(ratio=0.5, ignore_cases=True)


def test_calculate_similarity_ignore_cases(ignore_cases_matcher):
    assert ignore_cases_matcher.calculate_similarity("Lewandowski", "LEWANDOWSKI")==1
    assert ignore_cases_matcher.calculate_similarity("Lewandowski", "DEWANDOWSKI")>0
    assert ignore_cases_matcher.calculate_similarity("AAAA", "BBB")==0

def test_calculate_similarity_not_ignore_cases(not_ignore_cases_matcher):
    assert not_ignore_cases_matcher.calculate_similarity("Lewandowski", "Lewandowski")==1
    assert not_ignore_cases_matcher.calculate_similarity("Lewandowski", "DEWANDOWSKI")==0
    assert not_ignore_cases_matcher.calculate_similarity("AAAA", "aaaa")==0
    assert not_ignore_cases_matcher.calculate_similarity("AAAA", "BBB")==0

def test_are_similar_ignore_cases(ignore_cases_matcher):
    assert ignore_cases_matcher.are_similar("Lewandowski", "LEWANDOWSKI")
    assert ignore_cases_matcher.are_similar("Lewandowski", "DEWANDOWSKI")
    assert ignore_cases_matcher.are_similar("AAAA", "BBB") is False

def test_are_similar_not_ignore_cases(not_ignore_cases_matcher):
    assert not_ignore_cases_matcher.are_similar("Lewandowski", "Lewandowski") 
    assert not_ignore_cases_matcher.are_similar("Lewandowski", "DEWANDOWSKI") is False
    assert not_ignore_cases_matcher.are_similar("AAAA", "aaaa") is False
    assert not_ignore_cases_matcher.are_similar("AAAA", "BBB") is False

def test_contains_word_ignore_cases(ignore_cases_matcher):
    assert ignore_cases_matcher.contains_word("Lewandowski scores","SCORE")
    assert ignore_cases_matcher.contains_word("Lewandowski scores","LEWENDOWSKI")
    assert ignore_cases_matcher.contains_word("Lewandowski scores","score")
    assert ignore_cases_matcher.contains_word("Lewandowski scores","lewendowski")

def test_contains_word_not_ignore_cases(not_ignore_cases_matcher):
    assert not_ignore_cases_matcher.contains_word("Lewandowski scores","SCORE") is False
    assert not_ignore_cases_matcher.contains_word("Lewandowski scores","LEWENDOWSKI") is False
    assert not_ignore_cases_matcher.contains_word("Lewandowski scores","score")
    assert not_ignore_cases_matcher.contains_word("Lewandowski scores","Lewendowski") 

def test_contains_substring_not_ignore_cases(not_ignore_cases_matcher):
    assert not_ignore_cases_matcher.contains_substring("Robert Lewandowski", "ewandowsky")
    assert not_ignore_cases_matcher.contains_substring("Robert Lewandowski", "EWANDOwskY") is False
    assert not_ignore_cases_matcher.contains_substring("Robert Lewandowski", "OBERT") is False
    assert not_ignore_cases_matcher.contains_substring("Robert Lewandowski", "obert")
    assert not_ignore_cases_matcher.contains_substring("Robert Lewandowski", "XXXXXX") is False

def test_contains_substring_ignore_cases(ignore_cases_matcher):
    assert ignore_cases_matcher.contains_substring("Robert Lewandowski", "ewAnDOwskY")
    assert ignore_cases_matcher.contains_substring("Robert Lewandowski", "OBERT") 
    assert ignore_cases_matcher.contains_substring("Robert Lewandowski", "ewandowsky")
    assert ignore_cases_matcher.contains_substring("Robert Lewandowski", "obert") 
    assert ignore_cases_matcher.contains_substring("Robert Lewandowski", "XXXXXX") is False