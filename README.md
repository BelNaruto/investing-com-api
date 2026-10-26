# Investing.com API — quotes, historical prices, economic calendar & news (2026)

[![RapidAPI](https://img.shields.io/badge/RapidAPI-Investing.com%20Ultimate%20API-0055DA?logo=rapid)](https://rapidapi.com/belchiorarkad-FqvHs2EDOtP/api/investing-com-ultimate-api)
[![Telegram support](https://img.shields.io/badge/Support-Telegram%20%40pintoflow-26A5E4?logo=telegram)](https://t.me/pintoflow)
![Updated](https://img.shields.io/badge/updated-October%202026-brightgreen)

An unofficial **Investing.com data API** with clean JSON for **stocks, ETFs, funds, indices, forex, crypto, commodities, bonds and certificates**: real-time quotes, historical OHLC prices, technical analysis, company financials, the **economic calendar**, earnings, dividends, IPOs and market news, in 32 languages.

👉 **Get your API key:** https://rapidapi.com/belchiorarkad-FqvHs2EDOtP/api/investing-com-ultimate-api

💬 **Questions? Faster support on Telegram: [@pintoflow](https://t.me/pintoflow)**

---

## Why this API

- **One consistent v2 interface** for every asset class: pick the asset, pass a `symbol` (and `country` for stocks/ETFs)
- **Historical prices** daily, weekly or monthly, with custom date ranges
- **Economic calendar** filtered by country and importance, plus earnings, dividends and IPO calendars
- **Company data:** profile, income statement, balance sheet, cash flow, ratios, earnings, analyst forecasts
- **Technical analysis:** moving averages, indicators and buy/sell signals
- **Market screens:** all stocks/ETFs/indices of a country, top gainers/losers/most active, crypto by market cap, government bond yields
- **News & analysis** per instrument or market-wide
- **Search** by ticker, ISIN or name
- **32 languages** and prices converted to **any currency**
- Actively maintained

## Quick start

Every request needs two headers:

| Header | Value |
|--------|-------|
| `X-RapidAPI-Key` | your key from the [RapidAPI page](https://rapidapi.com/belchiorarkad-FqvHs2EDOtP/api/investing-com-ultimate-api) |
| `X-RapidAPI-Host` | `investing-com-ultimate-api.p.rapidapi.com` |

### cURL

```bash
curl "https://investing-com-ultimate-api.p.rapidapi.com/v2/stocks?symbol=AAPL&country=US" \
  -H "X-RapidAPI-Key: YOUR_KEY" \
  -H "X-RapidAPI-Host: investing-com-ultimate-api.p.rapidapi.com"
```

### Python

```python
import requests

HOST = "investing-com-ultimate-api.p.rapidapi.com"
HEADERS = {"X-RapidAPI-Key": "YOUR_KEY", "X-RapidAPI-Host": HOST}

def get(path, **params):
    r = requests.get(f"https://{HOST}{path}", headers=HEADERS, params=params, timeout=30)
    r.raise_for_status()
    return r.json()

# Apple quote
print(get("/v2/stocks", symbol="AAPL", country="US"))

# Apple daily prices since January 2025
print(get("/v2/stocks/historical", symbol="AAPL", country="US", **{"from": "2025-01-01"}))

# High-impact US economic events
print(get("/v2/calendars/economic", countries="US", importance="high"))
```

### Node.js

```js
const HOST = "investing-com-ultimate-api.p.rapidapi.com";

async function get(path, params = {}) {
  const url = `https://${HOST}${path}?${new URLSearchParams(params)}`;
  const res = await fetch(url, {
    headers: { "X-RapidAPI-Key": process.env.RAPIDAPI_KEY, "X-RapidAPI-Host": HOST },
  });
  if (!res.ok) throw new Error(`${res.status} ${await res.text()}`);
  return res.json();
}

console.log(await get("/v2/currencies", { symbol: "EUR/USD" }));
console.log(await get("/v2/crypto/technical", { symbol: "BTC" }));
```

More runnable examples are in [`examples/`](examples).

## Endpoints (v2)

### Instrument data

`{asset}` is one of `stocks`, `etfs`, `funds`, `indices`, `currencies`, `crypto`, `commodities`, `bonds`, `certificates`.

| Endpoint | What you get |
|----------|--------------|
| `GET /v2/{asset}` | Quote and overview |
| `GET /v2/{asset}/historical` | Historical prices (`from`, `to`, `interval`: daily/weekly/monthly) |
| `GET /v2/{asset}/technical` | Technical analysis |
| `GET /v2/{asset}/news` | Latest news |
| `GET /v2/{asset}/related` | "People also watch" |
| `GET /v2/stocks/profile` | Company profile |
| `GET /v2/stocks/financials/{statement}` | Income statement, balance sheet, cash flow |
| `GET /v2/stocks/ratios` | Financial ratios |
| `GET /v2/stocks/earnings` | Earnings history |
| `GET /v2/{stocks or etfs}/dividends` | Dividends |
| `GET /v2/stocks/forecast` | Analyst forecast |

### Markets

| Endpoint | What you get |
|----------|--------------|
| `GET /v2/markets/stocks` | All stocks of a country |
| `GET /v2/markets/etfs` | All ETFs of a country |
| `GET /v2/markets/indices` | All indices of a country |
| `GET /v2/markets/movers` | Top gainers, losers, most active |
| `GET /v2/markets/commodities` | Metals, energy, grains, softs… |
| `GET /v2/markets/crypto` | Cryptocurrencies by market cap |
| `GET /v2/markets/bonds` | Government bond yields |

### Calendars

| Endpoint | What you get |
|----------|--------------|
| `GET /v2/calendars/economic` | Economic calendar (CPI, NFP, rate decisions…) |
| `GET /v2/calendars/earnings` | Companies reporting earnings |
| `GET /v2/calendars/dividends` | Ex-dividend dates |
| `GET /v2/calendars/ipo` | Upcoming IPOs |
| `GET /v2/calendars/splits` | Stock splits |
| `GET /v2/calendars/holidays` | Stock market holidays |

### Search & reference

| Endpoint | What you get |
|----------|--------------|
| `GET /v2/search` | Find a symbol, country or slug |
| `GET /v2/search/content` | Search news, analysis and economic events |
| `GET /v2/reference/editions` | The 32 supported languages |
| `GET /v2/reference/currencies` | Currencies for price conversion |
| `GET /v2/reference/countries` | Countries with stock markets |

Full parameter docs: see the **About** tab on [RapidAPI](https://rapidapi.com/belchiorarkad-FqvHs2EDOtP/api/investing-com-ultimate-api).

## Use cases

- Trading bots and backtesting with historical OHLC data
- Economic calendar widgets and macro alerts
- Portfolio trackers and stock screeners
- Fintech dashboards, Discord/Telegram finance bots
- Research notebooks and data science projects

## FAQ

**Is this the official Investing.com API?** No. Investing.com does not offer a public API; this is an independent, unofficial API that returns its data as clean JSON.

**What does it cost?** See the plans on the [RapidAPI pricing page](https://rapidapi.com/belchiorarkad-FqvHs2EDOtP/api/investing-com-ultimate-api/pricing).

**I need an endpoint or field that isn't there.** Message [@pintoflow on Telegram](https://t.me/pintoflow), we usually answer much faster there than through RapidAPI.

## Support

💬 Telegram: [@pintoflow](https://t.me/pintoflow) · 🔑 API: [RapidAPI listing](https://rapidapi.com/belchiorarkad-FqvHs2EDOtP/api/investing-com-ultimate-api)

---

*Not affiliated with or endorsed by Investing.com. "Investing.com" is a trademark of its respective owner.*
