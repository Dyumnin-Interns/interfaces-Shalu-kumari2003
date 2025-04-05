# test/Makefile
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES = ../hdl/delayed_dut.v ../hdl/FIFO1.v ../hdl/FIFO2.v ../hdl/dut.v
TOPLEVEL = delayed_dut
MODULE = dut_test

include $(shell cocotb-config --makefiles)/Makefile.sim

wave:
	gtkwave waveforms.vcd &
