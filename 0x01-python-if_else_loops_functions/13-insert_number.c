#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - Insert a node in a SLL
 * @head: double pointer to the head
 * @number: contents of the node
 * Return: pointer to the node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *sll_pointer = *head;

	if (!new_node)
		return (NULL);

	new_node->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (sll_pointer->next)
	{
		if ((sll_pointer->next)->n >= number)
		{
			new_node->next = sll_pointer->next;
			sll_pointer->next = new_node;
			return (new_node);
		}
		sll_pointer = sll_pointer->next;
	}

	new_node->next = NULL;
	sll_pointer->next = new_node;

	return (new_node);
}
