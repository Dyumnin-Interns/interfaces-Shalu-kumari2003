// hdl/dut.v
module dut(
    input clk,
    input rst,
    input a,
    input b,
    output reg out
);

always @(posedge clk or posedge rst) begin
    if (rst) begin
        out <= 1'b0;
    end else begin
        out <= a ^ b;
    end
end

endmodule
