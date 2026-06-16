class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) ->float:
        
        x = init
        while iterations>0:
            x = x-learning_rate*2*x;
            iterations -=1;
        return round(x,5)