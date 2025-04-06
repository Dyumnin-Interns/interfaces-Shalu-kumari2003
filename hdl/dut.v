module dut (
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
    // Instantiate FIFO1 for input A
    FIFO1 fifo_A (
        .clk(clk),
        .reset_n(reset_n),
        .data_in(A_data),
        .enable_in(A_enable),
        .ready_out(A_ready),
        .data_out(A_fifo_out),
        .enable_out(A_fifo_enable),
        .ready_in(A_fifo_ready)
    );

    // Instantiate FIFO1 for input B
    FIFO1 fifo_B (
        .clk(clk),
        .reset_n(reset_n),
        .data_in(B_data),
        .enable_in(B_enable),
        .ready_out(B_ready),
        .data_out(B_fifo_out),
        .enable_out(B_fifo_enable),
        .ready_in(B_fifo_ready)
    );

    // Instantiate delayed_dut (XOR Logic)
    delayed_dut xor_logic (
        .clk(clk),
        .reset_n(reset_n),
        .A_data(A_fifo_out),
        .A_enable(A_fifo_enable),
        .A_ready(A_fifo_ready),
        .B_data(B_fifo_out),
        .B_enable(B_fifo_enable),
        .B_ready(B_fifo_ready),
        .Y_data(Y_data),
        .Y_enable(Y_enable),
        .Y_ready(Y_ready)
    );
endmodule
