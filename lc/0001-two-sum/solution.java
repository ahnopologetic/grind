class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i = 0;
        int[] list = new int[2];
        while (i < nums.length) {
            // if (target - nums[i] )
            for (int j = i + 1; j < nums.length; j++) {
                if (target - nums[i] == nums[j]) {
                    // list.add(i);
                    // list.add(j);
                    list[0] = i;
                    list[1] = j;
                }
            }
            i++;
        }
        return list;
    }
}
