function Module() {
    'use asm';
    function f() {
        arr();
    }

    function g() {
    }

    var arr = [g];
    return f;
}

let f = Module();
f();

