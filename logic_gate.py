class LogicGate(object):
    _LOGICAL_VALUE_ZERO = 0
    _LOGICAL_VALUE_ONE = 1

    value = None

    def __str__(self):
        return self.value

    def process(self, *inputs):
        result = None
        for input_value in inputs:
            if result == None:
                result = input_value
            else:
                result = self.process_logic(result, input_value)
        self.value = result
        return result

    def process_logic(self, input1, input2):
        raise NotImplementedError()


class AndLogicGate(LogicGate):
    def process_logic(self, input1, input2):
        return self._LOGICAL_VALUE_ONE if input1 and input2 else self._LOGICAL_VALUE_ZERO

class OrLogicGate(LogicGate):
    def process_logic(self, input1, input2):
        return self._LOGICAL_VALUE_ONE if input1 or input2 else self._LOGICAL_VALUE_ZERO

class XorLogicGate(LogicGate):
    def process_logic(self, input1, input2):
        return self._LOGICAL_VALUE_ONE if (input1 or input2) and input1 != input2 else self._LOGICAL_VALUE_ZERO

