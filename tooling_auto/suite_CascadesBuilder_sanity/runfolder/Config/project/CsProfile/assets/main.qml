// Default empty project template
import bb.cascades 1.0
import "myJS.js" as JS

// creates one page with a label
Page {
    Container {
        Label {
            id: l1
        }
        ImageView {
            imageSource: "asset:///1.png"
        }
        //add MyBtn{} here
        
    }
    onCreationCompleted: {
        l1.text = JS.foo();
    }
    
}
