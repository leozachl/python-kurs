import steuer
import pytest

def test():
    assert round(steuer.einkommenssteuer(40000),2) == 10080.00
    assert round(steuer.einkommenssteuer(11001),2) == 0.25
    assert round(steuer.einkommenssteuer(18000), 2) == 1750.00
    assert round(steuer.einkommenssteuer(18001), 2) == 1750.35
    assert round(steuer.einkommenssteuer(31000), 2) == 6300.00
    assert round(steuer.einkommenssteuer(31001), 2) == 6300.42
    assert round(steuer.einkommenssteuer(60000), 2) == 18480.00
    assert round(steuer.einkommenssteuer(60001), 2) == 18480.48
    assert round(steuer.einkommenssteuer(90000), 2) == 32880.00
    assert round(steuer.einkommenssteuer(90001), 2) == 32880.50
    assert round(steuer.einkommenssteuer(1000000), 2) == 487880.00
    assert round(steuer.einkommenssteuer(1000001), 2) == 487880.55


