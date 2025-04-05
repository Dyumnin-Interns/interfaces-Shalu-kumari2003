import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def test_xor(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    dut.rst.value = 1
    await RisingEdge(dut.clk)
    dut.rst.value = 0
    
    test_vectors = [(0,0), (0,1), (1,0), (1,1)]
    
    for a, b in test_vectors:
        dut.din.value = (b << 1) | a
        dut.wr_en.value = 1
        await RisingEdge(dut.clk)
        dut.wr_en.value = 0
        
        while dut.empty.value:
            await RisingEdge(dut.clk)
            
        assert dut.dout.value[0] == (a ^ b), f"Failed {a}^{b}={dut.dout.value[0]}"
        print(f"PASS: {a}^{b}={dut.dout.value[0]}")
