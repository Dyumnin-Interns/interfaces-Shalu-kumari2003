module delayed_dut (
    input clk,
    input reset_n,
    input A_data,
    input A_enable,
    output A_ready,
    input B_data,
    input B_enable,
    output B_ready,
    output reg Y_data,
    output reg Y_enable,
    input Y_ready
);
    // State management
    reg A_valid, B_valid;
    
    assign A_ready = !A_valid;
    assign B_ready = !B_valid;

    always @(posedge clk or negedge reset_n) begin
        if (!reset_n) begin
            A_valid <= 0;
            B_valid <= 0;
            Y_enable <= 0;
        end
        else begin
            // Capture inputs when enabled
            if (A_enable && A_ready) A_valid <= 1;
            if (B_enable && B_ready) B_valid <= 1;
            
            // Compute XOR when both inputs are valid
            if (A_valid && B_valid) begin
                Y_data <= A_data ^ B_data;  // Correct XOR operation
                Y_enable <= 1;
                A_valid <= 0;
                B_valid <= 0;
            end
            
            // Clear output when consumed
            if (Y_enable && Y_ready) begin
                Y_enable <= 0;
            end
        end
    end

    // VCD Dumping for waveform generation
    `ifdef COCOTB_SIM
    initial begin
        $dumpfile("tests/delayed_dut.vcd");  // VCD file saved in tests/ directory
        $dumpvars(0, delayed_dut);           // Dump all variables in this module
        #1;
    end
    `endif
endmodule
