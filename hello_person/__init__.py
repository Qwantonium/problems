import check50

@check50.check()
def exists():
    """hello.py exists."""
    check50.exists("hello.py")

@check50.check(exists)
def veronica():
    """responds to name James."""
    check50.run("python3 hello.py").stdin("James").stdout("James").exit(0)

@check50.check(exists)
def brian():
    """responds to name Phoebe."""
    check50.run("python3 hello.py").stdin("Phoebe").stdout("Phoebe").exit(0)
