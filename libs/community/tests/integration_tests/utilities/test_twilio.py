"""Integration test for Sms."""

from aiagentsforce_community.utilities.twilio import TwilioAPIWrapper


def test_call() -> None:
    """Test that call runs."""
    twilio = TwilioAPIWrapper()  # type: ignore[call-arg]
    output = twilio.run("Message", "+16162904619")
    assert output
