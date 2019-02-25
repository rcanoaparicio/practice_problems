#include <iostream>

using namespace std;

struct Element {
	int value;
	uintptr_t both;
};

class XORList
{
public:
	XORList();
	XORList(Element* root);
	~XORList();

	void add(Element* element);
	Element* get(unsigned int index);

	Element* root;
	unsigned int length;

};

XORList::XORList()
{

}

XORList::XORList(Element* root)
{
	this->root = root;
	if (root != NULL)
		this->root->both = NULL;
		this->length++;
}


XORList::~XORList()
{
}

void XORList::add(Element * element)
{
	if (this->root != NULL) {
		uintptr_t prev = this->root->both ^ NULL;
		this->root->both = prev ^ (uintptr_t)element;
		element->both = (uintptr_t)this->root ^ NULL;
		this->root = element;
	}
	else {
		this->root = element;
		this->root->both = NULL ^ NULL;
	}
	++this->length;
}

Element* XORList::get(unsigned int index)
{
	int len = this->length - index - 1;
	Element* e = this->root;
	uintptr_t prev = NULL;
	for (int i = 0; i < len; ++i) {
		e = (Element*)(e->both ^ prev);
		prev = (int)e;
	}

	return e;
}

int main() {

	Element e{ 32 };
	XORList* list = new XORList(&e);

	int len = 4;
	for (int i = 0; i < len; ++i) {
		Element ei{ len - i };
		list->add(&ei);
	}

	cout << list->get(2)->value << endl;
	cout << list->get(3)->value << endl;
	cout << list->get(0)->value << endl;


	system("pause");
	return 0;

}
