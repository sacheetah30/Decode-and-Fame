import pytest
from project import caesar_cipher, encrypt, provide_hint, actors_movies
def test_caesar_cipher():
    assert caesar_cipher("ABC", 1) == "BCD"
    assert caesar_cipher("XYZ", 3) == "ABC"
    assert caesar_cipher("abc", 2) == "cde"

def test_encrypt():
    assert encrypt("HELLO", 3) == "KHOOR"
    assert encrypt("world", 5) == "btwqi"

def test_provide_hint():
    # Test Case 1: When no letters have been guessed yet
    user_progress = "_____"
    quote = "Leonardo DiCaprio"
    actor_name = "Leonardo DiCaprio"
    movies = actors_movies[actor_name]
    
    hint = provide_hint(user_progress, quote, actor_name, movies)
    print(f"Test Case 1 - Hint when no letters are guessed: {hint}")

    # Test Case 2: When some letters have been guessed
    user_progress = "L__n__r_ _iC__rio"
    quote = "Leonardo DiCaprio"
    actor_name = "Leonardo DiCaprio"
    hint = provide_hint(user_progress, quote, actor_name, movies)
    print(f"Test Case 2 - Hint when some letters are guessed: {hint}")

    # Test Case 3: When all letters have been guessed
    user_progress = "Leonardo DiCaprio"
    quote = "Leonardo DiCaprio"
    actor_name = "Leonardo DiCaprio"
    hint = provide_hint(user_progress, quote, actor_name, movies)
    print(f"Test Case 3 - Hint when all letters are guessed: {hint}")

    # Test Case 4: When no hints are required (only showing message)
    user_progress = "Leonardo DiCaprio"
    quote = "Leonardo DiCaprio"
    actor_name = "Leonardo DiCaprio"
    hint = provide_hint(user_progress, quote, actor_name, movies)
    print(f"Test Case 4 - Hint when all letters are guessed correctly: {hint}")
    
    # Test Case 5: When user has guessed part of the quote
    user_progress = "_e__r__o _iC__rio"
    quote = "Leonardo DiCaprio"
    actor_name = "Leonardo DiCaprio"
    hint = provide_hint(user_progress, quote, actor_name, movies)
    print(f"Test Case 5 - Hint when part of the name is guessed: {hint}")

