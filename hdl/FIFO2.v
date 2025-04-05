module FIFO2 (
    input wire CLK,
    input wire RST_N,
    input wire write_en,
    input wire write_data,
    output wire write_rdy,
    input wire read_en,
    output wire read_data,
    output wire read_rdy
);

reg [1:0] mem [0:0];
reg [0:0] wptr, rptr;
reg full, empty;

assign write_rdy = !full;
assign read_rdy = !empty;
assign read_data = mem[rptr];

always @(posedge CLK or negedge RST_N) begin
    if (!RST_N) begin
        wptr <= 1'b0;
        rptr <= 1'b0;
        full <= 1'b0;
        empty <= 1'b1;
    end else begin
        if (write_en && !full) begin
            mem[wptr] <= write_data;
            wptr <= wptr + 1;
            full <= (wptr + 1 == rptr);
            empty <= 1'b0;
        end else if (read_en && !empty) begin
            rptr <= rptr + 1;
            empty <= (rptr + 1 == wptr);
            full <= 1'b0;
        end
    end
end

endmodule
