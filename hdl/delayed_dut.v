module delayed_dut (
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

// Add 2-cycle delay to all signals
reg [2:0] read_address_d1, read_address_d2;
reg read_en_d1, read_en_d2;
reg [2:0] write_address_d1, write_address_d2;
reg [0:0] write_data_d1, write_data_d2;
reg write_en_d1, write_en_d2;

always @(posedge CLK or negedge RST_N) begin
    if (!RST_N) begin
        read_address_d1 <= 3'b0;
        read_address_d2 <= 3'b0;
        read_en_d1 <= 1'b0;
        read_en_d2 <= 1'b0;
        write_address_d1 <= 3'b0;
        write_address_d2 <= 3'b0;
        write_data_d1 <= 1'b0;
        write_data_d2 <= 1'b0;
        write_en_d1 <= 1'b0;
        write_en_d2 <= 1'b0;
    end else begin
        read_address_d1 <= read_address;
        read_address_d2 <= read_address_d1;
        read_en_d1 <= read_en;
        read_en_d2 <= read_en_d1;
        write_address_d1 <= write_address;
        write_address_d2 <= write_address_d1;
        write_data_d1 <= write_data;
        write_data_d2 <= write_data_d1;
        write_en_d1 <= write_en;
        write_en_d2 <= write_en_d1;
    end
end

// Instantiate actual DUT with delayed signals
dut dut_inst (
    .CLK(CLK),
    .RST_N(RST_N),
    .read_address(read_address_d2),
    .read_data(read_data),
    .read_rdy(read_rdy),
    .read_en(read_en_d2),
    .write_rdy(write_rdy),
    .write_address(write_address_d2),
    .write_data(write_data_d2),
    .write_en(write_en_d2)
);

endmodule
