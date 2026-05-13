func numBusesToDestination(routes [][]int, source int, target int) int {
    if source == target {
        return 0
    }

    stopMap := make(map[int][]int, 0)
    for busNum, stops := range routes {
        for _, stop := range stops {
            stopMap[stop] = append(stopMap[stop], busNum)
        }

    }

    q := make([]int, 0) // q to store the busNum currently visited
    visited := make([]bool, len(routes)) // track with stops have been visited
    for _, busNum := range stopMap[source] {
        q = append(q, busNum)
        visited[busNum] = true
    }

    numBuses := 1 // have to start with 1 bus (soruce bus)

    for len(q) > 0 {
        currBuses := len(q) // number of buses at current level
        // fmt.Println("level", numBuses, q)

        for range currBuses {
            busNum := q[0]
            q = q[1:] // pop bus from front

            for _, stop := range routes[busNum] {
                if stop == target {
                    return numBuses
                }
                for _, nextBus := range stopMap[stop] {
                    if !visited[nextBus] {
                        q = append(q, nextBus)
                        visited[nextBus] = true
                    }
                }
            }
        }
        numBuses++
    }

    return -1;

}