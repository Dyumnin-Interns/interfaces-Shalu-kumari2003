TOPLEVEL_LANG = verilog
VERILOG_SOURCES = ../hdl/delayed_dut.v ../hdl/FIFO1.v ../hdl/FIFO2.v
TOPLEVEL = delayed_dut
MODULE = dut_test

# Waveform generation
SIM_ARGS += -vcd
PLUSARGS += +vcd=on
EXTRA_ARGS += --vcd=sim_build/waveform.vcd

include $(shell cocotb-config --makefiles)/Makefile.sim
