from beautysh import Beautify

__version__ = "0.0.0"  # DO NOT EDIT THIS LINE MANUALLY. LET bump2version UTILITY DO IT


def format_bash(unformatted: str) -> str:
    result, err = Beautify().beautify_string(unformatted)
    if err:
        return unformatted
    return result
