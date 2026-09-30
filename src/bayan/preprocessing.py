"""Bayan Arabic preprocessing entry point.

IMPORTANT:
This module is a project-owned entry point. Before final submission, run the
project notebooks against the actual Bayan artifacts and record the real
profile/version/test results in reports/.
"""

import re
import unicodedata

PROFILE_VERSION = "1.0.0"

_TATWEEL = "\u0640"
_DIACRITICS = re.compile(r"[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]")

def preprocess_arabic(text: str) -> str:
    """Normalize Arabic text without compatibility folding.

    The implementation reflects the documented smoke profile:
    Unicode normalization, tatweel/diacritic removal, and conservative
    Arabic letter folding. PII masking and display-copy preservation should
    be applied by the project pipeline where required.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = unicodedata.normalize("NFC", text)
    text = text.replace(_TATWEEL, "")
    text = _DIACRITICS.sub("", text)

    # Conservative folds documented in the supplied project material.
    text = text.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")
    text = text.replace("ى", "ي")

    return text
