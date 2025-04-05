TOPLEVEL_LANG = verilog
VERILOG_SOURCES = ../hdl/delayed_dut.v ../hdl/FIFO1.v ../hdl/FIFO2.v
TOPLEVEL = delayed_dut
MODULE = dut_test
SIM = icarus
WAVES = 1  # Enable waveform dumping
EXTRA_ARGS = -DCOCOTB_SIM=1 -s$(TOPLEVEL) -g2012

include $(shell cocotb-config --makefiles)/Makefile.sim
