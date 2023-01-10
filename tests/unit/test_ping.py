from eat_it.app import ping

UNIMPLEMENTED = 501


def test_ping_returns_501_response() -> None:
    result = ping()
    assert result.status_code == UNIMPLEMENTED
