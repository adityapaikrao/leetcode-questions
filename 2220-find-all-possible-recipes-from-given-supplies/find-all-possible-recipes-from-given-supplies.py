class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        recipes = a b
        ingredients a -> c, b
                    b -> a, e

        c -> a 
        b -> a

        """
        recipes_set = set(recipes)
        adj = defaultdict(list) 
        in_degree = defaultdict(int)
        for list_ingredients, recipe in zip(ingredients, recipes):
            for src in list_ingredients:
                adj[src].append(recipe)
            in_degree[recipe] += len(list_ingredients)
        
        q = deque()
        for supply in supplies:
            if in_degree[supply] == 0:
                q.append(supply)
        
        can_make = []
        while q:
            curr = q.popleft()
            for nxt in adj[curr]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    q.append(nxt)
                    can_make.append(nxt)
        
        return can_make

