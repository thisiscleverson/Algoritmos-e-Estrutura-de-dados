#include <stdio.h>
#include <stdlib.h>

typedef struct node{
	int data;
	struct node *prev;
	struct node *next;
} t_node;


void append(t_node **head, int data){
    t_node *new_node = (t_node*)malloc(sizeof(t_node));

	if(new_node == NULL){
        printf("Error creating a new node.\n");
        exit(0);
    }

	new_node->data = data;
	new_node->prev = NULL;
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
	new_node->prev = current;
}

void print_list(t_node *head){
	t_node *cursor = head;

	while(cursor != NULL){
		printf("current node: %d\n", cursor->data);
		
		if(cursor->prev != NULL){
			printf("prev node: %d\n", cursor->prev->data);
		}else{
			printf("prev node: NULL\n");
		}

		if(cursor->next != NULL){
			printf("next node: %d\n\n", cursor->next->data);
		}else{
			printf("next node: NULL\n\n");
		}
		
		cursor = cursor->next;
	}
}

int main(){
	t_node *head = NULL;

	append(&head, 1);
	append(&head, 2);
	append(&head, 3);
	append(&head, 4);

	print_list(head);
	
	return 0;
}
