/*
if all pos -> prod array
if even neg -> prod array
if odd neg -> ignore one neg 

[2, 3, -2, 4, -6, 5, 3, -1, 7]
for each neg
-> max(a[:2], a[3:]) 
-> max(a[:4], a[5:])
-> max(a[:7], a[8:])

==> prod of prefixes or suffixes 
*/

func maxProduct(nums []int) int {
    prefixProd := 1
    suffixProd := 1
    maxProd := nums[0]

    for i := range nums{
        if prefixProd == 0{
            prefixProd = 1
        }
        if suffixProd == 0{
            suffixProd = 1
        }

        prefixProd *= nums[i]
        suffixProd *= nums[len(nums) - 1 - i]

        if prefixProd > maxProd && prefixProd >= suffixProd{
            maxProd = prefixProd
        } else if suffixProd > maxProd && suffixProd >= prefixProd{
            maxProd = suffixProd
        }
    }

    return maxProd
}