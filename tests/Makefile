
TOPLEVEL_LANG = verilog
VERILOG_SOURCES = ../hdl/delayed_dut.v ../hdl/FIFO1.v ../hdl/FIFO2.v
TOPLEVEL = delayed_dut
MODULE = dut_test
SIM = icarus
GUI ?= 0
WAVES ?= 1

ifeq ($(WAVES),1)
	EXTRA_ARGS += -DDUMP_VCD=1
endif

include $(shell cocotb-config --makefiles)/Makefile.sim
