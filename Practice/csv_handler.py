import pandas as pd
import numpy as np
import torch
from sklearn.preprocessing import MinMaxScaler

class CsvHandler:
    def __init__(self, filename: str) -> None:
        self._df = pd.read_csv(filename)
        self._normalized_df = CsvHandler.get_normalized(self._df)
        self._normalized_tensor = CsvHandler.get_tensor(self._normalized_df)

    def print(self):
        print(self._df)
        
    def print_average(self) -> None:
        print(f'\nAverage power: {self._df['power'].mean()}')
        print(f'Average viscosity: {self._df['viscosity'].mean()}')
        print(f'Average color intensity: {self._df['color_intensity'].mean()}')
        
    def print_max(self) -> None:
        max_power_row = self._df[self._df['power'] == self._df["power"].max()]
        max_viscosity_row = self._df[self._df['viscosity'] == self._df["viscosity"].max()]
        max_color_intensity_row = self._df[self._df['color_intensity'] == self._df["color_intensity"].max()]

        print(f'\nMax power: {max_power_row['name'].iloc[0]}, {max_power_row['power'].iloc[0]}')
        print(f'Max viscosity: {max_viscosity_row['name'].iloc[0]}, {max_viscosity_row['viscosity'].iloc[0]}')
        print(f'Max color intensity: {max_color_intensity_row['name'].iloc[0]}, {max_color_intensity_row['color_intensity'].iloc[0]}')
        
    def print_min(self) -> None:
        min_power_row = self._df[self._df['power'] == self._df["power"].min()]
        min_viscosity_row = self._df[self._df['viscosity'] == self._df["viscosity"].min()]
        min_color_intensity_row = self._df[self._df['color_intensity'] == self._df["color_intensity"].min()]

        print(f'\nMin power: {min_power_row['name'].iloc[0]}, {min_power_row['power'].iloc[0]}')
        print(f'Min viscosity: {min_viscosity_row['name'].iloc[0]}, {min_viscosity_row['viscosity'].iloc[0]}')
        print(
            f'Min color intensity: {min_color_intensity_row['name'].iloc[0]}, {min_color_intensity_row['color_intensity'].iloc[0]}')

    def get_normalized(df_to_normalize: pd.DataFrame) -> pd.DataFrame:
        num_cols = df_to_normalize.select_dtypes(include=['float64']).columns
        scaler = MinMaxScaler()

        df_to_normalize[num_cols] = scaler.fit_transform(df_to_normalize[num_cols])

        return df_to_normalize
        
    def print_normalized(self) -> None:
        print(self._normalized_df)

    def get_tensor(df_to_tensor: pd.DataFrame) -> torch.Tensor:
        num_cols = df_to_tensor.select_dtypes(include=['float64']).columns
        data_np = df_to_tensor[num_cols].values

        return torch.tensor(data_np, dtype=torch.float32)

    def print_tensor(self) -> None:
        print(self._normalized_tensor)

    def save_to_csv(self, filename: str) -> None:
        np_array = self._normalized_tensor.numpy()
        df_to_csv = pd.DataFrame(np_array, columns=['power', 'viscosity', 'color_intensity'])
        df_to_csv.to_csv(filename, index=False)