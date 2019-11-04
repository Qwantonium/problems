import check50


@check50.check()
def exists():
    """cash.py exists"""
    check50.exists("cash.py")

@check50.check(exists)
def test041():
    """input of 0.4 yields output of 2"""
    check50.run("python3 cash.py").stdin("0.4").stdout(coins(2), "2\n").exit(0)

@check50.check(exists)
def test001():
    """input of 0.10 yields output of 1"""
    check50.run("python3 cash.py").stdin("0.10").stdout(coins(1), "1\n").exit(0)

@check50.check(exists)
def test015():
    """input of 0.40 yields output of 2"""
    check50.run("python3 cash.py").stdin("0.40").stdout(coins(2), "2\n").exit(0)

@check50.check(exists)
def test160():
    """input of 6.6 yields output of 5"""
    check50.run("python3 cash.py").stdin("6.6").stdout(coins(5), "5\n").exit(0)

@check50.check(exists)
def test230():
    """input of 23 yields output of 13"""
    check50.run("python3 cash.py").stdin("23").stdout(coins(13), "13\n").exit(0)

@check50.check(exists)
def test420():
    """input of 12.95 yields output of 10"""
    from re import search
    expected = "10\n"
    actual = check50.run("python3 cash.py").stdin("4.2").stdout()
    if not search(coins(10), actual):
        help = None
        if search(coins(9), actual):
            help = "did you forget to give 10c if 5c is owing?"
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
