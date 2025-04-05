// hdl/FIFO1.v
module FIFO1(
    input clk,
    input rst,
    input wr_en,
    input [1:0] din,
    output reg rd_en,
    output reg [1:0] dout,
    output reg full,
    output reg empty
);

reg [1:0] mem [0:7];
reg [2:0] wr_ptr, rd_ptr;
reg [3:0] count;

always @(posedge clk or posedge rst) begin
    if (rst) begin
        wr_ptr <= 0;
        rd_ptr <= 0;
        count <= 0;
        full <= 0;
        empty <= 1;
        rd_en <= 0;
    end else begin
        if (wr_en && !full) begin
            mem[wr_ptr] <= din;
            wr_ptr <= wr_ptr + 1;
            empty <= 0;
            if (wr_ptr + 1 == rd_ptr)
                full <= 1;
        end
        
        if (rd_en && !empty) begin
            dout <= mem[rd_ptr];
            rd_ptr <= rd_ptr + 1;
            full <= 0;
            if (rd_ptr + 1 == wr_ptr)
                empty <= 1;
        end
        
        if (wr_en && !full)
            count <= count + 1;
        if (rd_en && !empty)
            count <= count - 1;
    end
end

endmodule
