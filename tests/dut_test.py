import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.drivers import BusDriver
from cocotb.result import TestSuccess

class InputDriver(BusDriver):
    def __init__(self, dut, name):
        super().__init__(dut, name)
        self.bus.enable.value = 0

    async def send(self, value):
        await RisingEdge(self.dut.clk)
        self.bus.data.value = value
        self.bus.enable.value = 1
        await RisingEdge(self.dut.clk)
        self.bus.enable.value = 0

class OutputMonitor:
    def __init__(self, dut, name):
        self.dut = dut
        self.name = name

    async def monitor(self):
        while True:
            await RisingEdge(self.dut.clk)
            if self.dut.Y_enable.value == 1:
                print(f"Output Y = {self.dut.Y_data.value}")

@cocotb.test()
async def test_xor_gate(dut):
    # Reset
    dut.reset_n.value = 0
    await Timer(10, units="ns")
    dut.reset_n.value = 1

    # Create Drivers
    input_a = InputDriver(dut, "A")
    input_b = InputDriver(dut, "B")
    output_mon = OutputMonitor(dut, "Y")

    # Start Monitoring
    cocotb.fork(output_mon.monitor())

    # Test Cases
    await input_a.send(0)
    await input_b.send(0)
    await Timer(20, units="ns")
    assert dut.Y_data.value == 0  # 0 XOR 0 = 0

    await input_a.send(1)
    await input_b.send(0)
    await Timer(20, units="ns")
    assert dut.Y_data.value == 1  # 1 XOR 0 = 1

    raise TestSuccess("XOR Test Passed!")
