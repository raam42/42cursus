NAME	= libftprintf.a
LIBFT	= libft
CC		= cc 
CFLAGS	= -Wall -Wextra -Werror 
AR		= ar rcs
RM		= rm -f

SRCS	=	ft_printf.c \
			ft_printf_utils.c \
			ft_printf_numbers.c \
			ft_printf_ptr.c

OBJS	= $(SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
		make -C $(LIBFT)
		cp libft/libft.a $(NAME)
		$(AR) $(NAME) $(OBJS)

%.o: %.c
			$(CC) $(CFLAGS) -c $< -o $@

clean:
		$(RM) $(OBJS)
		make -C $(LIBFT) clean

fclean: clean
		$(RM) $(NAME)
		make -C $(LIBFT) fclean

re: fclean all

.PHONY: all clean fclean re

		
