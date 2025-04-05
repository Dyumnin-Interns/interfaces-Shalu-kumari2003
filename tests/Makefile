TOPLEVEL_LANG = verilog
VERILOG_SOURCES = ../hdl/delayed_dut.v
TOPLEVEL = delayed_dut
MODULE = dut_test

# Waveform generation (correct syntax for Icarus)
SIM_ARGS = -vcd=waveform.vcd
EXTRA_ARGS = 

include $(shell cocotb-config --makefiles)/Makefile.sim
