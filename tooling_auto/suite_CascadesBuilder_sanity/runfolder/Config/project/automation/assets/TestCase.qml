import bb.cascades 1.0
import "global.js" as GlobalResource

Container {
    id: testCase
    minHeight: 500
    background: Color.DarkGray
    objectName: "testcase"
    visible: ! test.automode
    property string name
    property string expect
    verticalAlignment: VerticalAlignment.Bottom
    layout: StackLayout {
        orientation: LayoutOrientation.TopToBottom
    }
    TextArea {
        id: expectId
        backgroundVisible: true
        objectName: "expectId"
        text: "expect"
        editable: false
        maxHeight: 450
        minHeight: 450
        textStyle {
            fontWeight: FontWeight.Bold
        }
        animations: [
            FadeTransition {
                id: fade
                duration: 800
                easingCurve: StockCurve.CubicOut
                fromOpacity: 0
                toOpacity: 1
                onEnded: {
                    toggle_buttons();
                    //runnext();
                }
            }
        ]
    }
    Container {
        Container {
            layout: StackLayout {
                orientation: LayoutOrientation.LeftToRight
            }
            Button {
                leftMargin: 10
                id: passId
                text: "Pass"
                imageSource: "images/pass.jpg"
                objectName: "passId"
                onClicked: {
                    TestResult.pushResult(TestResult.Pass); // pass
                    toggle_buttons();
                    runnext();
                }
            }
            Button {
                leftMargin: 10
                id: failId
                text: "Fail"
                imageSource: "images/error.png"
                objectName: "failId"
                onClicked: {
                    TestResult.pushResult(TestResult.Fail); // fail
                    toggle_buttons();
                    runnext();
                }
            }
            Button {
                leftMargin: 10
                id: skipId
                text: "Skip"
                imageSource: "images/skip.jpg"
                objectName: "skipId"
                onClicked: {
                    TestResult.pushResult(TestResult.Skip); // skip
                    toggle_buttons();
                    runnext();
                }
            }
        }
    }
    function log_result(result, msg) {
        TestResult.testDescription = msg;
        if (result) {
            TestResult.pushResult(TestResult.Pass);
            // pass
        } else {
            TestResult.pushResult(TestResult.Fail); // failure
        }
    }
    function isDefined(someVar, msg) {
        log_result(! (typeof someVar === 'undefined'), msg);
    }
    function isUndefined(someVar, msg) {
        log_result(typeof someVar === 'undefined', msg + " but it is " + someVar);
    }
    function isNull(someVar, msg) {
        log_result(someVar === null, msg);
    }
    function isString(someVar, msg) {
        log_result(typeof someVar === 'string', msg + " but is is " + (typeof someVar));
    }
    function stringContains(source, target) {
        log_result(source.indexOf(target) != -1, "'" + source + "' should contain: '" + target + "'");
    }
    function isNumber(someVar, msg) {
        log_result(typeof someVar === 'number' && isFinite(someVar), msg + " but it is " + (typeof someVar));
    }
    function isEqual(actual, expect) {
        log_result(actual === expect || actual == expect || (""+actual)==(""+expect), "expect: '" + expect + "' actual: '" + actual + "'");
    }
    function isBoolean(someVar, msg) {
        log_result(typeof someVar === 'boolean', msg + " but is is " + (typeof someVar));
    }
    function setExpect(msg) {
        TestResult.testDescription = msg;
    }
    
    function setMksId(id) {
        TestResult.mksId = id;
        
    }
    
    function toggle_buttons() {
        passId.enabled = ! passId.enabled;
        failId.enabled = ! failId.enabled;
        skipId.enabled = ! skipId.enabled;
    }
    
    // sleep millsecs on main thread   
    function wait(ms) {
     test.cwait(ms);   
    }
    
    function runnext() {
        GlobalResource.testindex ++;
        if (GlobalResource.testindex >= GlobalResource.testList.length) {
            test.nextqml();
        } else {
            var prop = GlobalResource.testList[GlobalResource.testindex];
            TestResult.functionName = prop;
            try {
                testCase[prop]();
                expectId.text = "TestCase:\n" + name + "\n\n" + "Test Function:\n" + TestResult.functionName + "\n\n Status:\n" + TestResult.status + "\n" + "MKS:\n"+TestResult.mksId +"\n" + "Instruction:\n" +TestResult.testDescription ;
                fade.play();
            } catch (e) {
                expectId.text = "EXCEPTIONS: " + e.message + "\n\n" + expectId.text;
            }
        }
    }
    function start() {
        // automation
        console.log("test.automode: " + test.automode);
        TestResult.testCaseName = name;
        GlobalResource.testList = [
        ];
        GlobalResource.testindex = 0;

        // looking for all valid function
        for (var prop in testCase) {
            
               if (test.automode && prop.indexOf("automation_") != 0 || ! test.automode && prop.indexOf("manual_") != 0) {
                   continue;
               }
           // if (prop.indexOf("automation_") != 0 && prop.indexOf("manual_") != 0) {
           //     continue;
           // }
            GlobalResource.testList.push(prop);
            console.log("add function: " + prop);
        }
        GlobalResource.testList.sort();
        if (test.automode) {
            for (var index in GlobalResource.testList) {
                var prop = GlobalResource.testList[index];
                console.log(prop);
                TestResult.functionName = prop;
                try {
                    testCase[prop]();
                } catch (e) {
                    TestResult.exceptionHandle(e.message); // exception handle
                    
                }
            }
            test.emmitdone(); // continue next qml test
        } else {
            // manual test
            GlobalResource.testindex = 0;
            if (GlobalResource.testList.length == 0) {
                expectId.text = "TestCase:" + name + "\n\n" + " Warn : There is no function to run !!";
                passId.visible = false;
                skipId.visible = false;
                failId.text = "Continue";
            } else {
                // start first function
                var prop = GlobalResource.testList[GlobalResource.testindex];
                TestResult.functionName = prop;
                try {
                  testCase[prop]();
                  expectId.text = "TestCase:\n" + name + "\n\n" + "Test Function:\n" + TestResult.functionName + "\n\n Status:\n" + TestResult.status + "\n" + "MKS:\n"+TestResult.mksId +"\n" + "Instruction:\n" +TestResult.testDescription ;
                } catch (e) {
                    expectId.text = "EXCEPTIONS: " + e.message + "\n\n" + expectId.text;
                }
            }
        }
    }
    onCreationCompleted: {
        // if (! test.automode) start();
        if (test.automode && ! test.attach_screen) start();
    }
}
