#include "lists.h"  

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 * Return: 0 if not a palindrome, 1 if a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *ahead, *tail;
	int count = 0, a, b;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	ahead = tail = *head;

	while (ahead != NULL)
	{
		count++;
		ahead = ahead->next;
	}

	/* Reset ahead and tail to the start of the list */
	ahead = tail = *head;

	for (a = 0; a < count / 2; a++)
	{
		ahead = *head; /* Reset ahead to the head of the list */
		for (b = 0; b < count - a - 1; b++)
		{
			ahead = ahead->next;
		}
		if (tail->n != ahead->n)
			return (0);
		tail = tail->next;
	}

	return (1);
}
