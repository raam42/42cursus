NAME = libftprintf.a

CC = cc
CFLAGS = -Wall -Wextra -Werror -I. -I./libft

LIBFT_DIR = ./libft
LIBFT = $(LIBFT_DIR)/libft.a

SRCS = \
	ft_printf.c

OBJS = $(SRCS:.c=.o)

BONUS_SRCS = \
	ft_parse_bonus.c \
	ft_bonus_utils.c \
	ft_bonus_utils2.c \
	ft_bonus_print_core.c \
	ft_bonus_layout.c \
	ft_bonus_print_num.c \
	ft_bonus_hex_layout.c \
	ft_bonus_ptr_layout.c \
	ft_bonus_print_hex_ptr.c \
	ft_handle_convert_bonus.c

BONUS_OBJS = $(BONUS_SRCS:.c=.o)

all: $(NAME)

$(LIBFT):
	@$(MAKE) -C $(LIBFT_DIR)

$(NAME): $(LIBFT) $(OBJS) $(BONUS_OBJS)
	@cp $(LIBFT) $(NAME)
	@ar rcs $(NAME) $(OBJS) $(BONUS_OBJS)

bonus: $(NAME)

.c.o:
	@$(CC) $(CFLAGS) -c $< -o $@

clean:
	@rm -f $(OBJS) $(BONUS_OBJS)
	@$(MAKE) -C $(LIBFT_DIR) clean

fclean: clean
	@rm -f $(NAME)
	@$(MAKE) -C $(LIBFT_DIR) fclean

re: fclean all

.PHONY: all bonus clean fclean re
