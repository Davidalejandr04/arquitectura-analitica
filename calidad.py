import pandas as pd # type: ignore

def validate_data(file_path):
    df = pd.read_csv(file_path)

    print("Validación de valores nulos...")
    nulls = df.isnull().sum()
    print(nulls)

    df = df.dropna()

    print("Datos validados exitosamente.")
    return df

if __name__ == "__main__":
    validated_df = validate_data("data.csv")
    validated_df.to_csv("datosvalidados.csv", index=False)