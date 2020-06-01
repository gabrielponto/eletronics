#!/usr/bin/python
from .logic_gate import AndLogicGate, OrLogicGate, XorLogicGate
from .circuit import AdderCircuit, FullAdderCircuit
from .numbers import Decimal, Binary


class LogicGatesTest(object):
    def test_and_logic_gate(self):
        lg = AndLogicGate()
        assert 1 == lg.process(1, 1)
        assert 0 == lg.process(0, 0)
        assert 0 == lg.process(0, 1)
        assert 0 == lg.process(1, 0)

        assert 1 == lg.process(1, 1, 1, 1, 1)
        assert 0 == lg.process(0, 1, 0, 1, 0)
        assert 0 == lg.process(1, 0, 1, 1, 1)

    def test_or_logic_gate(self):
        lg = OrLogicGate()
        assert 0 == lg.process(0, 0)
        assert 1 == lg.process(0, 1)
        assert 1 == lg.process(1, 0)
        assert 1 == lg.process(1, 1)

        assert 0 == lg.process(0, 0, 0, 0, 0)
        assert 1 == lg.process(0, 0, 1, 0, 1)
        assert 1 == lg.process(1, 0, 0, 0, 1)
        assert 1 == lg.process(0, 0, 0, 1, 0)

    def test_xor_logic_gate(self):
        lg = XorLogicGate()
        assert 0 == lg.process(0, 0)
        assert 1 == lg.process(0, 1)
        assert 1 == lg.process(1, 0)
        assert 0 == lg.process(0, 0)


class AdderCircuitTest(object):
    def test_adder(self):
        adder = AdderCircuit()
        adder.process({
            'A': 1,
            'B': 1,
            'Cin': 1
        })

        assert adder.get('S') == 1
        assert adder.get('Cout') == 1

        adder.process({
            'A': 1,
            'B': 0,
            'Cin': 0
        })

        assert adder.get('S') == 1
        assert adder.get('Cout') == 0


class NumbersTest(object):
    def test_binary_convert(self):
        decimal = Decimal(100)
        assert decimal.convert_to_binary().value == '1100100'

        decimal = Decimal(7)
        assert decimal.convert_to_binary().value == '111'


class FullAdderCircuitTest(object):
    def test_full_adder(self):
        full_adder = FullAdderCircuit()
        full_adder.process({'A': Binary(4), 'B': Binary(7)})
        print("The result was: %s" % full_adder.value)
        assert full_adder.value == '1011'


logic_gates_test = LogicGatesTest()
logic_gates_test.test_and_logic_gate()
logic_gates_test.test_or_logic_gate()
logic_gates_test.test_xor_logic_gate()

adder_circuit_test = AdderCircuitTest()
adder_circuit_test.test_adder()

number_test = NumbersTest()
number_test.test_binary_convert()

full_adder_test = FullAdderCircuitTest()
full_adder_test.test_full_adder()

print("[OK] All tests are passed!")
