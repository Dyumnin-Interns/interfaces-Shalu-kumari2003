import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.clock import Clock

async def reset_dut(dut):
    dut.reset_n.value = 0
    await Timer(10, units="ns")
    dut.reset_n.value = 1
    await RisingEdge(dut.clk)

@cocotb.test()
async def test_xor_gate(dut):
    # Start Clock
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())
    
    # Reset
    await reset_dut(dut)
    
    # Test Cases
    test_cases = [
        (0, 0, 0),  # A=0, B=0 → Y=0
        (0, 1, 1),  # A=0, B=1 → Y=1
        (1, 0, 1),  # A=1, B=0 → Y=1
        (1, 1, 0)   # A=1, B=1 → Y=0
    ]
    
    for a, b, expected in test_cases:
        # Drive inputs
        dut.A_data.value = a
        dut.B_data.value = b
        dut.A_enable.value = 1
        dut.B_enable.value = 1
        
        # Wait for processing
        await RisingEdge(dut.clk)
        dut.A_enable.value = 0
        dut.B_enable.value = 0
        
        # Wait for output
        while dut.Y_enable.value != 1:
            await RisingEdge(dut.clk)
        
        # Verify
        assert dut.Y_data.value == expected, f"Failed: {a} XOR {b} != {dut.Y_data.value}"
    
    dut._log.info("All tests passed!")
