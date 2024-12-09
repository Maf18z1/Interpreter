import os
import xml.etree.ElementTree as ET
from Confmg4 import assemble, interpret

def validate_output(output_path, expected):
    tree = ET.parse(output_path)
    root = tree.getroot()
    memory = {}
    for memory_entry in root.findall("memory"):
        addr = int(memory_entry.find("address").text)
        value = int(memory_entry.find("value").text)
        memory[addr] = value
    return memory == expected

def test_xor_operation():
    vector = [34, 45, 56, 78, 89, 123, 200, 255]
    xor_value = 156
    expected_result = {i: val ^ xor_value for i, val in enumerate(vector)}
    print(expected_result)

    # ��������� �����
    input_file = "Test.txt"
    log_file = "log.xml"
    output_file = "output.xml"

    # �������� �������� �����
    with open(input_file, "w") as f:
        for i, val in enumerate(vector):
            f.write(f"2 {val}\n")       # Load constant (vector value)
            f.write(f"2 {xor_value}\n") # Load constant (XOR value)
            f.write(f"4 {i}\n")         # XOR operation, save result at address i
    
    # ���������� ���������� � ��������������
    assemble(input_file, log_file)
    interpret(log_file, output_file)

    # �������� ����������
    assert validate_output(output_file, expected_result), "XOR operation test failed!"

    # �������� ��������� ������ (�����������)
    os.remove(log_file)
    os.remove(output_file)
