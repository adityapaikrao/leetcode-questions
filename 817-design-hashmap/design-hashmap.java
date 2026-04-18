class MyHashMap {

    List<int[]>[] arr;
    int n=10000;

    public MyHashMap() {
        arr = new ArrayList[n];
        for(int i=0;i<n;i++){
            arr[i] = new ArrayList<>();
        }
        
    }
    
    public void put(int key, int value) {

        int idx = key%n;

        for(int[] p: arr[idx]){
            if(p[0]==key){
                p[1]=value;
                return;
            }
        }

        arr[idx].add(new int[]{key,value});
        
    }
    
    public int get(int key) {

        int idx = key%n;

        for(int[] p:arr[idx]){
            if(p[0]==key){
                    return p[1];
            }
        }
        return -1;
        
    }
    
    public void remove(int key) {

        int idx=key%n;
        arr[idx].removeIf(p->p[0]==key);
        
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */