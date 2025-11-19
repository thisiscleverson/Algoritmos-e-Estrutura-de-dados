#include <stdio.h>
#include <stdlib.h>


typedef struct node{
	int data;
	struct node *next;
} t_node;


void append(t_node **head, int data);
int list_size(t_node *head);
int search(t_node *head, int data);
void print_list(t_node *head);


int main(){

	int size;


	t_node *head = NULL;
	
	size = list_size(head);
	printf("Init size: %d\n", size);
	
	append(&head, 1);
	append(&head, 2);
	append(&head, 3);
	append(&head, 4);

	int index = search(head, 2);
	printf("Search index return: %d\n", index);
	
	size = list_size(head);
	printf("End size: %d\n", size);

	

	print_list(head);
	
	return 0;
}


void append(t_node **head, int data){
    t_node *new_node = (t_node*)malloc(sizeof(t_node));

	if(new_node == NULL){
        printf("Error creating a new node.\n");
        exit(0);
    }

	new_node->data = data;
    new_node->next = NULL;
    
    
    if (*head == NULL) {
        *head = new_node;
        return;
    }
    
   
    t_node *current = *head;

	while (current->next != NULL) {
        current = current->next;
    }
    
    current->next = new_node;
}


void print_list(t_node *head){
	t_node *current = head;
	
	while(current != NULL){
		printf("%d\n", current->data);
		current = current->next;
	}
}


int list_size(t_node *head){
	int count = 0;

	t_node *current = head;

	while(current != NULL){
		count++;
		current = current->next;
	}

	return count;
}


int search(t_node *head, int data){
	int index = 0;
	t_node *current = head;
	
	while(current != NULL){
		if(current->data == data){
			return index;
		}
		current = current->next;
		index++;
	}
	
	return -1;
}
