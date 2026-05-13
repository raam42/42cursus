/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstsize.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rodri <rodri@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/28 23:06:26 by rodri             #+#    #+#             */
/*   Updated: 2026/01/29 03:26:34 by rodri            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_lstsize(t_list *lst)
{
	size_t	len;
	t_list	*node;

	if (!lst)
		return (0);
	len = 0;
	node = lst;
	while (node)
	{
		len++;
		node = node->next;
	}
	return (len);
}
