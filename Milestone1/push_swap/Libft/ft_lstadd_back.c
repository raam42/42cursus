/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_back.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/29 00:23:55 by rodri             #+#    #+#             */
/*   Updated: 2026/02/02 18:21:46 by roandres         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstadd_back(t_list **lst, t_list *new)
{
	t_list	*node;

	node = *lst;
	if (!*lst)
	{
		new->next = NULL;
		*lst = new;
		return ;
	}
	while (node->next != NULL)
	{
		node = node->next;
	}
	node->next = new;
}
