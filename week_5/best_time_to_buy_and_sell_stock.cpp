class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max = 0;
        int lsf = 999999;
        for(int i=0; i< prices.size(); i++)
        {
            if (prices[i] < lsf)
            {
                lsf = prices[i];
            }

            if (prices[i] - lsf > max)
            {
                max = prices[i] - lsf;
            }
        }
        return max;
    }
};