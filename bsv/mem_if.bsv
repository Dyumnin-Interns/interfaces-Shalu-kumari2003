// BSV/mem_if.bsv
package MemIfc;

interface MemIfc;
    method Action put(Bit#(1) a, Bit#(1) b);
    method Bit#(1) get();
endinterface

module mkXOR(MemIfc);
    Reg#(Bit#(1)) x <- mkReg(0);
    Reg#(Bit#(1)) y <- mkReg(0);
    Reg#(Bit#(1)) out <- mkReg(0);

    rule compute;
        out <= x ^ y;
    endrule

    method Action put(Bit#(1) a, Bit#(1) b);
        x <= a;
        y <= b;
    endmethod

    method Bit#(1) get();
        return out;
    endmethod
endmodule

endpackage
