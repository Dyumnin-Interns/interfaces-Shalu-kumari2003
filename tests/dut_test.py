import random
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

async def reset_dut(dut):
    dut.RST_N.value = 0
    await Timer(10, units="ns")
    dut.RST_N.value = 1
    await RisingEdge(dut.CLK)

async def write_register(dut, address, data):
    await FallingEdge(dut.CLK)
    dut.write_address.value = address
    dut.write_data.value = data
    dut.write_en.value = 1
    await FallingEdge(dut.CLK)
    while dut.write_rdy.value != 1:
        await FallingEdge(dut.CLK)
    dut.write_en.value = 0

async def read_register(dut, address):
    await FallingEdge(dut.CLK)
    dut.read_address.value = address
    dut.read_en.value = 1
    await FallingEdge(dut.CLK)
    while dut.read_rdy.value != 1:
        await FallingEdge(dut.CLK)
    data = dut.read_data.value
    dut.read_en.value = 0
    return data

@cocotb.test()
async def test_xor_gate(dut):
    clock = Clock(dut.CLK, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    await reset_dut(dut)
    
    # Test all combinations of A and B
    test_cases = [(0, 0), (0, 1), (1, 0), (1, 1)]
    
    for a, b in test_cases:
        # Write A and B values
        await write_register(dut, 4, a)
        await write_register(dut, 5, b)
        
        # Check status registers
        a_status = await read_register(dut, 0)
        b_status = await read_register(dut, 1)
        y_status = await read_register(dut, 2)
        
        # Read output
        y_output = await read_register(dut, 3)
        
        # Verify XOR operation
        expected = a ^ b
        assert y_output == expected, f"XOR failed: {a} ^ {b} = {y_output}, expected {expected}"
        
        print(f"PASS: {a} ^ {b} = {y_output}")
    
    print("All XOR tests passed!")
