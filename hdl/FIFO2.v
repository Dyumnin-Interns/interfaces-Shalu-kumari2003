// hdl/FIFO2.v
module FIFO2(
    input clk,
    input rst,
    input wr_en,
    input din,
    output rd_en,
    output reg dout,
    output full,
    output empty
);

reg [7:0] mem;
reg [2:0] wr_ptr, rd_ptr;
reg [3:0] count;
reg rd_en_reg;

assign rd_en = rd_en_reg;
assign full = (count == 8);
assign empty = (count == 0);

always @(posedge clk or posedge rst) begin
    if (rst) begin
        wr_ptr <= 0;
        rd_ptr <= 0;
        count <= 0;
        rd_en_reg <= 0;
    end else begin
        if (wr_en && !full) begin
            mem[wr_ptr] <= din;
            wr_ptr <= wr_ptr + 1;
        end
        
        if (rd_en && !empty) begin
            dout <= mem[rd_ptr];
            rd_ptr <= rd_ptr + 1;
        end
        
        // Update count
        case ({wr_en && !full, rd_en && !empty})
            2'b01: count <= count - 1;
            2'b10: count <= count + 1;
            default: count <= count;
        endcase
    end
end

endmodule
