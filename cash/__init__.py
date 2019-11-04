import check50


@check50.check()
def exists():
    """cash.py exists"""
    check50.exists("cash.py")

@check50.check(exists)
def test041():
    """input of 0.41 yields output of 3"""
    check50.run("python3 cash.py").stdin("0.41").stdout(coins(3), "3\n").exit(0)

@check50.check(exists)
def test001():
    """input of 0.01 yields output of 1"""
    check50.run("python3 cash.py").stdin("0.01").stdout(coins(1), "1\n").exit(0)

@check50.check(exists)
def test015():
    """input of 0.15 yields output of 2"""
    check50.run("python3 cash.py").stdin("0.15").stdout(coins(2), "2\n").exit(0)

@check50.check(exists)
def test160():
    """input of 1.6 yields output of 3"""
    check50.run("python3 cash.py").stdin("1.6").stdout(coins(3), "3\n").exit(0)

@check50.check(exists)
def test230():
    """input of 23 yields output of 13"""
    check50.run("python3 cash.py").stdin("23").stdout(coins(13), "13\n").exit(0)

@check50.check(exists)
def test420():
    """input of 4.25 yields output of 4"""
    from re import search
    expected = "4\n"
    actual = check50.run("python3 cash.py").stdin("4.25").stdout()
    if not search(coins(4), actual):
        help = None
        if search(coins(3), actual):
            help = "did you forget to round your input to the nearest cent?"
        raise Mismatch(expected, actual, help=help)

@check50.check(exists)
def test_reject_negative():
    """rejects a negative input like -1"""
    check50.run("python3 cash.py").stdin("-1").reject()

@check50.check(exists)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("python3 cash.py").stdin("foo").reject()

@check50.check(exists)
def test_reject_empty():
    """rejects a non-numeric input of "" """
    check50.run("python3 cash.py").stdin("").reject()


def coins(num):
    return fr"(^|[^\d]){num}(?!\d)"
