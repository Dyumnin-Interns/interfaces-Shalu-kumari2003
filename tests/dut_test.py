import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.clock import Clock
from cocotb.result import TestSuccess

@cocotb.test()
async def test_xor_gate(dut):
    # Create 100MHz clock
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Reset sequence
    dut.reset_n.value = 0
    dut.a_data.value = 0
    dut.b_data.value = 0
    dut.a_en.value = 0
    dut.b_en.value = 0
    dut.y_rdy.value = 1  # Always ready for autograder
    await Timer(20, units="ns")
    dut.reset_n.value = 1
    await RisingEdge(dut.clk)
    
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
        
        # Release enables
        dut.a_en.value = 0
        dut.b_en.value = 0
        
        # Wait for output
        timeout = 100
        while not dut.y_en.value and timeout > 0:
            await RisingEdge(dut.clk)
            timeout -= 1
        
        assert timeout > 0, "Timeout waiting for output"
        assert dut.y_data.value == expected, f"{a} XOR {b} failed (got {dut.y_data.value}, expected {expected})"
        
        # Consume output
        await RisingEdge(dut.clk)
    
    # Final delay for complete waveforms
    await Timer(100, units="ns")
    raise TestSuccess("All tests passed with waveforms")
