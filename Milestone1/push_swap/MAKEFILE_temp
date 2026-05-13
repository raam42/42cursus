NAME = push_swap
CC = cc
INC_FOLDER = inc

FLAGS = -Wall -Werror -Wextra

LIBFT_DIR = Libft
LIBFT = $(LIBFT_DIR)/libft.a

INC_FLAGS = -I $(INC_FOLDER) -I $(LIBFT_DIR)

SRC = src/main.c \
src/disorder.c \
src/flags.c \
src/index.c \
src/parser.c \
src/print_bench.c \
src/strategy.c \
src/moves/pushing.c \
src/moves/rotating.c \
src/moves/rrotating.c \
src/moves/swapping.c \
utils/complex_sort.c \
utils/linear_sort.c \
utils/medium_sort.c \
utils/simple_sort.c \
utils/frees.c \
utils/ft_safe_atoi.c \
utils/stack_mngr.c

OBJ = $(SRC:.c=.o)

all : $(NAME)

$(LIBFT):
	@make -C $(LIBFT_DIR)

$(NAME) : $(OBJ) $(LIBFT)
	$(CC) $(INC_FLAGS) $(FLAGS) $(OBJ) $(LIBFT) -o $(NAME)

%.o: %.c
	$(CC) $(INC_FLAGS) $(FLAGS) -c $< -o $@

clean : 
	@make clean -C $(LIBFT_DIR)
	rm -f $(OBJ)

fclean : clean
	@make fclean -C $(LIBFT_DIR)
	rm -f $(NAME)

re : fclean all

.PHONY : all clean fclean re
