module delayed_dut (
    input  CLK,
    input  RST_N,
    input  a_data,
    input  a_en,
    output a_rdy,
    input  b_data,
    input  b_en,
    output b_rdy,
    output y_data,
    output y_en,
    input  y_rdy
);
    reg a_valid, b_valid;
    reg y_data_reg;
    reg y_en_reg;
    
    assign a_rdy = !a_valid;
    assign b_rdy = !b_valid;
    assign y_data = y_data_reg;
    assign y_en = y_en_reg;

    always @(posedge CLK or negedge RST_N) begin
        if (!RST_N) begin
            a_valid <= 0;
            b_valid <= 0;
            y_en_reg <= 0;
        end
        else begin
            // Capture inputs
            if (a_en && a_rdy) a_valid <= 1;
            if (b_en && b_rdy) b_valid <= 1;
            
            // Compute XOR when both inputs ready
            if (a_valid && b_valid) begin
                y_data_reg <= a_data ^ b_data;
                y_en_reg <= 1;
                a_valid <= 0;
                b_valid <= 0;
            end
            
            // Clear output when consumed
            if (y_en_reg && y_rdy) begin
                y_en_reg <= 0;
            end
        end
    end
endmodule
