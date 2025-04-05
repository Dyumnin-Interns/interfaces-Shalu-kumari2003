module delayed_dut (
    input clk,
    input reset_n,
    input a_data,
    input a_en,
    output a_rdy,
    input b_data,
    input b_en,
    output b_rdy,
    output reg y_data,
    output reg y_en,
    input y_rdy
);
    reg a_valid, b_valid;
    
    assign a_rdy = !a_valid;
    assign b_rdy = !b_valid;

    // Initialize waveform dumping
    initial begin
        $dumpfile("waveform.vcd");
        $dumpvars(0, delayed_dut);
    end

    always @(posedge clk or negedge reset_n) begin
        if (!reset_n) begin
            a_valid <= 0;
            b_valid <= 0;
            y_en <= 0;
            y_data <= 0;
        end
        else begin
            // Capture inputs
            if (a_en && a_rdy) a_valid <= 1;
            if (b_en && b_rdy) b_valid <= 1;
            
            // Compute XOR when both inputs are ready
            if (a_valid && b_valid) begin
                y_data <= a_data ^ b_data;
                y_en <= 1;
                a_valid <= 0;
                b_valid <= 0;
            end
            
            // Clear output when consumed
            if (y_en && y_rdy) begin
                y_en <= 0;
            end
        end
    end
endmodule
