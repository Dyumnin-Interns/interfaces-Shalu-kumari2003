TOPLEVEL_LANG = verilog
VERILOG_SOURCES = ../hdl/dut.v ../hdl/FIFO1.v ../hdl/FIFO2.v ../hdl/delayed_dut.v
TOPLEVEL = dut
MODULE = dut_test

# Icarus Verilog specific flags for waveform generation
SIM_ARGS += -D COCOTB_SIM=1 -s $(TOPLEVEL) -g2012
EXTRA_ARGS += -Wall

# For VCD generation
PLUSARGS += -lvvm
SIM_BUILD = sim_build
VCD = waveform.vcd

include $(shell cocotb-config --makefiles)/Makefile.sim

# Custom rule for simulation with VCD
sim_build/sim.vvp: $(VERILOG_SOURCES)
	@mkdir -p $(SIM_BUILD)
	iverilog -o $@ $(SIM_ARGS) $(VERILOG_SOURCES) -DCOCOTB_SIM=1 -g2012

waveform.vcd: sim_build/sim.vvp
	vvp -n $< +lvvm $(PLUSARGS) +vcd=$(VCD)

run: waveform.vcd

clean::
	rm -rf $(SIM_BUILD) $(VCD) results.xml
