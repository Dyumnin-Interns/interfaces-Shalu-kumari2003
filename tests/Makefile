TOPLEVEL_LANG = verilog
VERILOG_SOURCES = ../hdl/delayed_dut.v ../hdl/FIFO1.v ../hdl/FIFO2.v
TOPLEVEL = delayed_dut
MODULE = dut_test

# Waveform generation (correct syntax for Icarus)
SIM_ARGS = -DCOCOTB_SIM=1
PLUSARGS = +vcd
EXTRA_ARGS = 

# For VCD dumping, use this instead of --vcd
COCOTB_HDL_TIMEPRECISION = 1ns

include $(shell cocotb-config --makefiles)/Makefile.sim

# Additional target to generate VCD
wave: all
	vvp -n sim_build/sim.vvp +vcd
