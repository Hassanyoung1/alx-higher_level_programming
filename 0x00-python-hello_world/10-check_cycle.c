#include "lists.h"
/**
 *check_cycle - checks if a singly linked list has a cycle in it.
 *@list: list to check
 *Return: 0 if there is no cycle, 1 if there is a cycle
 */


int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *tail = list;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	while (head != NULL && head->next != NULL)
	{
		tail = tail->next;
		head = head->next->next;

		if (tail == head)
		{
			return (1);
		}
	}
	return (0);
}
