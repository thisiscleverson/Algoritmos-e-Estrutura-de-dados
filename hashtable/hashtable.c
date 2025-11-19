#include <stdio.h>
#include <stdlib.h>


typedef struct node{
	int data;
	struct node *prev;
	struct node *next;
} Node;


typedef struct {
	Node* head;
} DoublyLinkedList;


// Closed Address
typedef struct{
	int size;
    DoublyLinkedList** table; 
} HashTableClosed;


int hash_function(int k, int hash_size){
	return k % hash_size;
}


Node* create_node(int data){
	Node* new_node = (Node*)malloc(sizeof(Node));

	if(new_node == NULL){
        printf("Error creating a new node.\n");
        exit(0);
    }

	new_node->data = data;
	new_node->prev = NULL;
    new_node->next = NULL;

	return new_node;
}


Node* searchDoublyLinkedList(int data, DoublyLinkedList* list){
	Node* current = list->head;

	if(current != NULL){
		while(current != NULL && current->data != data){
			current = current->next;
		}
	}else{
		printf("list is empty!");
	}
	
	return current;
}

void append(Node* node, DoublyLinkedList* list){
	node->next = list->head;
	if(list->head != NULL)
		list->head->prev = node;
	list->head = node;
}

HashTableClosed* create_table(int size){
	HashTableClosed* table = malloc(sizeof(HashTableClosed));
	table->size = size;

	table->table = malloc(size * sizeof(HashTableClosed));

	for(int i=0; i<size; i++){
		table->table[i] = malloc(sizeof(DoublyLinkedList));
		table->table[i]->head = NULL;
	}

	return table;
}


Node* searchHashTableClosed(int data, HashTableClosed* hash_table){
	int key = hash_function(data, hash_table->size);
	DoublyLinkedList* list = hash_table->table[key];
	return searchDoublyLinkedList(data, list);
}


void insertHashTableClosed(Node* node, HashTableClosed* hash_table){
	int key = hash_function(node->data, hash_table->size);
	DoublyLinkedList* list = hash_table->table[key];
	append(node, list);
}


int main(){
	HashTableClosed* my_hash_table = create_table(7);

	Node* node = create_node(1);
	Node* anotherNode = create_node(8);
	
	insertHashTableClosed(node, my_hash_table);
	insertHashTableClosed(anotherNode, my_hash_table);

	Node* result = searchHashTableClosed(8, my_hash_table);

	printf("%d\n", result->data);

	return 0;
}
