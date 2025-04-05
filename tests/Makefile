SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES = $(shell pwd)/../hdl/FIFO1.v $(shell pwd)/../hdl/dut.v
TOPLEVEL = dut
MODULE = dut_test

EXTRA_ARGS = --vcd=on

include $(shell cocotb-config --makefiles)/Makefile.sim

wave:
	gtkwave dump.vcd
