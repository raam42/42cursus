#include "ft_printf.h"
#include <limits.h>

int	main(void)
{
	int	ft_len;
	int	std_len;

	printf("--- 42 MADRID FT_PRINTF EVALUATION TESTER ---\n\n");

	/* 1. Basic Strings and Chars */
	ft_len = ft_printf("Mine: %c %s %%\n", 'G', "Hello 42");
	std_len = printf("Real: %c %s %%\n", 'G', "Hello 42");
	printf("Return -> Mine: %d | Real: %d\n\n", ft_len, std_len);

	/* 2. Integers and Unsigned (Edge Cases) */
	ft_len = ft_printf("Mine: %d %i %u\n", INT_MIN, INT_MAX, UINT_MAX);
	std_len = printf("Real: %d %i %u\n", INT_MIN, INT_MAX, UINT_MAX);
	printf("Return -> Mine: %d | Real: %d\n\n", ft_len, std_len);

	/* 3. Hexadecimal (Lowercase and Uppercase) */
	ft_len = ft_printf("Mine: %x %X %x\n", 0, 255, 4224242);
	std_len = printf("Real: %x %X %x\n", 0, 255, 4224242);
	printf("Return -> Mine: %d | Real: %d\n\n", ft_len, std_len);

	/* 4. Pointers (The Nil Case) */
	ft_len = ft_printf("Mine: %p %p\n", &ft_len, NULL);
	std_len = printf("Real: %p %p\n", &ft_len, NULL);
	printf("Return -> Mine: %d | Real: %d\n\n", ft_len, std_len);

	return (0);
}