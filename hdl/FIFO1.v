module FIFO1 (
    input wire CLK,
    input wire RST_N,
    input wire write_en,
    input wire write_data,
    output wire write_rdy,
    input wire read_en,
    output reg read_data,
    output wire read_rdy
);

reg full, empty;

assign write_rdy = !full;
assign read_rdy = !empty;

always @(posedge CLK or negedge RST_N) begin
    if (!RST_N) begin
        read_data <= 1'b0;
        full <= 1'b0;
        empty <= 1'b1;
    end else begin
        if (write_en && !full) begin
            read_data <= write_data;
            full <= 1'b1;
            empty <= 1'b0;
        end else if (read_en && !empty) begin
            full <= 1'b0;
            empty <= 1'b1;
        end
    end
end

endmodule
