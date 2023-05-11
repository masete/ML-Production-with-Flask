# from .hello import hello
from .acquisitions import acquisitions
from .predictSeriesA import to_series_A
from .investors_view import investor
from .deals_view import deals
from .dealsList_view import deals_list
# from .investment_view import deals

blueprints = [acquisitions, to_series_A, investor, deals, deals_list]
