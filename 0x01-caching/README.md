0x01-caching

What a caching system is: A caching system is an optimization technique that stores a subset of data in a faster storage medium, typically RAM, to speed up data retrieval. It reduces the time it takes to access data that is frequently used by temporarily storing it closer to the processing unit.

What FIFO means: FIFO, or "First In, First Out," is a straightforward cache eviction policy where the oldest data in the cache is removed first when new data needs to be stored. It's analogous to a queue, where the first element added is the first to be removed.

What LIFO means: LIFO, or "Last In, First Out," is another simple cache eviction strategy where the most recently added data is the first to be removed. This approach is similar to a stack, where the last element added is the first to be removed.

What LRU means: LRU, or "Least Recently Used," is a more sophisticated cache eviction policy that tracks the order of data usage. When the cache is full, the data that has not been accessed for the longest time is evicted first. This policy is particularly effective in scenarios where the most recently used data is likely to be accessed again soon.

What MRU means: MRU, or "Most Recently Used," is the opposite of LRU. In MRU, the data that was most recently used is the first to be removed when the cache needs space. This policy is less common and is used in specific situations where recently accessed data is less likely to be used again.

What LFU means: LFU, or "Least Frequently Used," is a cache eviction policy that counts the frequency of data usage and removes the data that has been accessed the least number of times. This approach is useful when access patterns are such that data accessed frequently in the past will continue to be accessed frequently in the future.

What the purpose of a caching system is: The purpose of a caching system is to enhance system performance by minimizing the time needed to access data. By storing frequently accessed data in a fast-access medium, caching reduces latency and decreases the load on the main data storage.

What limits a caching system have: The primary limits of a caching system include its finite storage capacity, which requires an efficient eviction strategy to manage space, and the potential for cache misses, which occur when requested data is not found in the cache. Additionally, the overhead of managing the cache, including the choice of eviction policy, can impact system performance. Balancing these factors is key to designing an effective caching strategy.
