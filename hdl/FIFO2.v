module FIFO2 (
    input CLK,
    input RST_N,
    input enq,
    input [0:0] din,
    output reg full,
    output reg [0:0] dout,
    output reg empty
);
    reg [1:0] fifo;
    reg [0:0] head;
    
    always @(posedge CLK or negedge RST_N) begin
        if (!RST_N) begin
            fifo <= 0;
            head <= 0;
            full <= 0;
            empty <= 1;
        end
        else if (enq && !full) begin
            fifo[head] <= din;
            head <= head + 1;
            empty <= 0;
            full <= (head == 1);
        end
    end
    
    assign dout = fifo[0];
endmodule
