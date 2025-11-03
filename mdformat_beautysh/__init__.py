from beautysh import BashFormatter

__version__ = "1.0.0"  # DO NOT EDIT THIS LINE MANUALLY. LET bump2version UTILITY DO IT

formatter = BashFormatter()


def format_bash(unformatted: str, _info_str: str) -> str:
    result, error = formatter.beautify_string(unformatted)
    if error:
        return unformatted
    return result
