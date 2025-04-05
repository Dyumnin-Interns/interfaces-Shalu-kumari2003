import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

async def reset_dut(dut, duration_ns=100):
    dut.RST_N.value = 0
    await Timer(duration_ns, units="ns")
    dut.RST_N.value = 1
    await RisingEdge(dut.CLK)
    await RisingEdge(dut.CLK)

async def write_register(dut, address, data):
    await RisingEdge(dut.CLK)
    dut.write_address.value = address
    dut.write_data.value = data
    dut.write_en.value = 1
    await RisingEdge(dut.CLK)
    while dut.write_rdy.value != 1:
        await RisingEdge(dut.CLK)
    dut.write_en.value = 0
    await RisingEdge(dut.CLK)

async def read_register(dut, address):
    await RisingEdge(dut.CLK)
    dut.read_address.value = address
    dut.read_en.value = 1
    await RisingEdge(dut.CLK)
    while dut.read_rdy.value != 1:
        await RisingEdge(dut.CLK)
    data = dut.read_data.value
    dut.read_en.value = 0
    await RisingEdge(dut.CLK)
    return data

@cocotb.test()
async def test_xor_gate(dut):
    clock = Clock(dut.CLK, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    await reset_dut(dut, 100)
    
    test_cases = [(0, 0), (0, 1), (1, 0), (1, 1)]
    
    for a, b in test_cases:
        # Write inputs
        await write_register(dut, 4, a)
        await write_register(dut, 5, b)
        
        # Wait for computation
        await Timer(50, units="ns")
        
        # Read output
        y_output = await read_register(dut, 3)
        
        # Verify
        expected = a ^ b
        assert y_output == expected, f"XOR failed: {a} ^ {b} = {int(y_output)}, expected {expected}"
        
        dut._log.info(f"PASS: {a} ^ {b} = {int(y_output)}")
    
    dut._log.info("All XOR tests passed!")
