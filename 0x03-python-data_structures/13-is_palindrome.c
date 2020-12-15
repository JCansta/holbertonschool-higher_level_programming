#include "lists.h"
#include <stdio.h>
/**
 * check_palindrome - check if palindrome
 * @temp: the head of the list
 * @count: the len of the list
 * Return: 1 or 0
 */
int check_palindrome(listint_t *temp, int count)
{
	int list[count];
	int ch = 0, end = count - 1;

	while (temp)
	{
		list[ch] = temp->n;
		temp = temp->next;
		ch++;
	}
	ch = 0;
	while (ch <= end)
	{
		if (list[ch] != list[end])
			return (0);
		ch++;
		end--;
	}
	return (1);
}
/**
 * is_palindrome - check if linked list is palindrome
 * @head: the head of the list
 * Return: 1 if yes 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int count = 0, check;

	if (temp == NULL)
		return (1);
	while (temp)
	{
		count++;
		temp = temp->next;
	}
	temp = *head;
	check = check_palindrome(temp, count);
	return (check);
}
