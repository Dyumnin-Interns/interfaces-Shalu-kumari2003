import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.clock import Clock
from cocotb.waveform import WaveDumper

async def reset_dut(dut):
    dut.reset_n.value = 0
    dut.a_data.value = 0
    dut.b_data.value = 0
    dut.a_en.value = 0
    dut.b_en.value = 0
    await Timer(20, units="ns")
    dut.reset_n.value = 1
    await RisingEdge(dut.clk)

@cocotb.test()
async def test_xor_gate(dut):
    # Enable waveform dumping
    WaveDumper(dut)
    
    # Start 100MHz clock
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())
    
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
        await RisingEdge(dut.clk)
        
        # Clear enables
        dut.a_en.value = 0
        dut.b_en.value = 0
        
        # Wait for computation
        while not dut.y_en.value:
            await RisingEdge(dut.clk)
        
        # Verify output
        assert dut.y_data.value == expected, f"Failed: {a} XOR {b} = {dut.y_data.value} (expected {expected})"
        
        # Acknowledge output
        dut.y_rdy.value = 1
        await RisingEdge(dut.clk)
        dut.y_rdy.value = 0
    
    dut._log.info("All XOR tests passed!")
    await Timer(100, units="ns")  # Extra time for waveform viewing
