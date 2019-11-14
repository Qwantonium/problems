import check50

@check50.check()
def exists():
    """hello.py exists."""
    check50.exists("helloname.py")

@check50.check(exists)
def veronica():
    """responds to name James."""
    check50.run("python3 helloname.py").stdin("James").stdout("James").exit(0)

@check50.check(exists)
def brian():
    """responds to name Phoebe."""
    check50.run("python3 helloname.py").stdin("Phoebe").stdout("Phoebe").exit(0)
