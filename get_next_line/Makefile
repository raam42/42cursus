NAME = get_next_line.a
CC = cc
CFLAGS = -Wall -Wextra -Werror
HEADER = get_next_line.h

SRCS = \
    get_next_line.c \
    gnl_utils.c

OBJS = $(SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
    ar rcs $(NAME) $(OBJS)

clean:
    rm -f $(OBJS)

fclean: clean
    rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
