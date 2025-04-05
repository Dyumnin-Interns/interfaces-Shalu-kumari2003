SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES = $(shell pwd)/../hdl/FIFO1.v $(shell pwd)/../hdl/FIFO2.v $(shell pwd)/../hdl/dut.v $(shell pwd)/../hdl/delayed_dut.v
TOPLEVEL ?= dut
MODULE = dut_test

include $(shell cocotb-config --makefiles)/Makefile.sim

wave:
	gtkwave dump.vcd
