import (
    "slices"
)

func plusOne(digits []int) []int {
    newDigits := make([]int, 0, len(digits) + 1)
    carry := 1
    for i := len(digits) - 1; i >= 0; i--{
        currDigit := carry + digits[i]
        carry = currDigit / 10
        currDigit = currDigit % 10

        newDigits = append(newDigits, currDigit)
    }

    if carry != 0{
        newDigits = append(newDigits, carry)
    }

    slices.Reverse(newDigits)

    return newDigits
}