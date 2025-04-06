TOPLEVEL_LANG = verilog
VERILOG_SOURCES = ../hdl/dut.v ../hdl/FIFO1.v ../hdl/FIFO2.v ../hdl/delayed_dut.v
TOPLEVEL = dut
MODULE = dut_test

# Waveform generation
SIM_ARGS += -vcd waveform.vcd
EXTRA_ARGS += --trace --trace-structs

include $(shell cocotb-config --makefiles)/Makefile.sim

# Clean additional files
clean::
	rm -f waveform.vcd results.xml
