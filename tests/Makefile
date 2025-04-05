TOPLEVEL_LANG = verilog
VERILOG_SOURCES = ../hdl/delayed_dut.v ../hdl/FIFO1.v ../hdl/FIFO2.v
TOPLEVEL = delayed_dut
MODULE = dut_test
SIM = icarus
EXTRA_ARGS = +vcd+dump.vcd

include $(shell cocotb-config --makefiles)/Makefile.sim
