import check50


@check50.check()
def exists():
    """odd.py exists"""
    check50.exists("odd.py")

@check50.check(exists)
def test1():
    """Check a small positive even number"""
    check50.run("python3 odd.py").stdin("2").stdout("Even\n").exit(0)

@check50.check(exists)
def test2():
    """Check a large positive even number"""
    check50.run("python3 odd.py").stdin("9999999999990").stdout("Even\n").exit(0)

@check50.check(exists)
def test3():
    """Check a small odd number"""
    check50.run("python3 odd.py").stdin("3").stdout("Odd\n").exit(0)

@check50.check(exists)
def test4():
    """Check a large odd number"""
    check50.run("python3 odd.py").stdin("9999999999999").stdout("Odd\n").exit(0)

@check50.check(exists)
def test5():
    """Check a negative even number"""
    check50.run("python3 odd.py").stdin("-10").stdout("Even\n").exit(0)

@check50.check(exists)
def test6():
    """Check a negative odd number"""
    check50.run("python3 odd.py").stdin("-11").stdout("Odd\n").exit(0)

@check50.check(exists)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("python3 cash.py").stdin("foo").reject()

@check50.check(exists)
def test_reject_empty():
    """rejects a non-numeric input of "" """
    check50.run("python3 cash.py").stdin("").reject()
