#include <iostream>

int main()
{
	return 0;
}

/*
 * Compiling code would take 450 microseconds
 */

template<class Iterator>
size_t seq_calc_sum(Iterator begin, Iterator end) {
	size_t x = 0;
	std::for_each(begin, end, [&](int item) {
		x += item;
	});
	return x;
}

