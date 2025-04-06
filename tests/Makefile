TOPLEVEL_LANG = verilog
# Only include delayed_dut.v OR dut.v, not both
VERILOG_SOURCES = ../hdl/delayed_dut.v ../hdl/FIFO1.v ../hdl/FIFO2.v
TOPLEVEL = delayed_dut  # Match the module name in delayed_dut.v
MODULE = dut_test

include $(shell cocotb-config --makefiles)/Makefile.sim
