import pandas as pd
import numpy as np


class SpiderUtils:
    def clean_df(self, df):
        df = df.fillna(value=np.nan)

        df.dropna(
            axis=0,
            # how="all", 
            how='any',
            inplace=True,
        )
        return df
