from nose.tools import *
from source import foo

def test_foo_returns_correct_greeting():
    myFoo = foo.foo()
    assert_equal("Hello World.", myFoo.getGreeting())