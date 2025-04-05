all: compile simulate

compile:
	iverilog -o dut_test ../hdl/FIFO1.v ../hdl/FIFO2.v ../hdl/dut.v dut_test.v

simulate:
	vvp dut_test
	gtkwave dut_test.vcd

clean:
	rm -f dut_test dut_test.vcd
