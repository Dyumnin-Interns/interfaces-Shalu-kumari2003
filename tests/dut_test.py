# test/dut_test.py
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles
import random

@cocotb.test()
async def test_xor_gate(dut):
    clock = Clock(dut.clk, 10, units="ns")  # 100MHz clock
    cocotb.start_soon(clock.start())
    
    # Reset
    dut.rst.value = 1
    await ClockCycles(dut.clk, 5)
    dut.rst.value = 0
    
    # Test all possible inputs
    test_cases = [(0,0), (0,1), (1,0), (1,1)]
    
    for a, b in test_cases:
        # Wait until FIFO is ready
        while dut.full.value == 1:
            await RisingEdge(dut.clk)
            
        # Send input
        dut.din.value = (b << 1) | a
        dut.wr_en.value = 1
        await RisingEdge(dut.clk)
        dut.wr_en.value = 0
        
        # Wait for output
        while dut.empty.value == 1:
            await RisingEdge(dut.clk)
            
        # Check output
        expected = a ^ b
        assert dut.dout.value[0] == expected, f"XOR failed for {a}, {b}: got {dut.dout.value[0]}, expected {expected}"
        print(f"PASS: {a} XOR {b} = {dut.dout.value[0]}")
    
    # Random tests
    for _ in range(10):
        a = random.randint(0, 1)
        b = random.randint(0, 1)
        
        while dut.full.value == 1:
            await RisingEdge(dut.clk)
            
        dut.din.value = (b << 1) | a
        dut.wr_en.value = 1
        await RisingEdge(dut.clk)
        dut.wr_en.value = 0
        
        while dut.empty.value == 1:
            await RisingEdge(dut.clk)
            
        expected = a ^ b
        assert dut.dout.value[0] == expected, f"XOR failed for {a}, {b}: got {dut.dout.value[0]}, expected {expected}"
        print(f"PASS: {a} XOR {b} = {dut.dout.value[0]}")
