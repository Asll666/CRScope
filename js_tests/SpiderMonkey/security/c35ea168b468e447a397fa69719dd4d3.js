var w = new WeakMap();
var g = newGlobal();
var k = g.eval('for (var i=0;i<100000;i++) new Object(); var q = new Object(); dumpObject(q); q');
dumpObject(k);
w.set(k, {});
k = null;

print('first gc...');
gc();
gc();
g.eval('q = null');
print('comp gc');
gc(g);
gc(g);
gc(g);
gc(g);
gc(g);
gc(g);
print('last gc');
gc();