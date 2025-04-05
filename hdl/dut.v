module dut (
    input wire CLK,
    input wire RST_N,
    
    // Read Interface
    input wire [2:0] read_address,
    output reg [0:0] read_data,
    output reg read_rdy,
    input wire read_en,
    
    // Write Interface
    output wire write_rdy,
    input wire [2:0] write_address,
    input wire [0:0] write_data,
    input wire write_en
);

// Internal registers
reg A_Data, B_Data;
reg Y_Status;
wire Y_Output;

// FIFO signals
wire A_FIFO_not_full, B_FIFO_not_full;
wire Y_FIFO_not_empty;

// Instantiate FIFOs
FIFO1 A_FIFO (
    .CLK(CLK),
    .RST_N(RST_N),
    .write_en(write_en && (write_address == 3'd4)),
    .write_data(write_data),
    .write_rdy(A_FIFO_not_full),
    .read_en(read_en && (read_address == 3'd4)),
    .read_data(A_Data),
    .read_rdy()
);

FIFO1 B_FIFO (
    .CLK(CLK),
    .RST_N(RST_N),
    .write_en(write_en && (write_address == 3'd5)),
    .write_data(write_data),
    .write_rdy(B_FIFO_not_full),
    .read_en(read_en && (read_address == 3'd5)),
    .read_data(B_Data),
    .read_rdy()
);

// XOR Gate implementation
assign Y_Output = A_Data ^ B_Data;

FIFO2 Y_FIFO (
    .CLK(CLK),
    .RST_N(RST_N),
    .write_en(A_FIFO_not_full && B_FIFO_not_full),
    .write_data(Y_Output),
    .write_rdy(),
    .read_en(read_en && (read_address == 3'd3)),
    .read_data(Y_Output),
    .read_rdy(Y_FIFO_not_empty)
);

// Read interface logic
always @(*) begin
    read_rdy = 1'b1;
    case (read_address)
        3'd0: read_data = A_FIFO_not_full;
        3'd1: read_data = B_FIFO_not_full;
        3'd2: read_data = Y_FIFO_not_empty;
        3'd3: read_data = Y_Output;
        default: read_data = 1'b0;
    endcase
end

// Write interface is handled by FIFOs directly
assign write_rdy = (write_address == 3'd4) ? A_FIFO_not_full :
                   (write_address == 3'd5) ? B_FIFO_not_full : 1'b0;

endmodule
