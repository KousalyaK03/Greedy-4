class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # Approach:
        # Use a two-pointer technique to simulate forming the target string using subsequences of source.
        # For each character in the target, check if it exists in the source.
        # If not, return -1 as it's impossible to form the target. Otherwise, count how many passes
        # through the source are required to form the target by incrementing pointers appropriately.

        # Time Complexity: O(n * m), where n = length of source, m = length of target.
        # Space Complexity: O(1), as we use constant space.
        # Did this code successfully run on Leetcode: Yes
        # Any problem you faced while coding this: No

        source_set = set(source)  # To quickly check if a character in target exists in source
        count = 0  # To count the number of subsequences used
        i = 0  # Pointer for target string

        while i < len(target):
            # Check if the current target character exists in the source
            if target[i] not in source_set:
                return -1  # Target can't be formed if a character is missing from the source

            # Pointer for source string
            j = 0
            # Simulate forming a subsequence by iterating through source and target
            while i < len(target) and j < len(source):
                if target[i] == source[j]:
                    i += 1  # Move to the next character in target if matched
                j += 1  # Always move to the next character in source

            # Completed one pass through the source
            count += 1

        return count
