# Python3+ Stock Trade Client

## Set-up

Just:
```
cp conf.py.template conf.py
```

Then edit this (minimalist) configuration file and you're good to go.

## Usage

```python
from core.trade import TradeMaker, OrderTypes

t = Trademaker("HOGE123456789") #Bank account

# Buy 10 stocks of "HOGE" @ $80
t.buy("HOGE", "FOOEX", 80 * 100, 10, Ordertypes.FOK)

# Profits
t.sell("HOGE", "FOOEX", 81 * 100, 10, Ordertypes.Limit)
```

