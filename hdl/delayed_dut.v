module delayed_dut (
    input clk,
    input reset_n,
    input A_data,
    input A_enable,
    output A_ready,
    input B_data,
    input B_enable,
    output B_ready,
    output Y_data,
    output Y_enable,
    input Y_ready
);
    reg A_reg, B_reg;
    reg Y_reg;
    reg Y_valid;

    assign A_ready = !Y_valid;
    assign B_ready = !Y_valid;
    assign Y_data = Y_reg;
    assign Y_enable = Y_valid;

    always @(posedge clk or negedge reset_n) begin
        if (!reset_n) begin
            A_reg <= 0;
            B_reg <= 0;
            Y_reg <= 0;
            Y_valid <= 0;
        end
        else begin
            if (A_enable && A_ready) A_reg <= A_data;
            if (B_enable && B_ready) B_reg <= B_data;
            if (A_enable || B_enable) begin
                Y_reg <= A_reg ^ B_reg;  // XOR Operation
                Y_valid <= 1;
            end
            else if (Y_enable && Y_ready) begin
                Y_valid <= 0;
            end
        end
    end
endmodule
