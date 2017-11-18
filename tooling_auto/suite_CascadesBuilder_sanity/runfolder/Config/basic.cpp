#include "applicationui.hpp"
#include <bb/cascades/Application>
#include <bb/cascades/QmlDocument>
#include <bb/cascades/AbstractPane>
#include <iostream.h>

using namespace bb::cascades;

ApplicationUI::ApplicationUI(bb::cascades::Application *app) :
		QObject(app) {
	char char_c('c');
	bool bool_true(true);
	char* char_p = &char_c;
	/* string string_s("string");
	string* string_p = &string_s; */
	int myints[] = { 1, 2, 3, 4 };
	string mystrings[] = { "string1", "string2" };
	QmlDocument *qml = QmlDocument::create("asset:///main.qml").parent(this);
	AbstractPane *root = qml->createRootObject<AbstractPane>();
	app->setScene(root);
}

void ApplicationUI::onSystemLanguageChanged()
{
    
}