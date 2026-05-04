NAME = get_next_line.a
CC = cc
CFLAGS = -Wall -Wextra -Werror
HEADER = get_next_line.h

SRCS = \
    get_next_line.c \
    gnl_utils.c

OBJS = $(SRCS:.c=.o)

BONUS_SRCS = \
    get_next_line_bonus.c \
    get_next_line_utils_bonus.c

BONUS_OBJS = $(BONUS_SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
	ar rcs $(NAME) $(OBJS)

bonus: $(BONUS_OBJS)
	ar rcs $(NAME) $(BONUS_OBJS)

clean:
	rm -f $(OBJS) $(BONUS_OBJS)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all bonus clean fclean re
