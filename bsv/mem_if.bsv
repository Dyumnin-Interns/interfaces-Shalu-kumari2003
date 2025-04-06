interface Mem_If;
    method Action put(Bit#(1) data);
    method ActionValue#(Bit#(1)) get();
endinterface
