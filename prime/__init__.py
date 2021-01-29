import check50


@check50.check()
def exists():
    """prime.py exists"""
    check50.exists("prime.py")

@check50.check(exists)
def test041():
    """input of 2 yields output of Prime"""
    output = check50.run("python3 prime.py").stdin("2").stdout()
    if not output == "Prime\n":
        raise check50.Failure("Expected Prime, received ", output)

@check50.check(exists)
def test001():
    """input of 3 yields output of Prime"""
    output = check50.run("python3 prime.py").stdin("3").stdout()
    if not output == "Prime":
        raise check50.Failure("Expected Prime, received ", output)

@check50.check(exists)
def test015():
    """input of 4 yields output of Not Prime"""
    output = check50.run("python3 prime.py").stdin("4").stdout()
    if not output == "Not Prime":
        raise check50.Failure("Expected Prime, received ", output)

@check50.check(exists)
def test160():
    """input of 13 yields output of Prime"""
    output = check50.run("python3 prime.py").stdin("13").stdout()
    if not output == "Prime":
        raise check50.Failure("Expected Prime, received ", output)

@check50.check(exists)
def test10007():
    """input of 10007 yields output of Prime"""
    output = check50.run("python3 prime.py").stdin("10007").stdout()
    if not output == "Prime":
        raise check50.Failure("Expected Prime, received ", output)

@check50.check(exists)
def test1000000():
    """input of 1000000 yields output of Not Prime"""
    output = check50.run("python3 prime.py").stdin("1000000").stdout()
    if not output == "Not Prime":
        raise check50.Failure("Expected Prime, received ", output)
    
@check50.check(exists)
def test_reject_fraction():
    """rejects a fraction input"""
    check50.run("python3 prime.py").stdin("12.95").reject()

@check50.check(exists)
def test_reject_negative():
    """rejects a negative input like -1"""
    check50.run("python3 prime.py").stdin("-50").reject()

@check50.check(exists)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("python3 prime.py").stdin("foo").reject()

@check50.check(exists)
def test_reject_empty():
    """rejects a non-numeric input of "" """
    check50.run("python3 prime.py").stdin("").reject()


def coins(num):
    return fr"(^|[^\d]){num}(?!\d)"