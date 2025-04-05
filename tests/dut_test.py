import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.clock import Clock
from cocotb.utils import get_sim_time

@cocotb.test()
async def test_xor_gate(dut):
    # Create 100MHz clock
    clock = Clock(dut.CLK, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Reset sequence
    dut.RST_N.value = 0
    dut.a_data.value = 0
    dut.b_data.value = 0
    dut.a_en.value = 0
    dut.b_en.value = 0
    dut.y_rdy.value = 0
    await Timer(20, units="ns")
    dut.RST_N.value = 1
    await RisingEdge(dut.CLK)
    
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
        
        # Wait for output with timeout
        timeout = 100
        while not dut.y_en.value and timeout > 0:
            await RisingEdge(dut.CLK)
            timeout -= 1
        
        if timeout == 0:
            raise cocotb.result.TestFailure(f"Timeout waiting for output (a={a}, b={b})")
        
        # Verify output
        assert dut.y_data.value == expected, \
            f"At {get_sim_time(units='ns')}ns: {a} XOR {b} = {int(dut.y_data.value)} (expected {expected})"
        
        # Acknowledge output
        dut.y_rdy.value = 1
        await RisingEdge(dut.CLK)
        dut.y_rdy.value = 0
    
    # Final delay for waveforms
    await Timer(100, units="ns")
    dut._log.info("All tests passed successfully!")
