import sys
from pathlib import Path

# Hyperopt 
# freqtrade download-data --exchange binanceusdm -t 5m 15m 1h --days 300
# freqtrade download-data --exchange binanceusdm -t 1d --days 600
# Hyperopt stoploss
# freqtrade hyperopt --hyperopt-loss OnlyProfitHyperOptLoss --spaces stoploss --timeframe 5m -e 10000 --print-all --strategy NostalgiaForInfinityXLeverage -j 8 --timerange=20211001-
# Backtesting
# freqtrade backtesting --timeframe 5m --strategy NostalgiaForInfinityXLeverage --timerange=20211001-

sys.path.append(str(Path(__file__).parent))

from NostalgiaForInfinityX import NostalgiaForInfinityX


class NostalgiaForInfinityXLeverage(NostalgiaForInfinityX):
    leverage_size = 3.0
    
    def leverage(self, pair: str, current_time, current_rate: float, proposed_leverage: float, max_leverage: float, side: str, **kwargs) -> float:
        """
        Customize leverage for each new trade.
        :param pair: Pair that's currently analyzed
        :param current_time: datetime object, containing the current datetime
        :param current_rate: Rate, calculated based on pricing settings in ask_strategy.
        :param proposed_leverage: A leverage proposed by the bot.
        :param max_leverage: Max leverage allowed on this pair
        :param side: 'long' or 'short' - indicating the direction of the proposed trade
        :return: A leverage amount, which is between 1.0 and max_leverage.
        """
        return self.leverage_size
    