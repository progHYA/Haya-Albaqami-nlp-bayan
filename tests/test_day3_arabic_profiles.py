import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from bayan.preprocessing import PROFILE_VERSION, preprocess_arabic

def test_profile_version():
    assert PROFILE_VERSION == "1.0.0"

def test_arabic_profile_normalization():
    text = "أَحْمَـدَى"
    assert preprocess_arabic(text) == "احمدي"

def test_non_string_rejected():
    try:
        preprocess_arabic(None)
    except TypeError:
        return
    raise AssertionError("Expected TypeError for non-string input")
