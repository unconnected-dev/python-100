class CurrencyHandler:
    CURRENCY_SYMBOL = "$"

    def __init__(self) -> None:
        pass
    
    def getFormattedCurrency(self, value) -> str:
        """Formats float to string"""
        return '{}{:,.2f}'.format(self.CURRENCY_SYMBOL, value)