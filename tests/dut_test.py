import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer
from cocotb.result import TestFailure
import xml.etree.ElementTree as ET

# Address map constants
A_STATUS = 0
B_STATUS = 1
Y_STATUS = 2
Y_OUTPUT = 3
A_DATA = 4
B_DATA = 5

async def reset_dut(dut):
    """Reset the DUT"""
    dut.RST_N.value = 0
    await Timer(20, units="ns")
    dut.RST_N.value = 1
    await Timer(20, units="ns")

async def write_data(dut, address, data):
    """Write data to the specified address"""
    await RisingEdge(dut.CLK)
    dut.write_address.value = address
    dut.write_data.value = data
    dut.write_en.value = 1
    await RisingEdge(dut.CLK)
    dut.write_en.value = 0

async def read_data(dut, address):
    """Read data from the specified address"""
    await RisingEdge(dut.CLK)
    dut.read_address.value = address
    dut.read_en.value = 1
    await RisingEdge(dut.CLK)
    await RisingEdge(dut.CLK)  # Wait for read_rdy
    data = dut.read_data.value
    dut.read_en.value = 0
    return data

@cocotb.test()
async def test_xor_gate(dut):
    """Test the XOR gate functionality"""
    # Start clock
    clock = Clock(dut.CLK, 10, units="ns")
    cocotb.start_soon(clock.start())

    # Initialize signals
    dut.read_en.value = 0
    dut.write_en.value = 0
    dut.read_address.value = 0
    dut.write_address.value = 0
    dut.write_data.value = 0

    # Reset DUT
    await reset_dut(dut)

    # XML root for results
    results = ET.Element("test_results")

    # Test case 1: 0 XOR 0 = 0
    await write_data(dut, A_DATA, 0)
    await write_data(dut, B_DATA, 0)
    output = await read_data(dut, Y_OUTPUT)
    expected = 0
    test_pass = (output == expected)
    print(f"Test 1: 0 XOR 0 = {output} (Expected: {expected}) - {'PASS' if test_pass else 'FAIL'}")
    test = ET.SubElement(results, "test", case="1", result="PASS" if test_pass else "FAIL", 
                         expected=str(expected), actual=str(output))

    # Test case 2: 0 XOR 1 = 1
    await write_data(dut, A_DATA, 0)
    await write_data(dut, B_DATA, 1)
    output = await read_data(dut, Y_OUTPUT)
    expected = 1
    test_pass = (output == expected)
    print(f"Test 2: 0 XOR 1 = {output} (Expected: {expected}) - {'PASS' if test_pass else 'FAIL'}")
    test = ET.SubElement(results, "test", case="2", result="PASS" if test_pass else "FAIL", 
                         expected=str(expected), actual=str(output))

    # Test case 3: 1 XOR 0 = 1
    await write_data(dut, A_DATA, 1)
    await write_data(dut, B_DATA, 0)
    output = await read_data(dut, Y_OUTPUT)
    expected = 1
    test_pass = (output == expected)
    print(f"Test 3: 1 XOR 0 = {output} (Expected: {expected}) - {'PASS' if test_pass else 'FAIL'}")
    test = ET.SubElement(results, "test", case="3", result="PASS" if test_pass else "FAIL", 
                         expected=str(expected), actual=str(output))

    # Test case 4: 1 XOR 1 = 0
    await write_data(dut, A_DATA, 1)
    await write_data(dut, B_DATA, 1)
    output = await read_data(dut, Y_OUTPUT)
    expected = 0
    test_pass = (output == expected)
    print(f"Test 4: 1 XOR 1 = {output} (Expected: {expected}) - {'PASS' if test_pass else 'FAIL'}")
    test = ET.SubElement(results, "test", case="4", result="PASS" if test_pass else "FAIL", 
                         expected=str(expected), actual=str(output))

    # Write results to XML file
    tree = ET.ElementTree(results)
    with open("results.xml", "wb") as f:
        tree.write(f)

    # Generate VCD for GTKWave
    await Timer(100, units="ns")
