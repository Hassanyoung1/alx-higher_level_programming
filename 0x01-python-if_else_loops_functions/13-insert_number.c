#include "lists.h"

/**
 * insert_node - inserts a number in a sorted linked list
 *
 * @head: pointer to the head of the list
 * @number: number to be inserted
 * Return: Address of new node, NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ahead;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	ahead = *head;
	new_node->n = number;
	new_node->next = NULL;

	if (ahead == NULL || number <= ahead->n)
	{
		new_node->next = ahead;
		*head = new_node;
		return (*head);
	}

	while (ahead->next != NULL && ahead->next->n < number)
	{
		ahead = ahead->next;
	}

	new_node->next = ahead->next;
	ahead->next = new_node;

	return (*head);
}
