#include "list.h"
#include "utils.h"
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>


list_t createList() {
    return NULL;
}

// insert at start
list_t ll_insert(node_t *data, list_t l) {

    llnode_t *node= my_malloc(sizeof(*node));
    node->data= data;
    node->next=l;

    return node;
}


void free_list(list_t l){
    llnode_t *p= l;
    while (p != NULL) {
        llnode_t *t= p;
        p= p->next;
        if (t != NULL) {
            if (t->data != NULL) {
                free(t->data);
                free(t);
            }
        }
    }
}

void *my_malloc(size_t n){
    assert(n>0);
    void *p= malloc(n);
    assert(p);
    return p;
}

/* EXTERNAL CODE REFERENCES 
	ll_insert() adapted from listops.c, from "Programming, Problem Solving, 
            and Abstraction with C by Alistair Moffat", 2012, by Alistair Moffat
	free_list() adapted from listops.c, from "Programming, Problem Solving, 
            and Abstraction with C by Alistair Moffat", 2012, by Alistair Moffat
	my_malloc() adapted from utils.c, from COMP20003 avo ass3 solution, by Anh Vo
*/