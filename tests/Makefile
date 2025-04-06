TOPLEVEL_LANG = verilog
VERILOG_SOURCES = ../hdl/delayed_dut.v ../hdl/FIFO1.v ../hdl/FIFO2.v
TOPLEVEL = delayed_dut  # Match the module name in delayed_dut.v
MODULE = dut_test
SIM = icarus  # Explicitly set Icarus Verilog as simulator

# Ensure tests directory exists and copy VCD files
EXTRA_ARGS += -o sim_build/sim.vvp
COCOTB_HDL_TIMEUNIT = 1ns
COCOTB_HDL_TIMEPRECISION = 1ps

include $(shell cocotb-config --makefiles)/Makefile.sim

# Custom target to ensure tests/ directory and move VCD files
.PHONY: post_sim
post_sim:
	@mkdir -p tests
	@if [ -f sim_build/delayed_dut.vcd ]; then mv sim_build/delayed_dut.vcd tests/; fi
