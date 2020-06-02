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
        try:
            assert int(value) == 1 or int(value) == 0
        except AssertionError:
            raise AssertionError("%s is not valid" % value)

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
        
       
class FullAdderCircuit(Circuit):
    input_names = ['A', 'B']
    output_names = ['S']

    def validate_input(self, value):
        return True

    def process(self, data):
        """The data have to contain binary digits as numbers.Binary (string like) object"""
        super(FullAdderCircuit, self).process(data)

        input1 = self.input_data.get('A')
        input2 = self.input_data.get('B')
        input1.equal_bits_length(input2)
        input2.equal_bits_length(input1)

        adderCircuit = None
        result = []

        input1.reverse()
        input2.reverse()

        for index in range(input1.len()):
            data = {'A': input1[index], 'B': input2[index]}
            if adderCircuit:
                data['Cin'] = adderCircuit.get('Cout')
            else:
                data['Cin'] = 0
            adderCircuit = AdderCircuit()
            adderCircuit.process(data)
            
            result.append(str(adderCircuit.get('S')))

        if adderCircuit:
            result.append(str(adderCircuit.get('Cout')))

        self.value = ''.join(result)
        return self.value

