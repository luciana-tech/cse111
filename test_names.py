from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    # Test cases
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("John", "Doe") == "Doe; John"
    assert make_full_name("Alice", "Smith") == "Smith; Alice"
    assert make_full_name("Bob", "O'Reilly") == "O'Reilly; Bob"
    assert make_full_name("Anna", "Lee") == "Lee; Anna"
    
    print("All tests passed!")

test_make_full_name()

def test_extract_family_name():
    # Test cases
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Doe; John") == "Doe"
    assert extract_family_name("Smith; Alice") == "Smith"
    assert extract_family_name("O'Reilly; Bob") == "O'Reilly"
    assert extract_family_name("Lee; Anna") == "Lee"
    
    print("All tests passed!")

test_make_full_name()
test_extract_family_name()