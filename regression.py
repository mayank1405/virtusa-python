from sklearn.linear_model import LinearRegression
import numpy as np
temperatures_list = [30, 31, 29, 32, 33, 34, 35]
def predict(temperatures):
    # Example historical temperature data
    

    # Step 1: Create X (day index)
    X = np.array(range(1, len(temperatures) + 1)).reshape(-1, 1)

    # Step 2: Create y (temperatures)
    y = np.array(temperatures)

    # Step 3: Train model
    model = LinearRegression()
    model.fit(X, y)

    # Step 4: Predict next day
    next_day = np.array([[len(temperatures) + 1]])
    prediction = model.predict(next_day)

    return (f"Predicted temperature for next day: {float(round(prediction[0],2))} Celsius")
if __name__=="__main__":
    a=predict(temperatures_list)
    print(a)