from beautysh import BashFormatter

__version__ = "0.1.1"  # DO NOT EDIT THIS LINE MANUALLY. LET bump2version UTILITY DO IT

# Instantiate the formatter.
# We can use the defaults, as mdformat doesn't pass options.
formatter = BashFormatter()


def format_bash(unformatted: str, _info_str: str) -> str:
    try:
        # Call the beautify_string method on the instance
        result, error = formatter.beautify_string(unformatted)
        if error:
            # If beautysh fails, return the original text
            return unformatted
        return result
    except Exception:
        # Fallback if beautysh fails unexpectedly
        return unformatted
