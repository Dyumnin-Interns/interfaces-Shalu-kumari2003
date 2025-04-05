module dut(
    input clk,
    input rst,
    input a,
    input b,
    output reg out
);
always @(posedge clk or posedge rst) begin
    if (rst) out <= 1'b0;
    else out <= a ^ b;
end
endmodule
