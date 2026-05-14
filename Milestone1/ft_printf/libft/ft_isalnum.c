/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_isalnum.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rodrigoa <rodrigoa@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 12:40:13 by rodrigoa          #+#    #+#             */
/*   Updated: 2026/01/27 15:01:01 by rodrigoa         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

int	ft_isalnum(int alph_num)
{
	if (ft_isalpha(alph_num) || ft_isdigit(alph_num))
		return (1);
	return (0);
}
