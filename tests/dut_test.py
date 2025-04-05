module dut_test;
    reg CLK;
    reg RST_N;
    reg [2:0] read_address;
    wire [0:0] read_data;
    wire read_rdy;
    reg read_en;
    wire write_rdy;
    reg [2:0] write_address;
    reg [0:0] write_data;
    reg write_en;
    
    dut DUT (
        .CLK(CLK),
        .RST_N(RST_N),
        .read_address(read_address),
        .read_data(read_data),
        .read_rdy(read_rdy),
        .read_en(read_en),
        .write_rdy(write_rdy),
        .write_address(write_address),
        .write_data(write_data),
        .write_en(write_en)
    );
    
    initial begin
        $dumpfile("dut_test.vcd");
        $dumpvars(0, dut_test);
        
        // Initialize
        CLK = 0;
        RST_N = 0;
        read_en = 0;
        write_en = 0;
        #10 RST_N = 1;
        
        // Test case 1: 0 XOR 0 = 0
        #10 write_address = 4; write_data = 0; write_en = 1;
        #10 write_en = 0;
        #10 write_address = 5; write_data = 0; write_en = 1;
        #10 write_en = 0;
        #10 read_address = 3; read_en = 1;
        #10 read_en = 0;
        if (read_data == 0) $display("Test 1: PASS (0 XOR 0 = 0)");
        else $display("Test 1: FAIL");
        
        // Test case 2: 0 XOR 1 = 1
        #10 write_address = 4; write_data = 0; write_en = 1;
        #10 write_en = 0;
        #10 write_address = 5; write_data = 1; write_en = 1;
        #10 write_en = 0;
        #10 read_address = 3; read_en = 1;
        #10 read_en = 0;
        if (read_data == 1) $display("Test 2: PASS (0 XOR 1 = 1)");
        else $display("Test 2: FAIL");
        
        // Test case 3: 1 XOR 1 = 0
        #10 write_address = 4; write_data = 1; write_en = 1;
        #10 write_en = 0;
        #10 write_address = 5; write_data = 1; write_en = 1;
        #10 write_en = 0;
        #10 read_address = 3; read_en = 1;
        #10 read_en = 0;
        if (read_data == 0) $display("Test 3: PASS (1 XOR 1 = 0)");
        else $display("Test 3: FAIL");
        
        #100 $finish;
    end
    
    always #5 CLK = ~CLK;
endmodule
