module delayed_dut(
    input clk,
    input rst,
    input [1:0] din,
    input wr_en,
    output [1:0] dout,
    output reg rd_en
);
reg [1:0] input_reg;
reg output_reg;
wire xor_out;

// Input handling
always @(posedge clk or posedge rst) begin
    if (rst) begin
        input_reg <= 2'b0;
        rd_en <= 0;
    end 
    else if (wr_en) begin
        input_reg <= din;
        rd_en <= 1;
    end
    else begin
        rd_en <= 0;
    end
end

// XOR operation
dut xor_inst(
    .clk(clk),
    .rst(rst),
    .a(input_reg[0]),
    .b(input_reg[1]),
    .out(xor_out)
);

// Output assignment
assign dout = {1'b0, xor_out};
endmodule
