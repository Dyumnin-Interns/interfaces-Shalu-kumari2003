module FIFO1(
    input clk,
    input rst,
    input wr_en,
    input [1:0] din,
    output reg rd_en,
    output reg [1:0] dout,
    output full,
    output empty
);
reg [1:0] mem [0:7];
reg [2:0] wr_ptr, rd_ptr;
reg [3:0] count;

assign full = (count == 8);
assign empty = (count == 0);

always @(posedge clk or posedge rst) begin
    if (rst) begin
        wr_ptr <= 0; rd_ptr <= 0;
        count <= 0; rd_en <= 0;
    end else begin
        if (wr_en && !full) begin
            mem[wr_ptr] <= din;
            wr_ptr <= wr_ptr + 1;
        end
        if (rd_en && !empty) begin
            dout <= mem[rd_ptr];
            rd_ptr <= rd_ptr + 1;
        end
        count <= count + (wr_en && !full) - (rd_en && !empty);
    end
end
endmodule
