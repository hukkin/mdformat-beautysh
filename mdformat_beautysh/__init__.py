from beautysh import Beautify

__version__ = "0.1.1"  # DO NOT EDIT THIS LINE MANUALLY. LET bump2version UTILITY DO IT


def format_bash(unformatted: str, _info_str: str) -> str:
    result, err = Beautify().beautify_string(unformatted)
    if err:
        return unformatted
    return result
