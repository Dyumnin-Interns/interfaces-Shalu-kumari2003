// hdl/delayed_dut.v
module delayed_dut(
    input clk,
    input rst,
    input [1:0] din,
    input wr_en,
    output [1:0] dout,
    output rd_en
);

wire a, b;
wire xor_out;

FIFO1 input_fifo(
    .clk(clk),
    .rst(rst),
    .wr_en(wr_en),
    .din(din),
    .rd_en(rd_en),
    .dout({a, b}),
    .full(),
    .empty()
);

dut xor_gate(
    .clk(clk),
    .rst(rst),
    .a(a),
    .b(b),
    .out(xor_out)
);

FIFO2 output_fifo(
    .clk(clk),
    .rst(rst),
    .wr_en(rd_en),
    .din(xor_out),
    .rd_en(1'b1),
    .dout(dout[0]),
    .full(),
    .empty()
);

assign dout[1] = 1'b0;

endmodule
