int maxProfit(int* prices, int pricesSize) {

    //take the first value, set that equal to the low, if it gets lower good
    //take the profit from the low right now (if its higher)

    int low = prices[0];
    int profit = 0;


    for(int day = 0; day < pricesSize; day++){
        if(prices[day] < low){
            low = prices[day];
        }

        if(prices[day] - low > profit){
            profit = prices[day] - low;
        }

    }

    return profit;
    
}