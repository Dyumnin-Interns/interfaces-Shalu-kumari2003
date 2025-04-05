TOPLEVEL_LANG = verilog
VERILOG_SOURCES = ../hdl/delayed_dut.v
TOPLEVEL = delayed_dut
MODULE = dut_test

# Enable waveform generation
SIM_ARGS = -vcd
EXTRA_ARGS = --vcd=waveform.vcd

include $(shell cocotb-config --makefiles)/Makefile.sim
