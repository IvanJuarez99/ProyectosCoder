class CurrencyPipe:
    @staticmethod
    def transform(value: float) -> str:
        formatted_value = f"{value:,.2f}" 
        formatted_value = formatted_value.replace(",", "X").replace(".", ",").replace("X", ".")
        return f"${formatted_value}" 
#necesitaba serparar con . cada 3 ceros y no funcionaba el import locale asi que tuve que improvisar.
