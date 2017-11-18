import bb.cascades 1.0
Page {
Container {
Label {
id: l1
text: "Hello"
}
onCreationCompleted: {
update();
}
function update() {
var x = 10;
x ++;
x --;
l1.text = "debug"
var y = 18;
y = x + y;
l1.text = "done";
y ++;
}
}
}