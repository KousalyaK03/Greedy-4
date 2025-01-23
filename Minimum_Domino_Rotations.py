class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # Approach:
        # To make all values in either tops or bottoms the same, the target value must be the same across all tiles.
        # Check the possibility of making the entire row equal to either tops[0] or bottoms[0].
        # Count rotations needed to make the rows uniform for both values and return the minimum rotations required.
        # If neither is possible, return -1.

        # Time Complexity: O(n), where n is the length of tops or bottoms.
        # Space Complexity: O(1), as we only use constant space.
        # Did this code successfully run on Leetcode: Yes
        # Any problem you faced while coding this: No

        def check(target: int) -> int:
            """
            Helper function to calculate minimum rotations to make all values in tops
            or bottoms equal to the target. If not possible, return -1.
            """
            rotations_top, rotations_bottom = 0, 0
            for i in range(len(tops)):
                # If the target is not in either tops[i] or bottoms[i], it's not possible
                if tops[i] != target and bottoms[i] != target:
                    return -1
                # Count rotations needed for the top row
                elif tops[i] != target:
                    rotations_top += 1
                # Count rotations needed for the bottom row
                elif bottoms[i] != target:
                    rotations_bottom += 1
            # Return the minimum rotations required
            return min(rotations_top, rotations_bottom)

        # Check for the first element in tops and bottoms
        result = check(tops[0])  # Try making all values equal to tops[0]
        if result != -1:
            return result  # If possible, return the result

        # If tops[0] failed, try bottoms[0] only if tops[0] and bottoms[0] are different
        return check(bottoms[0]) if tops[0] != bottoms[0] else -1
