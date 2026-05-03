#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PRINTF_DIR="$(dirname "$SCRIPT_DIR")"
PROJECT_ROOT="$(dirname "$PRINTF_DIR")"

TEST_DIR="$SCRIPT_DIR"
LIB="$PRINTF_DIR/libftprintf.a"

mkdir -p "$TEST_DIR"

cat > "$TEST_DIR/main.c" << 'EOF'
#include "../ft_printf.h"
#include <stdio.h>
#include <limits.h>
#include "../ft_printf.h"

static int g_tests = 0;
static int g_passed = 0;

static void assert_eq(const char *name, int my_ret, int orig_ret)
{
	g_tests++;
	if (my_ret == orig_ret)
	{
		g_passed++;
		printf("[PASS] %s (ret: %d)\n", name, my_ret);
	}
	else
	{
		printf("[FAIL] %s\n", name);
		printf("  my_ret: %d | orig_ret: %d\n", my_ret, orig_ret);
	}
}

static void test_mandatory(void)
{
	int r, o;

	printf("\n--- Mandatory tests ---\n");

	r = ft_printf("Hello %s\n", "World");
	o = printf("Hello %s\n", "World");
	assert_eq("string", r, o);

	r = ft_printf("Number: %d\n", 42);
	o = printf("Number: %d\n", 42);
	assert_eq("int positive", r, o);

	r = ft_printf("Negative: %d\n", -42);
	o = printf("Negative: %d\n", -42);
	assert_eq("int negative", r, o);

	r = ft_printf("INT_MIN: %d\n", INT_MIN);
	o = printf("INT_MIN: %d\n", INT_MIN);
	assert_eq("int min", r, o);

	r = ft_printf("INT_MAX: %d\n", INT_MAX);
	o = printf("INT_MAX: %d\n", INT_MAX);
	assert_eq("int max", r, o);

	r = ft_printf("Zero: %d\n", 0);
	o = printf("Zero: %d\n", 0);
	assert_eq("int zero", r, o);

	r = ft_printf("Unsigned: %u\n", 0);
	o = printf("Unsigned: %u\n", 0);
	assert_eq("uint zero", r, o);

	r = ft_printf("Unsigned: %u\n", UINT_MAX);
	o = printf("Unsigned: %u\n", UINT_MAX);
	assert_eq("uint max", r, o);

	r = ft_printf("Hex: %x\n", 255);
	o = printf("Hex: %x\n", 255);
	assert_eq("hex lowercase", r, o);

	r = ft_printf("Hex: %X\n", 255);
	o = printf("Hex: %X\n", 255);
	assert_eq("hex uppercase", r, o);

	r = ft_printf("Hex: %x\n", 0);
	o = printf("Hex: %x\n", 0);
	assert_eq("hex zero", r, o);

	r = ft_printf("Char: %c\n", 'A');
	o = printf("Char: %c\n", 'A');
	assert_eq("char", r, o);

	r = ft_printf("Char: %c\n", 0);
	o = printf("Char: %c\n", 0);
	assert_eq("char null", r, o);

	r = ft_printf("Percent: %%\n");
	o = printf("Percent: %%\n");
	assert_eq("percent", r, o);

	r = ft_printf("Null str: %s\n", "(null)");
	o = printf("Null str: %s\n", "(null)");
	assert_eq("string null repr", r, o);

	r = ft_printf("Ptr: %p\n", (void *)0xdeadbeef);
	o = printf("Ptr: %p\n", (void *)0xdeadbeef);
	assert_eq("pointer", r, o);

	r = ft_printf("Ptr null: %p\n", (void *)0);
	o = printf("Ptr null: %p\n", (void *)0);
	assert_eq("pointer null", r, o);

	r = ft_printf("Combined: %d %s %c %p\n", 123, "ok", 'X', (void *)12345);
	o = printf("Combined: %d %s %c %p\n", 123, "ok", 'X', (void *)12345);
	assert_eq("combined", r, o);
}

static void test_bonus(void)
{
	int r, o;

	printf("\n--- Bonus tests ---\n");

	r = ft_printf("%-10s|\n", "hi");
	o = printf("%-10s|\n", "hi");
	assert_eq("minus string", r, o);

	r = ft_printf("%05d\n", 42);
	o = printf("%05d\n", 42);
	assert_eq("zero pad", r, o);

	r = ft_printf("%.3s\n", "hello");
	o = printf("%.3s\n", "hello");
	assert_eq("precision str", r, o);

	r = ft_printf("%.5d\n", 42);
	o = printf("%.5d\n", 42);
	assert_eq("precision int", r, o);

	r = ft_printf("%#.8x\n", 42);
	o = printf("%#.8x\n", 42);
	assert_eq("hash hex", r, o);

	r = ft_printf("%+d\n", 42);
	o = printf("%+d\n", 42);
	assert_eq("plus flag", r, o);

	r = ft_printf("%+d\n", -42);
	o = printf("%+d\n", -42);
	assert_eq("plus flag negative", r, o);

	r = ft_printf("% d\n", 42);
	o = printf("% d\n", 42);
	assert_eq("space flag", r, o);

	r = ft_printf("%10.5d\n", 42);
	o = printf("%10.5d\n", 42);
	assert_eq("width precision int", r, o);

	r = ft_printf("%.0d\n", 0);
	o = printf("%.0d\n", 0);
	assert_eq("precision zero int zero", r, o);

	r = ft_printf("%-5d| %-5d|\n", 42, -42);
	o = printf("%-5d| %-5d|\n", 42, -42);
	assert_eq("minus pad", r, o);

	r = ft_printf("%#x\n", 0);
	o = printf("%#x\n", 0);
	assert_eq("hash zero hex", r, o);

	r = ft_printf("%-10p\n", (void *)0x123);
	o = printf("%-10p\n", (void *)0x123);
	assert_eq("minus pointer", r, o);

	r = ft_printf("%-5.5u|\n", 42);
	o = printf("%-5.5u|\n", 42);
	assert_eq("minus width precision uint", r, o);

	r = ft_printf("%#X\n", 255);
	o = printf("%#X\n", 255);
	assert_eq("hash uppercase hex", r, o);
}

int main(void)
{
	test_mandatory();
	test_bonus();

	printf("\n=== Results: %d/%d tests passed ===\n", g_passed, g_tests);
	return (g_passed == g_tests ? 0 : 1);
}
EOF

echo "=== Building libftprintf.a (bonus) ==="
cd "$PRINTF_DIR"
make fclean
make bonus
if [ $? -ne 0 ]; then
	echo "Compilation failed!"
	exit 1
fi

echo ""
echo "=== Running tests ==="
cc -Wall -Wextra -Werror "$TEST_DIR/main.c" "$LIB" -o "$TEST_DIR/printf_test"
if [ $? -ne 0 ]; then
	echo "Test compilation failed!"
	exit 1
fi

"$TEST_DIR/printf_test"
RESULT=$?

echo ""
echo "=== Cleanup ==="
rm -f "$TEST_DIR/main.c" "$TEST_DIR/printf_test"

exit $RESULT
