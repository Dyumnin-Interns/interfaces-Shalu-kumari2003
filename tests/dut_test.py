import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def test_xor_gate(dut):
    """Test XOR gate functionality through CSR interface"""
    
    clock = Clock(dut.CLK, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Reset
    dut.RST_N.value = 0
    await Timer(20, units="ns")
    dut.RST_N.value = 1
    await RisingEdge(dut.CLK)
    
    # Test all combinations
    test_cases = [(0, 0), (0, 1), (1, 0), (1, 1)]
    
    for a, b in test_cases:
        # Write A value (address 4)
        dut.write_address.value = 4
        dut.write_data.value = a
        dut.write_en.value = 1
        await RisingEdge(dut.CLK)
        dut.write_en.value = 0
        await RisingEdge(dut.CLK)
        
        # Write B value (address 5)
        dut.write_address.value = 5
        dut.write_data.value = b
        dut.write_en.value = 1
        await RisingEdge(dut.CLK)
        dut.write_en.value = 0
        await RisingEdge(dut.CLK)
        
        # Read output (address 3)
        dut.read_address.value = 3
        dut.read_en.value = 1
        await RisingEdge(dut.CLK)
        while dut.read_rdy.value != 1:
            await RisingEdge(dut.CLK)
        y_output = dut.read_data.value
        dut.read_en.value = 0
        
        # Verify
        expected = a ^ b
        assert y_output == expected, f"XOR failed: {a} ^ {b} = {y_output}, expected {expected}"
        
        dut._log.info(f"PASS: {a} ^ {b} = {y_output}")
    
    dut._log.info("All XOR tests passed!")
