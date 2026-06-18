class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        max_freq = 0
        num_max_freq_tasks = 0
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
            if freq[ord(task) - ord('A')] == max_freq:
                num_max_freq_tasks += 1
            elif freq[ord(task) - ord('A')] > max_freq:
                max_freq = freq[ord(task) - ord('A')]
                num_max_freq_tasks = 1
        
        parts = max_freq - 1
        part_len = n - num_max_freq_tasks + 1
        empty_slots = parts * part_len

        remaining_task = len(tasks) - (max_freq * num_max_freq_tasks)
        idle_time = max(0, empty_slots - remaining_task)

        return len(tasks) + idle_time