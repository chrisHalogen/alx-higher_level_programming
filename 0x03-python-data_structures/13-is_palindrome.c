#include "lists.h"

/**
 * is_palindrome - check for a palindrome sll
 * @head: pointer to the head
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *sll = *head;
	int buff[10240], alpha = 0, tail = 0;

	if (!*head || !((*head)->next))
		return (1);

	while (sll)
	{
		buff[tail] = sll->n;
		sll = sll->next;
		tail++;
	}

	tail--;

	while (alpha <= tail / 2)
	{
		if (buff[alpha] != buff[tail - alpha])
			return (0);
		alpha++;
	}

	return (1);
}