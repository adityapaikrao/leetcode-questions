func reverse(x int) int {
    rev := 0
    mul := 1
    if x < 0 {
        mul = -1
        x = x * -1
    }

    for x > 0 {
        digit := x % 10
        rev = rev * 10 + digit
        x = x / 10
    }

    if (rev >> 31) == 0 {
        return rev * mul
    }

    return 0
}