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
