#!/usr/bin/python
from .logic_gate import AndLogicGate, OrLogicGate, XorLogicGate
from .circuit import AdderCircuit


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


logic_gates_test = LogicGatesTest()
logic_gates_test.test_and_logic_gate()
logic_gates_test.test_or_logic_gate()
logic_gates_test.test_xor_logic_gate()

adder_circuit_test = AdderCircuitTest()
adder_circuit_test.test_adder()

print("[OK] All tests are passed!")
