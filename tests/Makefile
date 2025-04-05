TOPLEVEL_LANG = verilog
VERILOG_SOURCES = ../hdl/delayed_dut.v
TOPLEVEL = delayed_dut
MODULE = dut_test
SIM = icarus
GUI = 0

# Waveform generation
ifeq ($(WAVES),1)
EXTRA_ARGS += -DCOCOTB_SIM=1 -s $(TOPLEVEL) -g2012 -DDUMP_VCD=1
else
EXTRA_ARGS += -DCOCOTB_SIM=1 -s $(TOPLEVEL) -g2012
endif

include $(shell cocotb-config --makefiles)/Makefile.sim
