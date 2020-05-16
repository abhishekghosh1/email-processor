import talon

talon.init()

from talon import signature


def remove_signature(message, sender):
    text, _signature = signature.extract(message, sender)
    return text
