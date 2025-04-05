interface Mem_ifc;
    // Read interface
    method Action read(Bit#(3) read_address);
    method Bit#(1) read_data;
    method Bit#(1) read_rdy;
    
    // Write interface
    method Action write(Bit#(3) write_address, Bit#(1) write_data);
    method Bit#(1) write_rdy;
endinterface
