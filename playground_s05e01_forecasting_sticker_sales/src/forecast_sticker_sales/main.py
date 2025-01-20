from loguru import logger
import pandas as pd


def load_data():
    logger.info("Loading data")
    data = pd.read_csv("data/train.csv")
    logger.info(f"Data loaded: {data.head()}")
    return


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Transforming data")

    return


def main():
    logger.info("Forecasting sticker sales")
    load_data()
    return


if __name__ == "__main__":
    main()
