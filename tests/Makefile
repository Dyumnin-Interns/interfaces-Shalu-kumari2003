all: run

run:
	iverilog -o sim -I../hdl ../hdl/FIFO1.v ../hdl/FIFO2.v ../hdl/dut.v ../hdl/delayed_dut.v dut_test.py
	vvp sim
	gtkwave dump.vcd

clean:
	rm -f sim dump.vcd
