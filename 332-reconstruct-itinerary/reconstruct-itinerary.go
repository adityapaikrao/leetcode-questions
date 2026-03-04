import (
    "slices"
)

func findItinerary(tickets [][]string) []string {
    // goal is to find a path that covers all edges once, starting from the src (essentially Euler path)
    // guaranteed that atleast one such path exists
    adj := make(map[string][]string, 0)
    for _, ticket := range tickets{
        adj[ticket[0]] = append(adj[ticket[0]], ticket[1])
    }

    // pointers to mark next vertices for each node
    nextNodes := make(map[string]int, 0)
    
    // sort to ensure traversal in lexical order
    for key := range adj{
        slices.Sort(adj[key])
    }

    order := make([]string, 0, len(tickets))
    // Do DFS until all edges are not visited
    var dfs func(node string)
    dfs = func(node string){
        // no new nbrs
        if nextNodes[node] == len(adj[node]){
            order = append(order, node)
            return
        }

        for i := range adj[node]{
            if i < nextNodes[node]{
                continue
            }
            nextNodes[node]++
            dfs(adj[node][i])
        }
        order = append(order, node)
        return

    }

    dfs("JFK")
    slices.Reverse(order)

    return order

}