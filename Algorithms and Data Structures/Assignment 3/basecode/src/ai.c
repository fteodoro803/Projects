#include <time.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>

#include "ai.h"
#include "utils.h"
#include "hashtable.h"
#include "stack.h"
#include "list.h"


void copy_state(state_t* dst, state_t* src){   //use this for duplicate states onto nodes
	
	//Copy field
	memcpy( dst->field, src->field, SIZE*SIZE*sizeof(int8_t) );

	dst->cursor = src->cursor;
	dst->selected = src->selected;
}

/**
 * Saves the path up to the node as the best solution found so far
*/
void save_solution( node_t* solution_node ){
	node_t* n = solution_node;
	while( n->parent != NULL ){
		copy_state( &(solution[n->depth]), &(n->state) );
		solution_moves[n->depth-1] = n->move;

		n = n->parent;
	}
	solution_size = solution_node->depth;
}


node_t* create_init_node( state_t* init_state ){ //ORIGINAL
	node_t * new_n = (node_t *) malloc(sizeof(node_t));
	new_n->parent = NULL;	
	new_n->depth = 0;
	copy_state(&(new_n->state), init_state);

	return new_n;
}

/**
 * Apply an action to node n and return a new node resulting from executing the action
*/

node_t* applyAction(node_t* n, position_s* selected_peg, move_t action ){

    node_t* new_node = NULL;

	//FILL IN MISSING CODE
	new_node = malloc(sizeof(node_t));
    new_node->state = n->state; //state will be updated anyway at execute move
    new_node->depth = n->depth + 1;
    new_node->move = action; //im not sure about what this is and what it does TEST
    new_node->parent = n;
    new_node->state.cursor = *selected_peg;
	
    execute_move_t( &(new_node->state), selected_peg, action );

	return new_node;

}

/**
 * Find a solution path as per algorithm description in the handout
 */

void find_solution( state_t* init_state  ){ // (pseudocode line 1)

	HashTable table;
    list_t  nodeList = createList(); // to keep track of generated and expanded Nodes

	// Choose initial capacity of PRIME NUMBER
	// Specify the size of the keys and values you want to store once 
	ht_setup( &table, sizeof(int8_t) * SIZE * SIZE, sizeof(int8_t) * SIZE * SIZE, 16769023);

    // Initialize Stack
	initialize_stack();

	//Add the initial node
	node_t* n = create_init_node( init_state ); //(pseudocode line 2)
    nodeList = ll_insert(n, nodeList); //inserts to Node List

    /* FILL IN THE GRAPH ALGORITHM */

	stack_push(n); //(pseudocode line 3)

	int numRemainingPegs = num_pegs(init_state); //(pseudocode line 4)

	//TESTING PURPOSES
	int numInitialPegs=0;

    while (!is_stack_empty()){ //(pseudocode line 5)
        n = stack_top(); //(pseudocode line 6a)
        stack_pop();//(pseudocode line 6b)
        expanded_nodes += 1; //(pseudocode line 7)

        //Found a Better Solution
        if (num_pegs(&n->state) < numRemainingPegs) {//(pseudocode line 8)
            save_solution(n); //(pseudocode line 9)
            numRemainingPegs = num_pegs(&n->state); //(pseudocode line 10)
        } //(pseudocode line 11)

        //Goes through every possible Action
        for (int x=0; x<SIZE; x++) { //(pseudocode line 12a: x axis)
            for (int y=0; y<SIZE; y++) { //(12b: y axis)

                /*//TESTING PURPOSES
                //Checking Initial Number of Pegs
                if (n->state.field[x][y] == 'o') {
                    numInitialPegs += 1;
                }*/

                //TESTING START HERE /* TESTING PURPOSES, CHECKING INITIAL NODES ABOVE
                for (int direction=0; direction<NUM_DIRECTIONS; direction++) { //(pseudocode line 12c: peg directions)
                    if (n->state.field[x][y] == 'o') { //(pseudocode line 12d: current cursor position)
                        position_s currPeg;
                        currPeg.x = x;
                        currPeg.y = y;

                        //Checks for Legal Actions and Applies them
                        if (can_apply(&n->state, &currPeg, direction)) { //(pseudocode line 13)
                            node_t *newNode = applyAction(n, &currPeg, direction); //(pseudocode line 14)
                            nodeList = ll_insert(newNode, nodeList);
                            generated_nodes += 1; //(pseudocode line 15)

                            if (won(&newNode->state)) { //(pseudocode line 16)
                                save_solution(newNode); //(pseudocode line 17)
                                numRemainingPegs = num_pegs(&newNode->state); //(pseudocode line 18)

                                // Frees
                                free_list(nodeList);
                                ht_destroy(&table);

                                return; //(pseudocode line 19)
                            } //(20)
                            if (!ht_contains(&table, &newNode->state.field)) { //(pseudocode line 21)
                                ht_insert(&table, &newNode->state.field, newNode->state.field); //state to hash table
                                stack_push(newNode); //(pseudocode line 22)
                            } //(pseudocode line 23)
                        } //(pseudocode line 24)

                    }
                } //(pseudocode line 25a: end if - direction)
                 // TESTING END OF COMMENT HERE
            } //(pseudocode line 25b: end if - y)
        } //(pseudocode line 25c: end if - x)

        //Checks if Out-of-Budget
        if (expanded_nodes >= budget) { //(pseudocode line 26)
            free_list(nodeList);
            ht_destroy(&table);
            return; //(pseudocode line 27)
        } //(pseudocode line 28)
    } //(pseudocode line 29)
    printf("\n\nNUM INITIAL PEGS: %d\n\n", numInitialPegs);
}
