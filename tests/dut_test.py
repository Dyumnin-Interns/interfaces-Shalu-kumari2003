import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_xor(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Reset
    dut.rst.value = 1
    await RisingEdge(dut.clk)
    dut.rst.value = 0
    
    # Test all combinations
    test_vectors = [(0,0), (0,1), (1,0), (1,1)]
    
    for a, b in test_vectors:
        # Wait until FIFO is ready
        while dut.full.value:
            await RisingEdge(dut.clk)
            
        # Send input
        dut.din.value = (b << 1) | a
        dut.wr_en.value = 1
        await RisingEdge(dut.clk)
        dut.wr_en.value = 0
        
        # Wait for output
        while dut.empty.value:
            await RisingEdge(dut.clk)
            
        # Verify output
        expected = a ^ b
        assert dut.dout.value[0] == expected, f"Failed: {a}^{b}={dut.dout.value[0]}, expected {expected}"
        print(f"PASS: {a}^{b}={dut.dout.value[0]}")
