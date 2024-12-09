import sys
import xml.etree.ElementTree as ET

class VirtualMachine:
    def __init__(self):
        self.stack = []
        self.memory = {}

    def execute_instruction(self, opcode, operand=None):
        print(self.stack, self.memory)
        if opcode == 2:  # Load constant
            self.stack.append(operand)
        elif opcode == 7:  # Read from memory
            if not self.stack:
                addr = 0
            else:
                addr = self.stack.pop() 
            self.stack.append(self.memory.get(addr, 0))
        elif opcode == 6:  # Write to memory
            if not self.stack:
                raise IndexError(
                    f"Stack is empty. Cannot execute 'write to memory'. Current stack: {self.stack}"
                )
            addr = self.stack.pop() + operand 
            self.memory[addr] = addr
        elif opcode == 4:  # XOR operation
            if len(self.stack) < 2:
                raise IndexError(
                    f"Stack has fewer than 2 elements. Cannot execute 'XOR'. Current stack: {self.stack}"
                )
            op1 = self.stack.pop()
            op2 = self.stack.pop()
            addr = operand
            self.memory[addr] = op1 ^ op2
        else:
            raise ValueError(f"Unknown opcode: {opcode}")

def assemble(input_path, log_path):
    root = ET.Element("log")
    with open(input_path, "r") as f:
        lines = f.readlines()
    for line in lines:
        parts = line.split()
        opcode = int(parts[0])
        operand = int(parts[1]) if len(parts) > 1 else None
        instruction = ET.SubElement(root, "instruction")
        ET.SubElement(instruction, "opcode").text = str(opcode)
        ET.SubElement(instruction, "operand").text = str(operand) if operand is not None else "None"
    tree = ET.ElementTree(root)
    tree.write(log_path)

def interpret(log_path, output_path):
    tree = ET.parse(log_path)
    root = tree.getroot()
    vm = VirtualMachine()
    for instruction in root.findall("instruction"):
        opcode = int(instruction.find("opcode").text)
        operand_text = instruction.find("operand").text
        operand = int(operand_text) if operand_text != "None" else None
        try:
            vm.execute_instruction(opcode, operand)
        except Exception as e:
            print(f"Error while executing instruction {opcode}, operand {operand}: {e}")
            raise
    output = ET.Element("output")
    for addr, value in sorted(vm.memory.items()):
        memory_entry = ET.SubElement(output, "memory")
        ET.SubElement(memory_entry, "address").text = str(addr)
        ET.SubElement(memory_entry, "value").text = str(value)
    tree = ET.ElementTree(output)
    tree.write(output_path)

if __name__ == "__main__":
    input_path = sys.argv[1]
    log_path = sys.argv[2]
    output_path = sys.argv[3]
    assemble(input_path, log_path)
    interpret(log_path, output_path)


