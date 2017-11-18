import bb.cascades 1.0
import "test.js" as A
Page {
Container {
Label {
id: l1
text: "Hello"
}
onCreationCompleted: {
 A.update();
}
}
}
