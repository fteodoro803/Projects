/* Mostly adapted from Alistairs listops */

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
