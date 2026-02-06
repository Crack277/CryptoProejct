import { Card } from "antd";
import numberWithCommas from "../utils.js";
import "./CryptocurrencyCard.css";

function CryptocurrencyCard(props) {
  const { currency } = props;

  const priceChange = Math.round(100 * currency.percent_change_24h) / 100;
  const formattedPrice = numberWithCommas(currency.price.toFixed(2));
  const formattedMarketCap = numberWithCommas(Math.round(currency.market_cap / 1_000_000_000));

  const priceChangeClass = priceChange > 0 ? 'change-positive' : 'change-negative';

  return (
    <div className="p-4">
      <Card
        title={
          <div className="flex items-center gap-3">
            <img
              src={`https://s2.coinmarketcap.com/static/img/coins/64x64/${currency.id}.png`}
              alt='logo'
              className="crypto-logo"
            />
            <p className="crypto-name">{currency.name}</p>
          </div>
        }
        bordered={false}
        className="crypto-card"
        style={{
          width: 700,
          height: 500,
        }}
      >
        <div className="crypto-content">
          {/* Текущая цена */}
          <div className="data-field">
            <span className="data-label">Текущая цена</span>
            <span className="data-value price-value">${formattedPrice}</span>
          </div>

          {/* Изменение цены */}
          <div className="data-field">
            <div className="price-change-container">
              <span className="change-label">Изменение за 24 часа:</span>
              <span className={`change-value ${priceChangeClass}`}>
                {priceChange > 0 ? '+' : ''}{priceChange}%
              </span>
            </div>
          </div>

          {/* Капитализация */}
          <div className="data-field">
            <span className="data-label">Рыночная капитализация</span>
            <span className="data-value market-cap-value">${formattedMarketCap}B</span>
          </div>
        </div>
      </Card>
    </div>
  );
}

export default CryptocurrencyCard;