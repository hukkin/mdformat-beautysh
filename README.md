[![Build Status](https://github.com/hukkinj1/mdformat-beautysh/workflows/Tests/badge.svg?branch=master)](<https://github.com/hukkinj1/mdformat-beautysh/actions?query=workflow%3ATests+branch%3Amaster+event%3Apush>)
[![PyPI version](https://badge.fury.io/py/mdformat-beautysh.svg)](<https://badge.fury.io/py/mdformat-beautysh>)

# mdformat-beautysh
> Mdformat plugin to beautify Bash scripts

## Description
mdformat-beautysh is an [mdformat](https://github.com/executablebooks/mdformat) plugin
that makes mdformat format Bash scripts with [Beautysh](https://github.com/lovesegfault/beautysh).
## Usage
Install with:
```bash
pip install mdformat-beautysh
```

When using mdformat on the command line, Beautysh formatting will be automatically enabled after install.

When using mdformat Python API, code formatting for Bash scripts will have to be enabled explicitly:
```python
import mdformat


unformatted = """~~~bash
function bad_func()
 {
echo "test"
}
~~~
"""

formatted = mdformat.text(unformatted, codeformatters={"bash", "sh"})

assert formatted == """~~~bash
function bad_func()
{
    echo "test"
}
~~~
"""
```
