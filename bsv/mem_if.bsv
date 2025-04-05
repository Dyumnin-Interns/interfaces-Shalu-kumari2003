interface MemIfc;
    method Action readReq(Bit#(3) addr);
    method ActionValue#(Bit#(1)) readResp();
    method Action writeReq(Bit#(3) addr, Bit#(1) data);
    method Bool writeReady();
endinterface
