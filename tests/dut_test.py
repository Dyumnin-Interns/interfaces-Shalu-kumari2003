import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def test_xor(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Reset
    dut.rst.value = 1
    dut.wr_en.value = 0
    await RisingEdge(dut.clk)
    dut.rst.value = 0
    await RisingEdge(dut.clk)
    
    # Test cases
    test_vectors = [(0,0), (0,1), (1,0), (1,1)]
    
    for a, b in test_vectors:
        # Wait if FIFO is full
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
        
        # Verify output
        expected = a ^ b
        actual = dut.dout.value[0]
        assert actual == expected, f"Failed: {a}^{b}={actual}, expected {expected}"
        print(f"PASS: {a}^{b}={actual}")
        
        await RisingEdge(dut.clk)  # Extra cycle for stability
