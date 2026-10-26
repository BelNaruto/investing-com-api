// Download historical daily prices for a stock (Investing.com data) with Node.js 18+.
// Get your key: https://rapidapi.com/belchiorarkad-FqvHs2EDOtP/api/investing-com-ultimate-api
// Usage:  RAPIDAPI_KEY=xxx node historical_prices.mjs AAPL US 2025-01-01

const HOST = "investing-com-ultimate-api.p.rapidapi.com";
const [symbol = "AAPL", country = "US", from = "2025-01-01"] = process.argv.slice(2);

const params = new URLSearchParams({ symbol, country, from, interval: "daily" });
const res = await fetch(`https://${HOST}/v2/stocks/historical?${params}`, {
  headers: { "X-RapidAPI-Key": process.env.RAPIDAPI_KEY, "X-RapidAPI-Host": HOST },
});
if (!res.ok) throw new Error(`${res.status} ${await res.text()}`);
console.log(JSON.stringify(await res.json(), null, 2));
