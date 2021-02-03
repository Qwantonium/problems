import check50


@check50.check()
def exists():
    """prime-n.py exists"""
    check50.exists("prime-n.py")

@check50.check(exists)
def test002():
    """input of 2 yields 2nd prime number (3)"""
    check50.run("python3 prime-n.py").stdin("2").stdout("3")
   

@check50.check(exists)
def test003():
    """input of 3 yields 3rd prime number (3)"""
    check50.run("python3 prime-n.py").stdin("3").stdout("5")

@check50.check(exists)
def test004():
    """input of 4 yields 4th prime number (3)"""
    check50.run("python3 prime-n.py").stdin("4").stdout("7")

@check50.check(exists)
def test013():
    """input of 6 yields 6th prime number (3)"""
    check50.run("python3 prime-n.py").stdin("6").stdout("13")

@check50.check(exists)
def test412():
    """input of 412 yields 412th prime number"""
    check50.run("python3 prime-n.py").stdin("412").stdout("2837")

   
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
