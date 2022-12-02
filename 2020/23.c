#include <stdlib.h>
#include <stdio.h>

typedef struct node_t
{
    int value;
    struct node_t *next;
} node_t;

int main()
{

    int min_val = 1;
    int max_value = 1000000;

    int starting_list[] = {1, 6, 7, 2, 4, 8, 3, 5, 9};

    node_t *starting_node = (node_t *)malloc(sizeof(node_t));

    starting_node->value = 1;

    node_t *dict_labels[1000005]; // boh, sai mai

    dict_labels[1] = starting_node;

    node_t *current_node = starting_node;

    for (size_t i = 1; i < 9; i++)
    {
        node_t *new_node;
        new_node = calloc(1, sizeof(node_t));
        new_node->value = starting_list[i];
        ((node_t **)dict_labels)[starting_list[i * 1]] = new_node;
        current_node->next = new_node;
        current_node = current_node->next;
    }

    for (size_t i = 10; i < 1000001; i++)
    {
        node_t *new_node;
        new_node = calloc(1, sizeof(node_t));
        new_node->value = i;
        dict_labels[i] = new_node;
        current_node->next = new_node;
        current_node = current_node->next;
    }

    current_node->next = starting_node;

    current_node = starting_node;
    for (size_t i = 0; i < 10000000; i++)
    {
        int current_value = current_node->value;
        node_t *c1 = current_node->next;
        node_t *c2 = c1->next;
        node_t *c3 = c2->next;

        int val1 = c1->value;
        int val2 = c2->value;
        int val3 = c3->value;

        current_node->next = c3->next;

        int flag = 1;
        current_value -= 1;
        while (flag)
        {
            if (current_value == val1 || current_value == val2 || current_value == val3)
            {
                current_value -= 1;
                if (current_value < min_val)
                {
                    current_value = max_value;
                }
            }
            else
            {
                if (current_value == 0)
                {
                    current_value = max_value;
                }
                else
                {
                    flag = 0;
                }
            }
        }
        node_t *destination_cup = dict_labels[current_value];
        node_t *old_next = destination_cup->next;

        destination_cup->next = c1;

        c3->next = old_next;

        current_node = current_node->next;
    }

    printf("%d\n", ((node_t **)dict_labels)[1]->next->value);
    printf("%d\n", ((node_t **)dict_labels)[1]->next->next->value);
}