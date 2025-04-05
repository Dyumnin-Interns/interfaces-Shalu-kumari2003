import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.clock import Clock
import os

async def reset_dut(dut):
    dut.RST_N.value = 0
    dut.a_data.value = 0
    dut.b_data.value = 0
    dut.a_en.value = 0
    dut.b_en.value = 0
    await Timer(20, units="ns")
    dut.RST_N.value = 1
    await RisingEdge(dut.CLK)

@cocotb.test()
async def test_xor_gate(dut):
    # Start 100MHz clock
    clock = Clock(dut.CLK, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Reset
    await reset_dut(dut)
    
    # Test cases: (a, b, expected_y)
    test_cases = [
        (0, 0, 0),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0)
    ]
    
    for a, b, expected in test_cases:
        # Drive inputs
        dut.a_data.value = a
        dut.b_data.value = b
        dut.a_en.value = 1
        dut.b_en.value = 1
        await RisingEdge(dut.CLK)
        
        # Release enables
        dut.a_en.value = 0
        dut.b_en.value = 0
        
        # Wait for computation
        while not dut.y_en.value:
            await RisingEdge(dut.CLK)
        
        # Verify output
        assert dut.y_data.value == expected, f"Failed: {a} XOR {b} = {dut.y_data.value} (expected {expected})"
        
        # Acknowledge output
        dut.y_rdy.value = 1
        await RisingEdge(dut.CLK)
        dut.y_rdy.value = 0
    
    dut._log.info("All tests passed!")
    await Timer(100, units="ns")  # Extra time for waveforms
