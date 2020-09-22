import mdformat

import mdformat_beautysh


def test_format_beautysh():
    unformatted = """function dummyfunc()
                         {
local mytest=4
 }
"""
    formatted = """function dummyfunc()
{
    local mytest=4
}
"""
    assert mdformat_beautysh.format_bash(unformatted) == formatted


def test_mdformat_integration():
    unformatted_md = """```sh
function func1()
{
\techo "test"
  }
```
"""
    formatted_md = """~~~sh
function func1()
{
    echo "test"
}
~~~
"""
    assert mdformat.text(unformatted_md, codeformatters={"sh"}) == formatted_md
