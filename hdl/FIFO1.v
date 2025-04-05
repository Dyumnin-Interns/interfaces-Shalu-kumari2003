module FIFO1 (
    input CLK,
    input RST_N,
    input enq,
    input [0:0] din,
    output reg full,
    output reg [0:0] dout,
    output reg empty
);
    reg [0:0] fifo;
    
    always @(posedge CLK or negedge RST_N) begin
        if (!RST_N) begin
            fifo <= 0;
            full <= 0;
            empty <= 1;
        end
        else if (enq && !full) begin
            fifo <= din;
            full <= 1;
            empty <= 0;
        end
    end
    
    assign dout = fifo;
endmodule
