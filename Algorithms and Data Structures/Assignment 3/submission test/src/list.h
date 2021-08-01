/*
   this is Alistair's  listops.c
*/
#ifndef _LIST_
#define _LIST_

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include "utils.h"

typedef struct node llnode_t;

struct node {
    node_t *data;
    llnode_t *next;
};

typedef llnode_t *list_t;

list_t createList();
list_t ll_insert(node_t *d, list_t l);
void free_list(list_t l);
void *my_malloc(size_t n);

#endif