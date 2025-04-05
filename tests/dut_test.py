import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, ClockCycles

@cocotb.test()
async def basic_test(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Reset
    dut.rst.value = 1
    dut.wr_en.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst.value = 0
    
    # Test cases
    test_vectors = [
        (0, 0, 0),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0)
    ]
    
    for a, b, expected in test_vectors:
        # Apply inputs
        dut.din.value = (b << 1) | a
        dut.wr_en.value = 1
        await RisingEdge(dut.clk)
        dut.wr_en.value = 0
        
        # Wait 2 cycles for processing
        await ClockCycles(dut.clk, 2)
        
        # Verify output
        assert dut.dout.value[0] == expected, \
            f"Failed: {a}^{b} got {dut.dout.value[0]}, expected {expected}"
        
        print(f"PASS: {a}^{b} = {dut.dout.value[0]}")
