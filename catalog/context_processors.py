from .models import Market, Strategy

def menu_markets(request):
    markets = Market.objects.all()

    return {'menu_markets': markets}

def menu_strategies(request):
    strategies = Strategy.objects.all()

    return {'menu_strategies': strategies}