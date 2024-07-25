class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max = 0;
        int low = prices[0];
        for(int i=0; i < prices.size()-1; i++)
        {
            // the key observation is that to buy at local minimum and sell at the next local maximum 
            if (prices[i] > prices[i+1])
            {
                max += prices[i] - low;
                low = prices[i+1];
            }
        }
        if(prices[prices.size()-1] > low)
        {
            max += prices[prices.size()-1] - low;
        }
        return max;
    }
};