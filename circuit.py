from .logic_gate import AndLogicGate, OrLogicGate, XorLogicGate


class Circuit(object):
    """Contains one or more logic gates and pre defined inputs"""
    input_names = []
    input_data = {}
    output_names = []
    output_data = {}

    def set(self, key, value):
        self.output_data[key] = value

    def get(self, key, default=None):
        return self.output_data.get(key, default)

    def validate_input(self, value):
        assert value == 1 or value == 0

    def validate_inputs(self):
        """Validate if the input_data contains all data and if it is 0 or 1"""
        for input_name in self.input_names:
            self.validate_input(self.input_data.get(input_name))

    def process(self, data):
        self.input_data = data
        self.validate_inputs()


class AdderCircuit(Circuit):
    input_names = ['A', 'B', 'Cin']
    output_names = ['S', 'Cout']

    def process(self, data):
        super(AdderCircuit, self).process(data)

        and1 = AndLogicGate()
        and2 = AndLogicGate()
        xor1 = XorLogicGate()
        xor2 = XorLogicGate()
        or1 = OrLogicGate()

        xor1.process(self.input_data['A'], self.input_data['B'])
        and2.process(self.input_data['A'], self.input_data['B'])

        self.output_data['S'] = xor2.process(xor1.value, self.input_data['Cin'])
        and1.process(xor1.value, self.input_data['Cin'])

        self.output_data['Cout'] = or1.process(and1.value, and2.value)
        
        
