#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - check if the list have a loop
 * @list: the list to find the loop
 * Return: 1 if the list have a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle = list, *rabbit = list;

	while (list && turtle->next && rabbit->next && rabbit->next->next)
	{
		turtle = turtle->next;
		rabbit = rabbit->next->next;
		if (turtle == rabbit)
			return (1);
	}
	return (0);
}
