# Simulator settings
SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES = ../hdl/FIFO1.v ../hdl/FIFO2.v ../hdl/dut.v
TOPLEVEL = dut
MODULE = test_dut

# Cocotb settings
COCOTB_HDL_TIMEUNIT = 1ns
COCOTB_HDL_TIMEPRECISION = 1ps

# Include Cocotb's Makefile
include $(shell cocotb-config --makefiles)/Makefile.sim

# Override default targets
.PHONY: all test clean

all: test

test:
	$(MAKE) sim

clean:
	rm -rf sim_build results.xml orig.xml *.vcd
