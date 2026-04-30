NAME = libftprintf.a

CC = cc
CFLAGS = -Wall -Wextra -Werror

# =======================
# LIBFT
# =======================

LIBFT_DIR = libft
LIBFT = $(LIBFT_DIR)/libft.a

# =======================
# MANDATORY SOURCES
# =======================

SRCS = \
    ft_printf.c \
    ft_print_char.c \
    ft_print_str.c \
    ft_print_int.c \
    ft_print_uint.c \
    ft_print_hex.c \
    ft_print_ptr.c

OBJS = $(SRCS:.c=.o)

# =======================
# BONUS SOURCES
# =======================

BONUS_SRCS = \
    ft_printf_bonus.c \
    ft_parse_bonus_bonus.c \
    ft_bonus_utils_bonus.c \
    ft_bonus_utils2_bonus.c \
    ft_bonus_print_core_bonus.c \
    ft_bonus_layout_bonus.c \
    ft_bonus_print_num_bonus.c \
    ft_bonus_hex_layout_bonus.c \
    ft_bonus_ptr_layout_bonus.c \
    ft_handle_conversion_bonus_bonus.c

BONUS_OBJS = $(BONUS_SRCS:.c=.o)

# =======================
# RULES
# =======================

all: $(NAME)

$(LIBFT):
    $(MAKE) -C $(LIBFT_DIR)

$(NAME): $(LIBFT) $(OBJS)
    cp $(LIBFT) $(NAME)
    ar rcs $(NAME) $(OBJS)

bonus: $(LIBFT) $(OBJS) $(BONUS_OBJS)
    cp $(LIBFT) $(NAME)
    ar rcs $(NAME) $(OBJS) $(BONUS_OBJS)

clean:
    rm -f $(OBJS) $(BONUS_OBJS)
    $(MAKE) -C $(LIBFT_DIR) clean

fclean: clean
    rm -f $(NAME)
    $(MAKE) -C $(LIBFT_DIR) fclean

re: fclean all

.PHONY: all bonus clean fclean re
