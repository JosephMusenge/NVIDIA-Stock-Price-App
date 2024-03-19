# NVIDIA Stock Price App

This is a simple stock price app developed with Python and Streamlit. The purpose of this app is to provide users with insights into the historical performance of NVIDIA stock and to offer recommendations on whether to buy the stock today or wait for a better opportunity based on the trend.

## Features

- Displays the historical closing prices and volume of NVIDIA stock in the past two years.
- Calculates moving averages to identify trends.
- Provides recommendations on whether to buy the stock today or wait for a better opportunity.
- Offers predictions on when to check back for potential buying opportunities.

## How to Use

1. Clone this repository to your local machine.
2. Install the required dependencies listed in `requirements.txt` by running:
3. Run the Streamlit app by executing the following command in your terminal (refer to streamlit docs for more):
4. Access the app in your web browser at the specified URL (http://localhost:8501).

## App Overview

The app displays the historical closing prices and volume of NVIDIA stock in the form of line charts. It calculates moving averages to identify trends and provides a recommendation on whether to buy the stock today or wait for a better opportunity based on the current trend.

## Recommendation Logic

The recommendation provided by the app is based on the following logic:

- If the current closing price is higher than the 50-day moving average, which is higher than the 200-day moving average, the recommendation is to **buy your stock today**.
- If the 50-day moving average is higher than the 200-day moving average, the recommendation is to **wait for a dip, then buy**. The app also predicts when to check back for a potential buying opportunity, typically after 7 days.
- If the trend is not clear (i.e., the 200-day moving average is higher than the 50-day moving average), the recommendation is to **wait for a clearer trend**. The app predicts when to check back for a clearer trend, typically after 2 weeks.

## Project Video Walkthrough

Here's a walkthrough of implemented features:

<img src='./assets/nvidiastockprice.gif' title='Video Walkthrough' width='' alt='Video Walkthrough' />

GIF created with [LiceCap](https://www.cockos.com/licecap/) for Windows

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- This app utilizes the [yfinance](https://github.com/ranaroussi/yfinance) library for fetching historical stock data.
- Streamlit is used for building the interactive web application.
- Special thanks to the developers and maintainers of the libraries and tools used in this project.
