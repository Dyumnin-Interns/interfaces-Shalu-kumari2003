module FIFO1 (
    input clk,
    input reset_n,
    input data_in,
    input enable_in,
    output ready_out,
    output data_out,
    output enable_out,
    input ready_in
);
    reg buffer;
    reg full;

    assign ready_out = !full;
    assign data_out = buffer;
    assign enable_out = full;

    always @(posedge clk or negedge reset_n) begin
        if (!reset_n) begin
            buffer <= 0;
            full <= 0;
        end
        else if (enable_in && ready_out) begin
            buffer <= data_in;
            full <= 1;
        end
        else if (enable_out && ready_in) begin
            full <= 0;
        end
    end
endmodule
