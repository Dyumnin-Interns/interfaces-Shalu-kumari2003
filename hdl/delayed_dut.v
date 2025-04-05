`timescale 1ns/1ps

module delayed_dut (
    input  wire clk,
    input  wire reset_n,
    input  wire a_data,
    input  wire a_en,
    output reg  a_rdy,
    input  wire b_data,
    input  wire b_en,
    output reg  b_rdy,
    output reg  y_data,
    output reg  y_en,
    input  wire y_rdy
);
    reg a_valid, b_valid;

    // Combinatorial ready signals
    always @(*) begin
        a_rdy = !a_valid;
        b_rdy = !b_valid;
    end

    // Sequential logic
    always @(posedge clk or negedge reset_n) begin
        if (!reset_n) begin
            a_valid <= 1'b0;
            b_valid <= 1'b0;
            y_en <= 1'b0;
            y_data <= 1'b0;
        end
        else begin
            // Capture inputs
            if (a_en && a_rdy) a_valid <= 1'b1;
            if (b_en && b_rdy) b_valid <= 1'b1;
            
            // Compute XOR when both inputs ready
            if (a_valid && b_valid) begin
                y_data <= a_data ^ b_data;
                y_en <= 1'b1;
                a_valid <= 1'b0;
                b_valid <= 1'b0;
            end
            
            // Clear output when consumed
            if (y_en && y_rdy) begin
                y_en <= 1'b0;
            end
        end
    end
endmodule
