import check50

@check50.check()
def exists():
    """andries.py exists."""
    check50.exists("andries.py")

@check50.check(exists)
def veronica():
    """calcultes a positive product."""
    check50.run("python3 andries.py").stdin("3").stdin("6").stdout("18").exit(0)

@check50.check(exists)
def brian():
    """calculates a negative product."""
    check50.run("python3 andries.py").stdin("2").stdin("-2").stdout("-4").exit(0)
