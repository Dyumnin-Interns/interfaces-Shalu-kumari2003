TOPLEVEL_LANG = verilog
VERILOG_SOURCES = ../hdl/delayed_dut.v ../hdl/FIFO1.v ../hdl/FIFO2.v
TOPLEVEL = delayed_dut
MODULE = dut_test
SIM = icarus
WAVES = 1
EXTRA_ARGS = -DCOCOTB_SIM=1 -s $(TOPLEVEL)

# Waveform options
ifeq ($(WAVES),1)
EXTRA_ARGS += -DDUMP_VCD=1
endif

include $(shell cocotb-config --makefiles)/Makefile.sim
