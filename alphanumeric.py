def alphanumeric(password):

    if len(password) < 1:
        return False

    for c in password:
        if not c.isalnum():
            return False
    return True

def test_():
    tests = [
        ("hello world_", False),
        ("PassW0rd", True),
        ("     ", False)
    ]

    for s, b in tests:
        assert alphanumeric(s) == b