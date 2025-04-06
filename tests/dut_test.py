import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.clock import Clock
import os

# Configure output paths
os.environ["COCOTB_RESULTS_FILE"] = os.path.join(os.getcwd(), "results.xml")
os.environ["WAVES"] = os.path.join(os.getcwd(), "waveform.vcd")

async def reset_dut(dut):
    dut.reset_n.value = 0
    dut.A_data.value = 0
    dut.B_data.value = 0
    dut.A_enable.value = 0
    dut.B_enable.value = 0
    await Timer(20, units="ns")
    dut.reset_n.value = 1
    await RisingEdge(dut.clk)

@cocotb.test()
async def test_xor_gate(dut):
    # Enable waveform dumping
    dut._test.dumpfile = "waveform.vcd"
    
    # Start 100MHz clock
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Reset DUT
    await reset_dut(dut)
    
    # Test cases: (A, B, expected_Y)
    test_cases = [
        (0, 0, 0),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0)
    ]
    
    for a, b, expected in test_cases:
        # Drive inputs
        dut.A_data.value = a
        dut.B_data.value = b
        dut.A_enable.value = 1
        dut.B_enable.value = 1
        await RisingEdge(dut.clk)
        
        # Wait for computation (2 cycles for FIFOs + 1 cycle for XOR)
        for _ in range(3):
            await RisingEdge(dut.clk)
        
        # Verify output
        assert dut.Y_data.value == expected, f"Failed: {a} XOR {b} = {dut.Y_data.value} (expected {expected})"
        
        # Acknowledge output
        dut.Y_ready.value = 1
        await RisingEdge(dut.clk)
        dut.Y_ready.value = 0
    
    dut._log.info("All XOR tests passed!")
