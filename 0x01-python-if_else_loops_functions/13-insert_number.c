#include "lists.h"
#include <stdio.h>
/**
 * insert_node - insertar nodo
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp = *head, *next;

	new = malloc(sizeof(listint_t));
	if (new == NULL || *head == NULL)
		return (NULL);
	next = temp->next;
	if (temp->n > number)
	{
		new->n = number;
		new->next = temp;
		*head = new;
		return (new);
	}
	while (next != NULL)
	{
		if (next->n > number)
		{
			new->n = number;
			temp->next = new;
			new->next = next;
			return (new);
		}
		temp = temp->next;
		next = temp->next;
	}
	new->n = number;
	temp->next = new;
	new->next = NULL;
	return (new);
}
