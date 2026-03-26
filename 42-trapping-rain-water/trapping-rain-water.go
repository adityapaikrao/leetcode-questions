/*

[0,1,0,2,1,0,1,3,2,1,2,1]
   0 
   i 
                     j
 lmax = 0
 rmax = 1
 water = min(lmax, rmax) - height => 

 if lmax < rmax: 
    can def store (lmax - height) water at i
    i++
    lmax: update
else:
    can def store (lmax - height) water at i
    j++
    rmax: update

*/

func trap(height []int) int {
    if len(height) <= 1 {
        return 0
    }
    lmax := height[0]
    rmax := height[len(height) - 1]

    i := 1
    j := len(height) - 2
    water := 0

    for i <= j {
        if lmax <= rmax{
            if lmax > height[i]{
                water += lmax - height[i]
            } else{
                lmax = height[i]
            }
            i++
        } else{
            if rmax > height[j]{
                water += rmax - height[j]
            } else {
                rmax = height[j]
            }
            j--
        }
    }
    return water
}