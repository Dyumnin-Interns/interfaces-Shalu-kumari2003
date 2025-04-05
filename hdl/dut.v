module dut (
    input CLK,
    input RST_N,
    input [2:0] read_address,
    output reg [0:0] read_data,
    output reg read_rdy,
    input read_en,
    output reg write_rdy,
    input [2:0] write_address,
    input [0:0] write_data,
    input write_en
);
    wire [0:0] a_status, b_status, y_status, y_output;
    wire [0:0] a_data, b_data;
    
    // Instantiate FIFOs
    FIFO1 a_fifo(CLK, RST_N, write_en && write_address==4, write_data, a_status, a_data, );
    FIFO1 b_fifo(CLK, RST_N, write_en && write_address==5, write_data, b_status, b_data, );
    FIFO2 y_fifo(CLK, RST_N, a_status && b_status, a_data ^ b_data, , y_output, y_status);
    
    always @(posedge CLK or negedge RST_N) begin
        if (!RST_N) begin
            read_data <= 0;
            read_rdy <= 0;
            write_rdy <= 1;
        end
        else begin
            read_rdy <= read_en;
            write_rdy <= 1;
            
            if (read_en) begin
                case (read_address)
                    0: read_data <= a_status;
                    1: read_data <= b_status;
                    2: read_data <= y_status;
                    3: read_data <= y_output;  // XOR output
                    default: read_data <= 0;
                endcase
            end
        end
    end
endmodule
